---
tags: [CCNP, glossary, qos, networking]
aliases: ["Policing", "Token Bucket", "Policer", "Conform Exceed Violate"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# Policing

## Definition

**Policing** enforces a rate by **dropping (or re-marking) excess traffic** — it **does not buffer**. Built on the **token bucket** model (CIR + Bc, two/three-rate variants), it works on **ingress or egress**, and classifies each packet as **conform / exceed / (violate)**: conform = pass, exceed = drop or remark (EF→AF), violate = drop. Policing causes **bursty, jerkier** output but **no added latency**.

## The Combined Bucket

```text
conform: tokens available → pass (possibly with set-dscp)
exceed:  Bc consumed but Be tokens left → drop or re-mark (e.g. EF→AF41)
violate: all tokens gone → drop
single-rate vs two-rate (SrTCM/trTCM): single = CIR; dual = CIR + peak
```

## Exam Focus

- **"Which rate-limiter drops, doesn't buffer?" → policing**; "which adds latency?" → [[Shaping]] — the contrast pair.
- **Can police on ingress and egress**; shaping is egress-only — the placement question.
- **Token bucket parameters**: Bc = CIR × Tc — the CIR/Bc/Tc relationship (be able to compute burst).
- Policer actions: pass / drop / remark — the action list; "set-dscp" on exceed.

## Related Terms

- [[Shaping]], [[QoS Classification]], [[MQC]]
- Level 21 notes: [[Level 21 - QoS/03. Policing]]