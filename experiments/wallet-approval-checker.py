#!/usr/bin/env python3
"""
钱包授权检查 Agent — CLI 工具
检查合约风险：扫描源码中的危险函数、检查授权额度、评估合约可信度
"""

import json
import os
import sys
import urllib.request
import urllib.error
import re
from datetime import datetime, timezone

# ============================================================
# 配置
# ============================================================
ETHERSCAN_API_KEY = os.environ.get("ETHERSCAN_API_KEY", "")
SEPOLIA_API_URL = "https://api-sepolia.etherscan.io/api"
MAINNET_API_URL = "https://api.etherscan.io/api"

# ============================================================
# 危险模式库
# ============================================================
DANGER_PATTERNS = [
    {
        "name": "Reentrancy（重入攻击）",
        "patterns": [
            r"(?i)(\.call\s*\{[^}]*\}\s*\([^)]*\)\s*[;]?\s*.*(?:balance|transfer|withdraw|send))",
            r"(?i)(\.transfer\(.*\)\s*[;]?\s*.*(?:if|while|for)\s*[^;]*balance)",
        ],
        "severity": "high",
        "detail": "合约在更新状态前调用了外部合约，可能存在重入攻击风险"
    },
    {
        "name": "delegatecall 使用",
        "patterns": [r"(?i)delegatecall"],
        "severity": "high",
        "detail": "delegatecall 让外部合约在你的合约上下文中执行代码，等同于把控制权交给对方"
    },
    {
        "name": "selfdestruct / suicide",
        "patterns": [r"(?i)(selfdestruct|suicide)\s*\("],
        "severity": "high",
        "detail": "合约自毁功能可以将合约中的 ETH 强制发送到任意地址"
    },
    {
        "name": "未受保护的 initialize",
        "patterns": [
            r"(?i)function\s+initialize\b[^{]*\{[^}]*initializer[^}]*\}"
        ],
        "severity": "medium",
        "detail": "检查 initialize 是否有修饰符保护，防止重入初始化"
    },
    {
        "name": "tx.origin 鉴权",
        "patterns": [r"(?i)tx\.origin"],
        "severity": "medium",
        "detail": "tx.origin 鉴权容易被钓鱼攻击绕过，建议使用 msg.sender"
    },
    {
        "name": "block.timestamp 依赖",
        "patterns": [r"(?i)block\.timestamp"],
        "severity": "low",
        "detail": "依赖 block.timestamp 做关键判断可能被矿工轻微操纵"
    },
]

OWNERSHIP_PATTERNS = [
    {
        "name": "Ownership 可转移",
        "patterns": [
            r"(?i)function\s+(transferOwnership|renounceOwnership)\s*\(",
            r"(?i)event\s+OwnershipTransferred",
        ],
        "severity": "medium",
        "detail": "Owner 权限可以被转移或放弃"
    },
    {
        "name": "onlyOwner 修饰符",
        "patterns": [r"(?i)onlyOwner"],
        "severity": "info",
        "detail": "合约使用了 onlyOwner 保护关键函数，需确认 owner 地址是否安全"
    },
]

APPROVAL_PATTERNS = [
    {
        "name": "无限额度授权",
        "patterns": [r"(?i)(type\(uint256\)\.max|2\s*\*\*\s*256\s*-\s*1|MAX_UINT|maxUint256)"],
        "severity": "medium",
        "detail": "合约请求无限额度授权，一旦授权恶意合约可转走所有代币。建议使用自定义额度"
    },
]

# ERC20 ABI（简版，仅用于查询 balanceOf 和 allowance）
ERC20_BALANCE_ABI = {
    "balanceOf": '0x70a08231',
    "allowance": '0xdd62ed3e',
    "decimals":  '0x313ce567',
}

MOCK_BALANCES = {
    "0x7a250d5630b4cf539739df2c5dacb4c659f2488d": {
        "usdc":  {"balance": 100_500_000,  "decimals": 6,  "symbol": "USDC"},
        "weth":  {"balance": 500_000_000_000_000_000, "decimals": 18, "symbol": "WETH"},
        "dai":   {"balance": 2_000_000_000_000_000_000_000, "decimals": 18, "symbol": "DAI"},
    }
}


# ============================================================
# 工具函数
# ============================================================
def color(s, code):
    """终端颜色"""
    return f"\033[{code}m{s}\033[0m" if sys.stdout.isatty() else s

def red(s):    return color(s, "91")
def green(s):  return color(s, "92")
def yellow(s): return color(s, "93")
def blue(s):   return color(s, "94")
def gray(s):   return color(s, "90")
def bold(s):   return color(s, "1")

def risk_label(severity):
    labels = {
        "high":   red("🔴 高风险"),
        "medium": yellow("🟡 中风险"),
        "low":    blue("🔵 低风险"),
        "info":   gray("ℹ️  参考信息"),
    }
    return labels.get(severity, severity)


