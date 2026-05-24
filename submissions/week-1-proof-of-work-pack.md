# Week 1 Proof-of-Work Pack

> 📅 2026-05-19 ~ 2026-05-24
> 👤 B W | AI × Web3 School Cohort 0

---

## 总览

| 维度 | 内容 | 链接 |
|------|------|------|
| 🤖 AI 学习 | 10 张 AI 基础概念卡片 | [查看](daily/2026-05-24.md) |
| ⛓️ Web3 学习 | 12 张 Web3 基础概念卡片 | [查看](daily/2026-05-24-web3-concepts.md) |
| 🔧 Agent 实践 | Learning Agent Setup 记录 | [查看](submissions/learning-agent-setup.md) |
| 🧪 交互学习产物 | AI 概念测验 CLI 工具 | [代码](experiments/concept-quiz.py) |
| 💸 测试网交易 | Sepolia 0.01 ETH 转账 | [记录](submissions/testnet-transaction.md) |
| 📜 智能合约部署 | HelloWeb3 部署到 Sepolia | [记录](submissions/deploy-smart-contract.md) |
| 🆚 账户对比 | EOA / 智能账户 / 多签权限差异 | [对比](submissions/eoa-vs-smart-account-vs-multisig.md) |
| 🔀 交叉流程图 | AI × Web3 最小交叉流程 | [流程图](submissions/ai-web3-cross-flow.md) |
| 🛡️ 受限助手设计 | 钱包授权检查 Agent（CLI + Workflow） | [设计](submissions/restricted-web3-assistant.md) |

---

## 一、AI 学习记录

### 10 张 AI 基础概念卡片

**方式：** 逐概念用自己的话回答 → 与 AI 对话修正 → 归纳成卡片格式

| # | 概念 | 一句话解释 |
|---|------|-----------|
| 1 | LLM | 基于 next token prediction 的文本生成模型，不是查数据库 |
| 2 | Prompt | 给 LLM 的指令，核心在具体性和结构化 |
| 3 | Context Window | 短期记忆窗口，重要内容放头尾（lost in the middle） |
| 4 | Workflow | 预定义多步骤编排，路线固定 |
| 5 | Agent | LLM 自主决策每一步 |
| 6 | Tool Use | 给 LLM一双执行的"手" |
| 7 | AI Coding | 分三层：补全→对话→自主 Agent |
| 8 | Guardrails | 四层护栏让 Agent 安全地强大 |
| 9 | Tracing | 飞行记录仪，不是回退 |
| 10 | Human-in-the-Loop | 责任归属的设计决策 |

📄 [完整卡片（含例子 + 误区）](daily/2026-05-24.md)

### Learning Agent / AI 工具实践记录

**使用工具：** Hermes Agent（macOS 本地运行，Telegram 交互界面，模型：DeepSeek V4 Flash）

**效果：** AI 辅助完成概念整理、代码生成、git 操作、文档编写等。

📄 [完整运行记录](submissions/learning-agent-setup.md)

### AI 交互学习产物

**CLI 概念测验工具：** 10 张卡片 × 4 种出题模式，终端自测。

```bash
python3 experiments/concept-quiz.py
```

📄 [代码](experiments/concept-quiz.py) | [提交说明](submissions/interactive-learning-tool.md)

---

## 二、Web3 实践记录

### 12 张 Web3 基础概念卡片

| # | 概念 | 安全提醒 |
|---|------|---------|
| 1-2 | Account + Address | 地址公开，私钥绝不公开 |
| 3 | Wallet | 钱包存私钥，钱在链上 |
| 4-5 | Seed Phrase + Private Key | 助记词 > 私钥 > 地址（安全层级递减） |
| 6 | Signature | 不可伪造、不可否认、不可篡改 |
| 7 | Transaction | 从广播到确认需要时间 |
| 8 | Gas | Base fee 销毁，Priority fee 给验证者 |
| 9 | Smart Contract | 部署后不可篡改，公开可验证 |
| 10-12 | Testnet + Explorer + EOA/AA/MS | 测试网不花钱，区块浏览器公开可查 |

📄 [完整卡片](daily/2026-05-24-web3-concepts.md)

### 测试网交易

| 字段 | 值 |
|------|-----|
| 网络 | Sepolia |
| 发送地址 | `0x59104Db08d3f0BA5833ab1d8012D88d4780eEa1D` |
| 收款地址 | `0x6Cc9397c3B38739daCbfaA68EaD5F5D77Ba5F455` |
| 金额 | 0.01 ETH |
| 交易 Hash | `0x52aaa753bb05da71dfaddb183ce20bf3dfa94295a25b9b539b51b122527ad670` |
| 区块 | #10911166 |
| Gas | 0.0000527 ETH (2.5 Gwei) |
| 状态 | ✅ Success |

