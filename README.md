# AI × Web3 School — Cohort 0

Personal learning journal and proof-of-work for [AI × Web3 School](https://aiweb3.school/).

> Built by an open-source learning platform from [LXDAO](https://lxdao.io/) & [ETHPanda](https://ethpanda.org/).

---

## 📘 Week 1 学习总结 (2026-05-19 ~ 2026-05-24)

### 一个重新理解的 AI 概念：LLM ≠ 搜索引擎

以前觉得 LLM 就像可交互的百度百科，能回答各种问题。这周才真正理解：**LLM 是 next token prediction 模型**，它不是在"查知识"而是在"猜下一个词"。这解释了为什么 LLM 会 hallucinate（产生幻觉）— 它不是撒谎，而是遇到了训练数据中没有的知识点，只能编一个"看起来合理"的答案。

**实践启示：** 关键输出必须链上验证（如 Tx Hash 查区块浏览器），不能轻信 AI 的解读。

### 一个重新理解的 Web3 概念：钱包里不存钱

"钱包里存的是代币" — 这我原来就是这么以为的。这周做了测试网交易后彻底理解了：**MetaMask 存的是私钥，代币存在以太坊的账本上**。换了电脑导入助记词还能看到余额，因为链没变，钱没动。

**实践启示：** 助记词 > 私钥 > 地址（安全层级递减），助记词丢了=整个钱包没了。

### 一个 AI × Web3 交叉问题：Agent 能不能自动发交易？

不能。这周设计的 **钱包授权检查 Agent** 明确了边界：AI 可以查链上数据、分析合约风险、建议授权额度，但**签名这一步必须人工在 MetaMask 弹窗确认**。这是架构设计，不是技术限制 — HITL（人在环）把最终决策权留给用户。

**交叉点：** AI 负责"理解+建议"，Web3（钱包签名）负责"授权+执行"，交叉在 Tool Use → 人确认 → 链上执行这个流程中。

### 本周 Proof-of-Work

| 项目 | 链接 |
|------|------|
| 🔗 Week 1 完整 Pack | [submissions/week-1-proof-of-work-pack.md](submissions/week-1-proof-of-work-pack.md) |
| 🧠 AI 基础概念卡片 | [daily/2026-05-24.md](daily/2026-05-24.md) |
| 🤖 Learning Agent Setup | [submissions/learning-agent-setup.md](submissions/learning-agent-setup.md) |
| 🎮 AI 可交互产物（概念测验 CLI） | [experiments/concept-quiz.py](experiments/concept-quiz.py) |
| ⛓️ Web3 基础概念卡片 | [daily/2026-05-24-web3-concepts.md](daily/2026-05-24-web3-concepts.md) |
| 💸 测试网交易 | [submissions/testnet-transaction.md](submissions/testnet-transaction.md) |
| 📜 智能合约（HelloWeb3） | [submissions/deploy-smart-contract.md](submissions/deploy-smart-contract.md) |
| 🆚 EOA / 智能账户 / 多签对比 | [submissions/eoa-vs-smart-account-vs-multisig.md](submissions/eoa-vs-smart-account-vs-multisig.md) |
| 🔀 AI × Web3 交叉流程图 | [submissions/ai-web3-cross-flow.md](submissions/ai-web3-cross-flow.md) |
| 🛡️ 受限 Web3 助手设计 | [submissions/restricted-web3-assistant.md](submissions/restricted-web3-assistant.md) |

### 一个还没解决的问题：AI 如何验证链上结果的可信度？

这周我学会了"用区块浏览器验证交易"，但验证**仍然需要人工操作** — 复制 Tx Hash → 打开 Etherscan → 检查状态。理想情况下，Agent 应该能自动做这件事并返回可信的结果。

但问题是：**Agent 调用 Etherscan API 拿到的数据，和我在浏览器里看到的数据，是同样的数据源**。如果 Agent 本身被欺骗（比如调了钓鱼 API），那自动验证就失去了意义。下一周我想探索：有没有办法让 Agent 的链上验证也能被用户独立验证（比如签名验证、Merkle proof）？

---

## Quick Links

| Resource | URL |
|----------|-----|
| Handbook | https://aiweb3.school/zh/handbook/ |
| Bootcamp (WCB) | https://web3career.build/zh/programs/AI-Web3-School |
| Learning Page | https://web3career.build/zh/programs/AI-Web3-School#tab=learning |
| GitHub Repo (School) | https://github.com/lxdao-official/aiweb3school |
| Telegram Community | https://t.me/aiweb3school |

## ⚠️ Privacy Notice

This repository is **public**. Do NOT commit:
- API keys, tokens, or private keys
- Seed phrases or wallet private keys
- Personal contact info not intended for public sharing
- Internal meeting links
- Anyone else's personal data

## Directory Structure

```text
.
├── README.md                   # This file
├── profile.md                  # Personal learning profile
├── learning-plan.md            # Learning roadmap & progress
├── daily/                      # Daily learning notes (YYYY-MM-DD.md)
├── tasks/                      # Task breakdowns & checklists
├── experiments/                # Hands-on experiments & code
├── handbook-feedback/          # Feedback for the Handbook (bugs, suggestions)
├── hackathon/                  # Hackathon project materials
├── submissions/                # Course / bootcamp submissions
└── templates/                  # Reusable note templates
    ├── daily-note.md
    └── task-note.md
```

## Language

This repo uses **bilingual** (中文 + English) notes to serve both personal learning and open-source collaboration.
