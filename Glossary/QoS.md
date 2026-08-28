---
tags: [CCNP, glossary, qos, networking]
aliases: ["QoS", "Quality of Service", "Network QoS"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# QoS

## Definition

**QoS (Quality of Service)** is the toolkit for **managing bandwidth, delay, jitter, and loss** so critical traffic (voice, video) survives alongside bulk data. The pipeline: **[[QoS Classification|classify]] → [[QoS Marking|mark]] → ([[Policing]]/[[Shaping]]) → [[Queuing]]/[[CBWFQ]]+[[LLQ]] → [[WRED]]** — all built with [[MQC]] and the [[DiffServ]]/[[DSCP]] model. When traffic matters, QoS decides who gets the network first.

## The Pipeline

```text
classify (match) → mark (DSCP/CoS) → trust ([[Trust Boundary]]) →
rate-limit (police/shape) → schedule (queue: LLQ for voice, CBWFQ shares) →
manage drops (WRED before tail-drop)
config vehicle: MQC — class-map / policy-map / service-policy
```

## Exam Focus

- **"What does QoS protect?" → latency/jitter/loss sensitive traffic under congestion** — the definition; no congestion = no QoS drama.
- **The order**: classification before marking before scheduling — the pipeline question.
- **The big three exams love**: LLQ (voice), CBWFQ (class share), WRED (avoid sync) — the mechanisms.
- QoS is only useful where bandwidth is scarce or delay matters — the "where to deploy?" design answer.

## Related Terms

- [[QoS Classification]], [[QoS Marking]], [[Policing]], [[Shaping]], [[Queuing]], [[CBWFQ]], [[LLQ]], [[WRED]], [[MQC]], [[DiffServ]], [[DSCP]], [[Trust Boundary]]
- Level 21 overview: [[Level 21 - QoS/QoS Overview]], Level 29 note: [[Level 29 - Troubleshooting/16. QoS]]