# ============================================================
# Etherscan API
# ============================================================
def etherscan_api(network, action, address, apikey=""):
    """调用 Etherscan API"""
    base = SEPOLIA_API_URL if network == "sepolia" else MAINNET_API_URL
    url = f"{base}?module=contract&action={action}&address={address}"
    if apikey:
        url += f"&apikey={apikey}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "WalletChecker/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        if data.get("status") == "1":
            return data.get("result", [])
        elif "rate" in data.get("message", "").lower() or "max" in data.get("message", "").lower():
            return None, "rate_limit"
        else:
            return None, data.get("message", "Unknown error")
    except Exception as e:
        return None, str(e)


def analyze_contract_code(source_code):
    """分析合约源码中的风险模式"""
    findings = []

    # 展平源码（多层合约可能嵌套 JSON）
    if isinstance(source_code, str):
        # 可能是 JSON 多文件格式
        try:
            parsed = json.loads(source_code)
            if isinstance(parsed, dict):
                sources = []
                for key, val in parsed.get("sources", {}).items():
                    sources.append(val.get("content", ""))
                source_code = "\n".join(sources)
        except (json.JSONDecodeError, TypeError):
            pass

    if not source_code or not isinstance(source_code, str):
        return [{"name": "源码为空", "severity": "high", "detail": "无法获取合约源码", "matched": False}]

    # 扫描危险函数
    for pattern in DANGER_PATTERNS:
        found_any = False
        for p in pattern["patterns"]:
            if re.search(p, source_code):
                found_any = True
                break
        if found_any:
            findings.append({
                "name": pattern["name"],
                "severity": pattern["severity"],
                "detail": pattern["detail"],
                "matched": True
            })

    # 扫描权限相关
    for pattern in OWNERSHIP_PATTERNS:
        found_any = False
        for p in pattern["patterns"]:
            if re.search(p, source_code):
                found_any = True
                break
        if found_any:
            findings.append({
                "name": pattern["name"],
                "severity": pattern["severity"],
                "detail": pattern["detail"],
                "matched": True
            })

    # 检查无限授权
    for pattern in APPROVAL_PATTERNS:
        found_any = False
        for p in pattern["patterns"]:
            if re.search(p, source_code):
                found_any = True
                break
        if found_any:
            findings.append({
                "name": pattern["name"],
                "severity": pattern["severity"],
                "detail": pattern["detail"],
                "matched": True
            })

    return findings


# ============================================================
# Mock 数据（无 API Key 时演示用）
# ============================================================
def mock_check():
    """Mock 模式示例数据"""
    mock_addr = "0x7a250d5630b4cf539739df2c5dacb4c659f2488d"
    balances = MOCK_BALANCES.get(mock_addr, {})
    
    return {
        "contract_name": "UniswapV2Router02",
        "verified": True,
        "compiler": "v0.6.6+commit.6c089d02",
        "deployed_at": "2023-06-15 (大约 2 年前)",
        "tx_count": "152,340 笔交易",
        "balances": balances,
        "source_code": """// 模拟源码片段
contract UniswapV2Router02 {
    address public owner;
    modifier onlyOwner() { require(msg.sender == owner); _; }
    function transferOwnership(address newOwner) public onlyOwner { owner = newOwner; }
    
    function swapExactTokensForTokens(
        uint amountIn, uint amountOutMin,
        address[] calldata path, address to, uint deadline
    ) external returns (uint[] memory amounts) {
        // Transfer tokens from user
        IERC20(path[0]).transferFrom(msg.sender, address(this), amountIn);
        // Swap logic...
    }
    
    function withdraw() public onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
    
    receive() external payable {}
}""",
        "findings": [
            {"name": "onlyOwner 修饰符", "severity": "info", "detail": "合约使用 onlyOwner 保护关键函数，需确认 owner 地址安全性", "matched": True},
            {"name": "Ownership 可转移", "severity": "medium", "detail": "Owner 权限可以被转移，确认 owner 地址可信", "matched": True},
            {"name": "withdraw 函数", "severity": "info", "detail": "合约有提款函数，但受 onlyOwner 保护", "matched": True},
        ],
        "overall": "medium",
        "recommendation": "合约已开源且经过审计，但授权时建议使用自定义额度而非无限授权"
    }


