---
tags: [CCNP, glossary, qos, networking]
aliases: ["CBWFQ", "Class-Based Weighted Fair Queuing", "Class-Based WFQ", "bandwidth percent"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# CBWFQ

## Definition

**CBWFQ (Class-Based Weighted Fair Queuing)** is the **modern egress scheduling** method: traffic is grouped into [[MQC]] classes, and **each class receives a guaranteed bandwidth share** (`bandwidth` or `bandwidth percent`) with fair queuing inside the class. It replaces legacy WFQ/PQ/CQ and honors voice/jitter via the companion **[[LLQ]]** strict-priority class.

## The Schedule

```text
class VOICE → priority (handed to LLQ — strict priority)
class DATA-1 → bandwidth percent 30   ┐
class DATA-2 → bandwidth percent 20   ├ shared leftover fairly
class DEFAULT → fair-queue            ┘
unused class bandwidth (e.g. no LLQ traffic) is redistributed to others
```

## Exam Focus

- **"Which scheduler guarantees per-class bandwidth?" → CBWFQ** — the definition; egress direction.
- **Options**: `bandwidth <kbps>` vs `bandwidth percent` vs `fair-queue` (best-effort default class) — the config choice.
- **CBWFQ vs LLQ**: CBWFQ = guaranteed share (can still queue); LLQ = strict priority for real-time — the pairing.
- Legacy contrast: WFQ = per-flow implicit; CBWFQ = explicit classes — "what made WFQ 'weighted'?" historical hook.

## Related Terms

- [[LLQ]], [[Queuing]], [[MQC]], [[WRED]]
- Level 21 notes: [[Level 21 - QoS/10. LLQ & CBWFQ]]