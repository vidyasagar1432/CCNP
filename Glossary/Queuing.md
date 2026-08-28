---
tags: [CCNP, glossary, qos, networking]
aliases: ["Queuing", "Scheduling", "QoS Queuing", "WRR", "Strict Priority"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# Queuing

## Definition

**Queuing (scheduling)** decides **in what order packets leave an interface during congestion** — the egress discipline. The modern Cisco answer: **[[CBWFQ]]** gives each class a guaranteed share (weighted), and **[[LLQ]]** puts delay-sensitive traffic (voice) in a **strict-priority queue** ahead of everything. Queuing acts **only when buffers fill** — no congestion, no scheduling drama.

## The Egress Picture

```text
interfaces have per-class queues (bandwidth = guaranteed share, bytes/queue)
LLQ: priority queue drained first → voice/video real-time traffic
CBWFQ: leftover bandwidth split by class weights (fair within class)
drop strategy inside queues: WRED (see [[WRED]]) or tail-drop
```

## Exam Focus

- **"Which mechanism orders packets out of a congested interface?" → queuing** — the definition; congestion-triggered behavior.
- **Classic queuing types**: FIFO, PQ, CQ, WFQ, CBWFQ, LLQ — "which is the modern default?" → CBWFQ + LLQ.
- Queuing vs [[WRED]]: queuing = ordering; WRED = drop-before-full — the mechanism separation.
- Scheduling fairness: WFQ = per-flow implicit; CBWFQ = per-class explicit — the fairness question.

## Related Terms

- [[CBWFQ]], [[LLQ]], [[WRED]], [[Shaping]]
- Level 21 notes: [[Level 21 - QoS/05. Queuing]]