---
tags: [CCNP, glossary, qos, networking]
aliases: ["LLQ", "Low Latency Queuing", "Priority Queue", "Priority Class"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# LLQ

## Definition

**LLQ (Low Latency Queuing)** puts **delay-sensitive traffic** — voice, real-time video — into a **strict-priority queue** that is **always drained first** on egress. Config: a `priority` (or `priority percent`) class inside [[MQC]]/[[CBWFQ]]. Because priority classes can starve others, **policing limits the priority rate** (excess = dropped); everything else keeps its [[CBWFQ]] guaranteed share.

## The Priority Lane

```text
arrival: VOICE (priority 128 kbps) | DATA (bandwidth/share)
egress selection: priority queue drained FIRST, always
token/policing on the priority class: bursts above rate = drop (never queue!)
result: max delay bound for voice; data survives via its own bandwidth share
```

## Exam Focus

- **"Which mechanism gives voice dedicated, always-first service?" → LLQ** — the definition; replaces PQ because the priority queue is **policed** (no starvation).
- **LLQ vs PQ legacy**: PQ could starve; LLQ caps priority via policing — the improvement question.
- **Config keyword**: `priority` in the policy-map — recognition; `priority percent 10`.
- What happens above the priority rate? → drop, not queue — the "voice is never delayed/buffered" fact.

## Related Terms

- [[CBWFQ]], [[Queuing]], [[MQC]], [[Policing]], [[IntServ]]
- Level 21 notes: [[Level 21 - QoS/10. LLQ & CBWFQ]]