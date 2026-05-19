# Learning Plan — AI × Web3 School Cohort 0

> Updated: 2026-05-19
> Daily commitment: 2–2.5 hours
> Output: Bilingual (中文 + English)

---

## Overview

Based on the [Handbook](https://aiweb3.school/zh/handbook/) structure, this plan is divided into four phases. Your **cryptography and cybersecurity PhD background** is a unique advantage — you'll bring rigorous security thinking to the AI×Web3 intersection that most learners lack.

---

## Phase 1: AI Basics ⏱ ~1 week

Core question: *What can models do, and what can't they do?*

| Day | Topic | Handbook Link | Est. Time |
|-----|-------|---------------|-----------|
| 1–2 | **LLM** — capabilities, limitations, tokenization | [/zh/handbook/ai/llm/](https://aiweb3.school/zh/handbook/ai/llm/) | 2h |
| 3 | **Prompt** — structure, system/user prompts, formatting | [/zh/handbook/ai/prompt/](https://aiweb3.school/zh/handbook/ai/prompt/) | 2h |
| 4 | **Context** — window, retrieval, grounding | [/zh/handbook/ai/context/](https://aiweb3.school/zh/handbook/ai/context/) | 2h |
| 5 | **Agent** — from Q&A to multi-step execution | [/zh/handbook/ai/agent/](https://aiweb3.school/zh/handbook/ai/agent/) | 2.5h |

**Milestone**: Write a daily note + check-in draft summarizing your mental model of how LLMs work.

---

## Phase 2: Web3 Basics ⏱ ~1 week

Core question: *What is a blockchain, and how does it change trust assumptions?*

Your cryptography background means you can move faster here — focus on **practical dev stack vs. theoretical crypto**.

| Day | Topic | Handbook Link | Est. Time |
|-----|-------|---------------|-----------|
| 6 | **Network** — blocks, consensus, L2, RPC | [/zh/handbook/web3/network/](https://aiweb3.school/zh/handbook/web3/network/) | 2h |
| 7 | **Cryptography** (review) — hash, key pair, signature in Web3 context | [/zh/handbook/web3/cryptography/](https://aiweb3.school/zh/handbook/web3/cryptography/) | 1.5h |
| — | **Wallet** — identity, signing, key management | [/zh/handbook/web3/wallet/](https://aiweb3.school/zh/handbook/web3/wallet/) | 2h |
| 8 | **Smart Contract** — deploy, call, state, permission | [/zh/handbook/web3/smart-contract/](https://aiweb3.school/zh/handbook/web3/smart-contract/) | 2.5h |
| 9 | **Account Abstraction** — Smart Account, why it matters for Agents | [/zh/handbook/web3/account-abstraction/](https://aiweb3.school/zh/handbook/web3/account-abstraction/) | 2h |
| 10 | **Security** — contract risks, permission isolation, monitoring | [/zh/handbook/web3/security/](https://aiweb3.school/zh/handbook/web3/security/) | 2h |

**Milestone**: Write a daily note comparing classical cryptography assumptions with blockchain security models. Your expertise here is your superpower — lean into it.

---

## Phase 3: AI × Web3 Bridge ⏱ ~1.5 weeks

Core question: *How do AI Agents interact with on-chain state, permissions, and payments?*

| Day | Topic | Handbook Link | Est. Time |
|-----|-------|---------------|-----------|
| 11 | **Chain-aware Context** — on-chain state → agent context | [/zh/handbook/bridge/chain-aware-context/](https://aiweb3.school/zh/handbook/bridge/chain-aware-context/) | 2h |
| 12 | **Web3 Tool Use** — RPC, wallet, contract tools | [/zh/handbook/bridge/web3-tool-use/](https://aiweb3.school/zh/handbook/bridge/web3-tool-use/) | 2.5h |
| 13 | **Agent Workflow** — automation vs. human-in-the-loop | [/zh/handbook/bridge/agent-workflow/](https://aiweb3.school/zh/handbook/bridge/agent-workflow/) | 2h |
| 14 | **Agent Wallet** — permissions, session keys, revocation | [/zh/handbook/bridge/agent-wallet/](https://aiweb3.school/zh/handbook/bridge/agent-wallet/) | 2.5h |
| 15 | **AI Security** — prompt injection, tool abuse, audit logs | [/zh/handbook/bridge/ai-security/](https://aiweb3.school/zh/handbook/bridge/ai-security/) | 2.5h |
| 16 | **Verifiable AI** — attestations, execution proofs | [/zh/handbook/bridge/verifiable-ai/](https://aiweb3.school/zh/handbook/bridge/verifiable-ai/) | 2h |
| 17 | **Agent Identity & Trust** — identity, reputation | [/zh/handbook/bridge/agent-identity/](https://aiweb3.school/zh/handbook/bridge/agent-identity/) + [/bridge/agent-trust-and-reputation/](https://aiweb3.school/zh/handbook/bridge/agent-trust-and-reputation/) | 2h |

**Milestone**: Sketch a mini idea combining an AI Agent with a Web3 component. Save it to `experiments/`.

---

## Phase 4: Explore Tracks ⏱ Ongoing

Core question: *What can I build?*

Pick one track to prototype:

| Track | Description | Handbook Link |
|-------|-------------|---------------|
| 🛒 Agentic Commerce | Agent discovers services, negotiates, pays | [/zh/handbook/tracks/agentic-commerce/](https://aiweb3.school/zh/handbook/tracks/agentic-commerce/) |
| 🔑 Wallet / Permission | Session keys, policies, guards | [/zh/handbook/tracks/wallet-permission/](https://aiweb3.school/zh/handbook/tracks/wallet-permission/) |
| 🛡️ AI Security | Attack surface, audit, alerts | [/zh/handbook/tracks/ai-security/](https://aiweb3.school/zh/handbook/tracks/ai-security/) |
| 🏛️ Governance | AI-assisted DAO tools | [/zh/handbook/tracks/governance/](https://aiweb3.school/zh/handbook/tracks/governance/) |
| 🔧 Dev Tooling | Contract understanding, testing, docs | [/zh/handbook/tracks/dev-tooling/](https://aiweb3.school/zh/handbook/tracks/dev-tooling/) |

---

## Daily Workflow

```
Morning (optional):   Review what you learned yesterday
Main session (2h):    Read Handbook → take notes → write daily note
Evening (10min):      Generate check-in draft → submit via WCB → save link
```

## Handbook Feedback

Whenever you find:
- A typo or unclear explanation → file in `handbook-feedback/`
- A concept that should be expanded → suggest additions
- A security perspective that Handbook misses ← **this is where your PhD expertise is most valuable**

---

## Progress Tracker

- [ ] Phase 1: AI Basics
- [ ] Phase 2: Web3 Basics
- [ ] Phase 3: AI × Web3 Bridge
- [ ] Phase 4: Track deep-dive
- [ ] Hackathon project (if applicable)
