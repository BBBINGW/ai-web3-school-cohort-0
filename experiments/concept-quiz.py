#!/usr/bin/env python3
"""AI 概念交互测验 — CLI 小工具
从今天整理的 10 张 AI 基础概念卡片中随机出题，自测你的理解。
"""

import random
import sys

# ---------- 概念卡片知识库（AI 辅助整理 + 人工复核修正）----------
# 每张卡片：概念名、一句话解释、例子、常见误区
# AI 辅助生成了初版内容，人工逐概念对话修正后定稿
CONCEPTS = [
    {
        "name": "LLM",
        "full": "LLM（Large Language Model）",
        "desc": "基于海量文本训练的 next token prediction 模型，能生成各类文本内容而非'查数据库'。",
        "example": "问'帮我解释零知识证明'，LLM 生成看起来合理的解释 — 但它不是从知识库检索，而是根据训练数据中该词的上下文模式'猜'出最可能的回答。",
        "misconception": "LLM 不等于搜索引擎。遇到训练数据中没有的知识点会 hallucinate 编造内容。关键输出必须自行验证。",
    },
    {
        "name": "Prompt",
        "full": "Prompt（提示词）",
        "desc": "给 LLM 的指令/输入，质量决定输出质量 — 核心在 specificity（具体性）和 structure（结构化）。",
        "example": "❌ '帮我写段代码' ✅ '用 Python 写一个函数，输入 URL 返回页面 title，报错返回 None，写 docstring'",
        "misconception": "以为 prompt 只是一段'话'。实际上有效 prompt engineering 包含三大技巧：Role、Few-shot、Chain-of-Thought。",
    },
    {
        "name": "Context Window",
        "full": "Context Window（上下文窗口）",
        "desc": "LLM 一次能'看到'的最大文本量（输入+输出），是短期记忆，对话一关就清空。",
        "example": "聊了 1 小时合约漏洞后问'前面那个合约地址是多少'— context window 满了被挤掉的话，LLM 会忘记或瞎编。",
        "misconception": "❌ 'Context window 越大越好' ✅ 研究发现 LLM 对窗口中间内容注意力下降（'lost in the middle'），重要信息放头尾。",
    },
    {
        "name": "Workflow",
        "full": "Workflow（工作流）",
        "desc": "多步骤编排的预定义自动化流程 — 像地铁线路图，站点固定。",
        "example": "步骤1: LLM 判断用户意图 → 步骤2: 如果是翻译则调用翻译 API → 步骤3: 格式化输出。每一步写死，不会自己改路线。",
        "misconception": "❌ 'Workflow = 让 AI 做事情' ✅ 技术语境下特指多步骤编排+数据传递+条件分支。简单一问一答不算 workflow。",
    },
    {
        "name": "Agent",
        "full": "Agent（智能体）",
        "desc": "LLM 自主决定下一步做什么来达成目标 — 像打车，你给目的地，司机自己选路线。",
        "example": "'帮我找到今天以太坊的大额转账并整理成表'→ Agent 自主：查 API → 数据太多 → 缩小范围 → 再查 → 生成表格 → 保存。",
        "misconception": "❌ 'Agent = 高级 Workflow' ✅ 关键区别在谁做决策：Workflow 路径固定（菜谱），Agent 动态决策（实习生）。",
    },
    {
        "name": "Tool Use",
        "full": "Tool Use（工具调用）",
        "desc": "让'只说不做'的 LLM 拥有'手' — 通过调用外部工具（终端、文件系统、API）实际执行操作。",
        "example": "'把测试覆盖率提到 80%'→ Agent 通过 read_file 读代码 → terminal 跑测试 → 实际修改文件 → 再次运行验证。",
        "misconception": "Tool Use 赋予 Agent 真实执行能力，但也可能误用（无限循环、误改文件）。必须配合权限控制和调用次数限制使用。",
    },
    {
        "name": "AI Coding",
        "full": "AI Coding（AI 编程）",
        "desc": "AI 辅助或自主完成补充/生成/测试/调试代码，分三个层次：补全、对话生成、自主 Agent。",
        "example": "🟢 补全：写函数名后 AI 猜下几句 🟡 对话生成：描述需求 AI 给出整段代码 🔴 自主 Agent：给 issue 自己改项目+跑测试+提 PR",
        "misconception": "❌ 'AI 写的代码可直接上线' ✅ AI 可能推荐过时 API、引入安全漏洞。AI 是 copilot，不是 autopilot。",
    },
    {
        "name": "Guardrails",
        "full": "Guardrails（护栏）",
        "desc": "在 AI 自由度和安全性之间设多层保护机制，防止失控或有害输出。",
        "example": "四层护栏：🛡️ 安全（不让生成恶意内容）🔐 权限（只能读不能删）📐 格式（必须输出 JSON）🔄 行为（最大调用限制）",
        "misconception": "❌ 'Guardrails = 限制 AI，越少越厉害' ✅ 没有 guardrails 的 Agent 像没刹车跑车。Guardrails 决定了它能跑多远而不出事。",
    },
    {
        "name": "Tracing",
        "full": "Tracing（追踪）",
        "desc": "像飞行记录仪一样完整记录 Agent 每一步的输入、输出、耗时、token 消耗 — 可回放、可审计。",
        "example": "Agent 跑 20 步后输出错误结果。Tracing 回放发现第 7 步传错参数 → 第 8 步基于错误数据推理 → 全跑偏。没有 tracing 只能重跑一次。",
        "misconception": "❌ 'Tracing = 出错退回上一步' ✅ Tracing = 记录，rollback = 回退，是不同机制。Tracing 价值在调试、成本分析、性能优化、审计合规。",
    },
    {
        "name": "Human-in-the-Loop",
        "full": "Human-in-the-Loop（人在环）",
        "desc": "关键决策点需要人审批 — 最终责任归属的设计决策，不是 AI 能力的妥协。",
        "example": "Agent 完成合约交互分析 → 生成操作建议 → 停下来等你审查 → 你批准 → Agent 才执行链上操作。不经你确认，它不动钱。",
        "misconception": "❌ 'HITL 是 AI 不够强的妥协，强了就不需要' ✅ 涉及资产转移等高风险的场景，即使 AI 99.9% 准确，最终决策权需要留给人类。",
    },
]


