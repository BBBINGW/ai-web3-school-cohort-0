# AI × Web3 最小交叉流程图

> 提交时间：2026-05-24
> 工具：Excalidraw（手绘风格流程图）

---

## 流程图链接

🔗 **查看与编辑：** https://excalidraw.com/#json=g-zGMbIUKrUEGVeRBFZeQ,qp7R1ibo42y9Lbi6KdEYoA

（打开后可以拖拽、编辑、导出截图）

## GitHub 文件

🔗 https://github.com/BBBINGW/ai-web3-school-cohort-0/blob/main/experiments/ai-web3-cross-flow.excalidraw

---

## 流程图说明

本图展示了从**用户意图到链上执行**的最小交叉路径，包含三个域：

### 🟦 AI 域（左侧）
| 节点 | 说明 |
|------|------|
| **用户输入** | 用自然语言描述任务（如"发 0.01 ETH 给 Bob"） |
| **AI Agent (LLM)** | 解析用户意图，决定下一步操作 |

### 🟨 交叉区（中间 — AI × Web3 的交汇点）
| 节点 | 说明 |
|------|------|
| **Tool Use** | AI 调用工具查询链上数据、构建交易参数 |
| **人在环确认** | 🔴 用户确认后交易才进入链上执行（HITL 安全机制） |

### 🟩 Web3 域（右侧）
| 节点 | 说明 |
|------|------|
| **链上交易** | 交易广播到网络，矿工/验证者打包确认 |
| **结果返回** | 返回 Tx Hash 和状态变更，AI 解析后反馈给用户 |

### 整体流程

```
用户输入 → AI 解析意图 → Tool Use 构建操作 → 人确认？→ 链上交易 → 结果返回
                                       ↑                    ↑
                                  AI 与 Web3 交叉点      Web3 域执行
```

---

## 你今天对应的实操经验

| 流程图节点 | 你今天做的对应操作 |
|-----------|------------------|
| 用户输入 | "帮我发 0.01 SEP ETH 到 0x6Cc9...5F455" |
| AI Agent | Hermes Agent（我）解析你的意图 |
| Tool Use | 指导你在 MetaMask 上操作 |
| 人在环 | 你在 MetaMask 弹窗里点"确认" |
| 链上交易 | `0x52aa...670` 被打包在 block #10911166 |
| 结果返回 | 我告诉你交易状态 Success |