# ============================================================
# 主逻辑
# ============================================================
def check_contract(address, network="sepolia", apikey=""):
    """检查一个合约地址"""
    print(f"\n{'='*60}")
    print(f"  🔍 检查合约: {address}")
    print(f"  网络: {network}")
    print(f"{'='*60}")

    # 无 API Key → 使用 Mock 演示
    if not apikey:
        print(yellow("\n  ⚠️  未设置 ETHERSCAN_API_KEY，使用演示数据"))
        print(gray("  设置方法: export ETHERSCAN_API_KEY=你的密钥\n"))
        result = mock_check()
    else:
        # 获取合约源码
        result_data = etherscan_api(network, "getsourcecode", address, apikey)
        if isinstance(result_data, tuple) and result_data[1] == "rate_limit":
            print(red("\n  ⚠️  API 请求频率超限，稍后再试"))
            return
        if not result_data or (isinstance(result_data, tuple)):
            print(red(f"\n  ⚠️  查询失败: {result_data[1] if isinstance(result_data, tuple) else '未知错误'}"))
            return

        info = result_data[0] if isinstance(result_data, list) else {}
        contract_name = info.get("ContractName", "Unknown")
        source_code = info.get("SourceCode", "")
        compiler = info.get("CompilerVersion", "未知")
        verified = bool(info.get("ABI", "")) and bool(source_code)

        # 分析源码
        findings = analyze_contract_code(source_code) if verified else [
            {"name": "合约未开源", "severity": "high",
             "detail": "合约源码未在 Etherscan 上验证，无法分析代码风险", "matched": True}
        ]

        result = {
            "contract_name": contract_name,
            "verified": verified,
            "compiler": compiler,
            "findings": findings,
        }

    # ========== 输出报告 ==========
    c = result
    print(f"\n  📄 合约: {bold(c.get('contract_name', '未知'))}")
    print(f"  {'✅ 已开源验证' if c.get('verified') else '❌ 未开源'}")
    if c.get("compiler"):
        print(f"  🔧 编译器: {c['compiler']}")
    if c.get("deployed_at"):
        print(f"  🕐 部署时间: {c['deployed_at']}")
    if c.get("tx_count"):
        print(f"  🔄 交互次数: {c['tx_count']}")

    # 代币余额 + 建议授权额度
    balances = c.get("balances", {})
    if balances:
        print(f"\n{'─'*60}")
        print(f"  💰 代币余额与建议授权额度")
        print(f"{'─'*60}")
        for token_key, info in balances.items():
            symbol = info.get("symbol", token_key.upper())
            raw_bal = info.get("balance", 0)
            dec = info.get("decimals", 18)
            bal = raw_bal / (10 ** dec)
            # 建议额度 = 余额 + 10% 缓冲
            suggested = bal * 1.1
            print(f"\n  {symbol}: {bal:,.4f}")
            print(f"     建议授权额度: {green(f'{suggested:,.4f} ' + symbol)}（余额 + 10% 缓冲）")
            print(f"     而非: {red('无限额度 (Unlimited)')}")

    # 安全发现
    findings = c.get("findings", [])
    print(f"\n{'─'*60}")
    print(f"  安全扫描发现 ({len(findings)} 项)")
    print(f"{'─'*60}")

    high_count = len([f for f in findings if f.get("severity") == "high"])
    med_count = len([f for f in findings if f.get("severity") == "medium"])

    if not findings:
        print(green("\n  ✅ 未发现已知风险模式"))
    else:
        for f in findings:
            icon = {"high": "🔴", "medium": "🟡", "low": "🔵", "info": "ℹ️"}
            sev = f.get("severity", "info")
            print(f"\n  {icon.get(sev, '•')} {bold(f.get('name', '未知'))}")
            print(f"    {risk_label(sev)}")
            print(f"    {f.get('detail', '')}")

    # 风险评级
    print(f"\n{'─'*60}")
    if high_count > 0:
        overall = red(f"🔴 高风险 — 发现 {high_count} 项高危问题")
        rec = red("❌ 强烈建议不要授权此合约")
    elif med_count > 0:
        overall = yellow(f"🟡 中风险 — 发现 {med_count} 项中风险问题")
        rec = yellow("⚠️ 如确需交互，建议自定义额度并确认合约地址来源可信")
    else:
        overall = green("🟢 低风险 — 未发现明显危险模式")
        rec = green("✅ 可考虑授权，但仍建议使用自定义额度")

    print(f"  总体评估: {overall}")
    print(f"  建议: {rec}")
    if c.get("recommendation"):
        print(f"\n  💡 {c['recommendation']}")

    # 确认提示
    print(f"\n{'─'*60}")
    print(yellow("  ⚠️  此报告仅供参考，AI 不能替你做最终决定"))
    print(yellow("  请自行在 MetaMask 确认交易详情后再签名"))
    print(f"{'─'*60}\n")


def parse_args():
    """简单的参数解析"""
    args = sys.argv[1:]
    if not args or "-h" in args or "--help" in args:
        print("""用法: python3 wallet-approval-checker.py <合约地址> [选项]

选项:
  --network NET    网络 (sepolia / mainnet，默认 sepolia)
  --api-key KEY    Etherscan API Key（或用环境变量 ETHERSCAN_API_KEY）
  --help           显示帮助

示例:
  python3 wallet-approval-checker.py 0x7a250d5630b4cf539739df2c5dacb4c659f2488d
  python3 wallet-approval-checker.py 0x7a250d... --network mainnet --api-key ABC123
""")
        sys.exit(0)

    address = args[0]
    network = "sepolia"
    apikey = ETHERSCAN_API_KEY

    i = 1
    while i < len(args):
        if args[i] == "--network" and i+1 < len(args):
            network = args[i+1].lower()
            i += 2
        elif args[i] == "--api-key" and i+1 < len(args):
            apikey = args[i+1]
            i += 2
        else:
            i += 1

    return address, network, apikey


if __name__ == "__main__":
    address, network, apikey = parse_args()
    check_contract(address, network, apikey)