def pick_mode():
    """选择出题模式"""
    print("\n🎯 选一个模式：")
    print("  1. 看概念名 → 回忆一句话解释")
    print("  2. 看一句话解释 → 猜是哪个概念")
    print("  3. 看例子 → 猜是哪个概念")
    print("  4. 全模式随机")
    while True:
        choice = input("👉 输入 1-4: ").strip()
        if choice in ("1", "2", "3", "4"):
            return choice
        print("  ⚠️ 请输入 1、2、3 或 4\n")


def run_one_round(card, mode):
    """出一题，返回对错"""
    if mode == "1":
        # 看概念名 → 回忆描述
        print(f"\n📌 概念：{card['full']}")
        print("你的任务：回忆并输入你理解的'一句话解释'")
        input("⏎ 按 Enter 后输入你的答案...")
        user_ans = input("✏️ 你的解释: ").strip()
        print(f"\n📖 卡片的解释:")
        print(f"   {card['desc']}")
        print(f"\n📘 例子: {card['example']}")

    elif mode == "2":
        # 看描述 → 猜概念名
        print(f"\n📖 一句话解释: {card['desc']}")
        user_ans = input("✏️ 这是哪个概念？: ").strip()
        print(f"\n✅ 正确答案: {card['full']}")
        print(f"📘 例子: {card['example']}")

    elif mode == "3":
        # 看例子 → 猜概念
        print(f"\n📘 例子: {card['example']}")
        user_ans = input("✏️ 这是哪个概念的例子？: ").strip()
        print(f"\n✅ 正确答案: {card['full']}")
        print(f"📖 一句话解释: {card['desc']}")

    else:
        # 随机模式
        return run_one_round(card, random.choice(["1", "2", "3"]))

    print(f"\n⚠️ 常见误区: {card['misconception']}")

    # 用户自评
    while True:
        correct = input("\n🤔 你答对了吗？(y/n): ").strip().lower()
        if correct in ("y", "n"):
            return correct == "y"
        print("  请输入 y 或 n")


def main():
    print("=" * 56)
    print("  🧠  AI 基础概念交互测验")
    print("  基于今天整理的 10 张概念卡片")
    print("  来源：daily/2026-05-24.md")
    print("=" * 56)

    mode = pick_mode()

    # 打乱概念顺序
    pool = CONCEPTS.copy()
    random.shuffle(pool)

    score = 0
    total = 0

    for card in pool:
        total += 1
        print(f"\n{'─' * 56}")
        print(f"  第 {total} / {len(pool)} 题")
        print(f"{'─' * 56}")
        if run_one_round(card, mode):
            score += 1
            print("  ✅ 好！")
        else:
            print("  💡 下次再看一遍就行")

        if total < len(pool):
            again = input("\n⏩ 继续下一题？(Enter=继续, q=退出): ").strip()
            if again.lower() == "q":
                break

    # 成绩总结
    print(f"\n{'=' * 56}")
    print(f"  📊 测验完成！{score}/{total} 题正确")
    if total > 0:
        pct = score / total * 100
        print(f"  正确率: {pct:.0f}%")
        if pct >= 80:
            print("  🎉 掌握得很好！可以去教别人了")
        elif pct >= 50:
            print("  👍 基础不错，再复习几遍更稳")
        else:
            print("  📚 多练几次，概念会越来越清晰")
    print(f"{'=' * 56}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 下次继续！")
        sys.exit(0)