🔗 [Etherscan](https://sepolia.etherscan.io/tx/0x52aaa753bb05da71dfaddb183ce20bf3dfa94295a25b9b539b51b122527ad670)

📄 [提交记录](submissions/testnet-transaction.md)

### 最小智能合约部署

**合约名称：** HelloWeb3
**合约功能：** 存储和修改一个公开的 greeting 字符串

| 操作 | 结果 |
|------|------|
| 部署交易 | `0xcadc76f97b5e0e0ef5e6efe8414b6243b8ef815e08917d591beaccfa15f613ab` |
| 合约地址 | [`0x08029418c8A7242cfA4662933b949c8438e5B20D`](https://sepolia.etherscan.io/address/0x08029418c8A7242cfA4662933b949c8438e5B20D) |
| 读取 greeting() | `"Hello AI x Web3!"` |
| 调用 setGreeting() 交易 | `0xdf0f9dc4c00829ba80be4b59fd07257e1766717667a04017878e9b61a10d66bc` |
| 再次读取 greeting() | `"I deployed my first contract!"` |

📄 [提交记录](submissions/deploy-smart-contract.md)

---

## 三、AI × Web3 交叉

### EOA / 智能账户 / 多签权限差异

六个维度对比 + "哪些操作必须人工确认"。

📄 [对比文档](submissions/eoa-vs-smart-account-vs-multisig.md)

### AI × Web3 最小交叉流程图

🔗 [查看流程图](https://excalidraw.com/#json=g-zGMbIUKrUEGVeRBFZeQ,qp7R1ibo42y9Lbi6KdEYoA)

流程：**用户输入 → AI 解析意图 → Tool Use 构建操作 → 人确认？→ 链上交易 → 结果返回**

📄 [说明文档](submissions/ai-web3-cross-flow.md)

### 受限 Web3 助手设计

**钱包授权检查 Agent：** CLI 工具，输入合约地址后 AI 自动：
1. 查询合约是否开源 + 部署时间 + 交互次数
2. 扫描源码中的危险函数（reentrancy、delegatecall、selfdestruct 等）
3. 计算你的代币余额并建议授权额度（余额 + 10%，而非无限额度）
4. 生成风险评级报告

🔗 [Workflow 图](https://excalidraw.com/#json=ooAcyMCds8pPE2XMAnXFn,sWkmF1LXo_9X3Q6r_LqjoA)

📄 [代码](experiments/wallet-approval-checker.py) | [设计文档](submissions/restricted-web3-assistant.md)

```bash
# 本地运行
cd experiments/
python3 wallet-approval-checker.py <合约地址>
```

---

## 四、本周遇到的问题与人工修正记录

### 问题 1：MetaMask 测试网余额不显示 (2026-05-24)

**场景：** PoW 水龙头（pk910.de）挖矿完成后，MetaMask 显示 ETH 余额为 0。

**根因：** MetaMask 默认在以太坊主网，测试网络需要在设置中手动开启。

**修正：** 设置 → 高级 → 显示测试网络 → 切换到 Sepolia → 余额正常显示。

**教训：** 任何测试网操作前先确认 MetaMask 网络已切换。

---

### 问题 2：Alchemy Faucet 拒绝领币 (2026-05-24)

**场景：** 尝试用 Alchemy Sepolia Faucet 领测试币。

**根因：** Alchemy 要求主网地址至少有 0.001 ETH 才能使用其 faucet。

**修正：** 更换为 PoW 水龙头（pk910.de），无需登录和主网余额。

**教训：** 测试网水龙头各有门槛，PoW 水龙头是最低门槛的选择。

---

### 问题 3：概念卡片整理 — Workflow vs Agent 的区别 (2026-05-24)

**场景：** 在整理 AI 概念卡片时，最初将 Workflow 理解为"使用 AI 的工作场景"。

**修正：** 与 AI 逐概念对话后认识到 — Workflow 是固定路径的多步骤编排（地铁图），Agent 是 LLM 自主决策（打车），关键区别在**谁做路径决策**。

**教训：** 用自己的话先答、再让 AI 纠正的方式，比直接看定义更有记忆深度。

---

## 五、GitHub 仓库

🔗 https://github.com/BBBINGW/ai-web3-school-cohort-0

```
.
├── README.md
├── profile.md
├── learning-plan.md
├── daily/                      # 每日学习笔记
│   ├── 2026-05-19.md           # Day 2: LLM
│   ├── 2026-05-20.md           # Day 3: Prompt
│   ├── 2026-05-23.md           # Day 4: 知识疑惑整理
│   ├── 2026-05-24.md           # Day 5: AI 概念卡片
│   └── 2026-05-24-web3-concepts.md  # Web3 概念卡片
├── submissions/                # 任务提交
│   ├── learning-agent-setup.md
│   ├── interactive-learning-tool.md
│   ├── testnet-transaction.md
│   ├── deploy-smart-contract.md
│   ├── eoa-vs-smart-account-vs-multisig.md
│   ├── ai-web3-cross-flow.md
│   └── restricted-web3-assistant.md
├── experiments/                # 实验代码与图表
│   ├── concept-quiz.py
│   ├── testnet-transaction.md
│   ├── ai-web3-cross-flow.excalidraw
│   ├── wallet-approval-agent.excalidraw
│   └── wallet-approval-checker.py
└── templates/
```

---

## 隐私声明

本 Pack **不包含**：
- ❌ 私钥 / 助记词
- ❌ API Key / Token
- ❌ .env 文件
- ❌ 真实资产相关信息
- ❌ 个人不可公开的联系方式
