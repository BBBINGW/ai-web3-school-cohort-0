# Learning Agent Setup — 配置与运行记录

> 提交时间：2026-05-24
> 提交者：B W

---

## 1. 选择的 Agent / AI 工具

**Hermes Agent**

- 运行环境：macOS 13.7.8（本地运行）
- 交互界面：Telegram（DM 对话）
- 模型：DeepSeek V4 Flash（通过自定义 provider）
- 仓库：https://github.com/NousResearch/hermes-agent

**工具能力**：支持终端命令执行、文件读写、Git 操作、网页搜索、内存持久化、session 搜索、技能管理、任务编排（cron job）、多子代理并行等。

---

## 2. Agent 协助完成的学习任务

**任务**：整理 AI 基础概念卡片
**要求**：用自己的话整理至少 6 个 AI 基础概念，每个包含一句话解释、一个具体例子、一个常见误区

**完成的概念（10 个）**：

| # | 概念 | 难度 |
|---|------|------|
| 1 | LLM（大语言模型） | ⭐ |
| 2 | Prompt（提示词） | ⭐ |
| 3 | Context Window（上下文窗口） | ⭐ |
| 4 | Workflow（工作流） | ⭐⭐ |
| 5 | Agent（智能体） | ⭐⭐ |
| 6 | Tool Use（工具调用） | ⭐⭐ |
| 7 | AI Coding（AI 编程） | ⭐⭐ |
| 8 | Guardrails（护栏） | ⭐⭐⭐ |
| 9 | Tracing（追踪） | ⭐⭐⭐ |
| 10 | Human-in-the-Loop（人在环） | ⭐⭐⭐ |

**输出文件**：[daily/2026-05-24.md](https://github.com/BBBINGW/ai-web3-school-cohort-0/blob/main/daily/2026-05-24.md)

---

## 3. 关键 prompt 或配置说明

### 交互模式（核心设计）

不是让 Agent 直接输出概念定义，而是采用 **Socratic 对话法**：

```
Agent 逐个提问 → 学生用自己的话回答 → Agent 核对并补充 → 达成共识后归纳成卡片
```

### 关键 prompt
```
"请作为我的 AI × Web3 School Learning Agent，先阅读启动 Prompt：https://aiweb3.school/learning-agent.zh.txt ，并结合 Handbook：https://aiweb3.school/zh/handbook/ ，帮我初始化个人学习计划、GitHub 学习仓库、每日打卡草稿和 Handbook feedback 流程。"
```

这是训练营官方提供的 **Learning Agent 启动 Prompt**，完整定义了 Agent 的角色和初始化流程，包括：
1. 阅读启动 Prompt 文件 + Handbook
2. 收集学员画像
3. 创建 GitHub 学习仓库并初始化目录结构
4. 编写个性化学习计划
5. 生成每日打卡草稿
6. 建立 Handbook feedback 流程

在此基础上，**具体任务的执行使用了 Socratic 对话法** — 每完成一个概念，Agent 先提问让用户用自己的话回答，再核对修正，最后归纳成卡:

### 配置说明

Hermes Agent 配置文件（`~/.hermes/config.yaml`）中与本任务相关的关键配置：

```yaml
# 模型配置
model: deepseek-v4-flash
provider: custom

# 启用的工具集
tools:
  - terminal      # 执行 shell 命令（git push 等）
  - file          # 读写文件（创建概念卡片）
  - web           # 访问 GitHub / 文档
  - memory        # 持久化用户偏好
  - skills        # 加载训练营技能
```

---

## 4. 一次成功输出记录

**任务终点**：10 张概念卡片整理完毕 → 写入仓库 → 推送到 GitHub

**执行过程摘要**：

```
① Agent 读取任务要求（整理 ≥6 个 AI 概念卡片）
② 按顺序逐概念提问：
    "用你自己的话说说 LLM 是什么？"
    用户回答 → Agent 补充修正 → 下一概念
    ...
    共 10 轮对话完成
③ Agent 汇总所有修正内容，生成结构化卡片（MD 格式）
④ 写入 /Users/admin/Downloads/AgentForweb3/AI-基础概念卡片.md
⑤ 同时写入 GitHub 仓库 /Users/admin/Downloads/web3 repo/daily/2026-05-24.md
⑥ git add → git commit → git push
```

**最终产出链接**：
- GitHub 文件：https://github.com/BBBINGW/ai-web3-school-cohort-0/blob/main/daily/2026-05-24.md
- 仓库首页：https://github.com/BBBINGW/ai-web3-school-cohort-0

**验证**：页面可正常公开访问 ✅

---

## 5. 一次人工复核、修正或拒绝 Agent 建议的记录

### 场景：概念理解修正 — Workflow（工作流）

**用户的原始理解（第 4 个概念）：**

> “顾名思义，工作流。我觉得就是在你工作的时候，使用 AI 的工作场景、如何使用。”

**Agent 的初始回应**（字面义理解）：
> 你的理解是字面意思。但在 AI 工程语境下，workflow 有更具体的技术含义...

**人工复核后用户补充回答**（自己思考后）：

> “agent 是你交给他一个任务，他完全自己帮你跑。workflow 是要自己有交互的。”

**修正结果**：
Agent 基于用户的第二次回答做了精准的概念区分：

| | Workflow | Agent |
|---|---|---|
| 路径 | 固定/预定义 | 动态/LLM 自主决策 |
| 灵活性 | 低 | 高 |
| 比喻 | 地铁线路图 | 打车 |

**最终卡片中的表述**（经过用户认可）：Workflow = 预定义的多步骤编排，Agent = LLM 自主决策。

### 场景：概念边界精确化 — Tracing（追踪）

**用户的理解**：
> "记录每一步做什么？到时候报错可以退回上一步这样？"

**修正**：Agent 指出 tracing 和 rollback 是两个不同概念。Tracing = 黑匣子记录，rollback = 回退机制。用户认可这个区分，最终卡片明确标注了这点。

---

## 隐私安全说明

本提交 **不包含**：
- ❌ API Key / Token
- ❌ 私钥 / 助记词
- ❌ .env 文件
- ❌ 个人隐私信息

仅包含学习任务的概念理解与配置记录。
