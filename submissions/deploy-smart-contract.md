# 部署最小智能合约 — 提交记录

> 提交时间：2026-05-24 17:55
> 工具：Remix IDE + MetaMask
> 网络：Sepolia

---

## 合约代码

**文件：** `HelloWeb3.sol`

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract HelloWeb3 {
    string public greeting;

    constructor() {
        greeting = "Hello AI x Web3!";
    }

    function setGreeting(string memory _newGreeting) public {
        greeting = _newGreeting;
    }
}
```

## 部署信息

| 字段 | 值 |
|------|-----|
| 合约地址 | `0x08029418c8A7242cfA4662933b949c8438e5B20D` |
| 交易 Hash | `0xcadc76f97b5e0e0ef5e6efe8414b6243b8ef815e08917d591beaccfa15f613ab` |
| Block | #10911205 |
| Gas 消耗 | 434,117 |
| 状态 | ✅ Success |

## 功能验证

| 步骤 | 操作 | 输入 | 输出/交易 Hash |
|------|------|------|---------------|
| 1 | 读取 `greeting()` | — | `"Hello AI x Web3!"` |
| 2 | 调用 `setGreeting()` | `"I deployed my first contract!"` | [`0xdf0f...6bc`](https://sepolia.etherscan.io/tx/0xdf0f9dc4c00829ba80be4b59fd07257e1766717667a04017878e9b61a10d66bc) |
| 3 | 再次读取 `greeting()` | — | `"I deployed my first contract!"` |

## 区块浏览器链接

- **合约地址：** https://sepolia.etherscan.io/address/0x08029418c8A7242cfA4662933b949c8438e5B20D
- **部署交易：** https://sepolia.etherscan.io/tx/0xcadc76f97b5e0e0ef5e6efe8414b6243b8ef815e08917d591beaccfa15f613ab
- **setGreeting 交易：** https://sepolia.etherscan.io/tx/0xdf0f9dc4c00829ba80be4b59fd07257e1766717667a04017878e9b61a10d66bc

## 说明

通过 Remix IDE 编写了一个最简 Solidity 合约（HelloWeb3），使用 MetaMask 连接 Sepolia 测试网部署。合约包含一个公开字符串状态变量 `greeting`、一个构造函数（部署时设初始值）和一个修改状态的函数 `setGreeting`。部署后分别测试了读和写操作，均成功执行。
