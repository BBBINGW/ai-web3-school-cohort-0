# Handbook Feedback — 2026-05-19 — LLM × Cryptography Connections

## Source Page

https://aiweb3.school/zh/handbook/ai/llm/

## Type

- [ ] Typo / grammar
- [ ] Unclear explanation
- [ ] Outdated content
- [x] Missing concept
- [x] Structure suggestion
- [ ] Other:

## Issue Description

The LLM chapter is very well written, but I noticed it doesn't explicitly address how LLM's **probabilistic output model** interfaces with **cryptographic trust assumptions** — which is exactly the AI×Web3 bridge problem. Specifically:

1. The chapter says "越靠近真实动作，越需要外部数据、确定性规则和人工或系统校验" — but doesn't discuss whether cryptographic primitives (ZK proofs, signatures, attestations) can formally verify LLM outputs or at least harden the verification layer.

2. The connection between "hallucination" and "Byzantine fault tolerance" is not made, though they are conceptually isomorphic: both are about untrusted participants producing plausible but wrong outputs.

3. The "minimal practice" (transaction explainer) is great, but lacks a security audit component that a cryptography/security reader would naturally expect.

## Suggestion

Consider adding a **"Cryptographic Perspective" callout box** or cross-reference section that maps LLM concepts to cryptographic equivalents:

| LLM Concept | Crypto Parallel | Why It Matters |
|-------------|-----------------|----------------|
| Hallucination | Byzantine fault | Both require verification before trust |
| Context window | Block calldata | Both have bounded sizes, need efficient encoding |
| Embedding similarity | Probabilistic ≠ proof | Both require alternative verification paths |
| Model output | Prover's claim | Needs a verifier to attest |

This would be especially valuable for readers with cryptography/security backgrounds (there are many in this community!) and would make the Handbook stand out as uniquely positioned at the AI×Web3 intersection.

For the minimal practice exercise, consider adding a follow-up: "How would you cryptographically attest that the LLM's interpretation of a transaction was bounded to only using on-chain data, without extra model inference?"

## Source Context

- Your background: Cryptography PhD candidate / Cybersecurity
- Your interpretation when reading: I kept noticing parallels to cryptographic verification that the chapter doesn't explore
- What you expected vs. what you found: Expected at least a footnote about cryptographic verification of LLM outputs. Found none.
