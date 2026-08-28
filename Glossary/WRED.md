---
tags: [CCNP, glossary, qos, networking]
aliases: ["WRED", "Weighted Random Early Detection", "Congestion Avoidance", "RED", "Tail Drop"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# WRED

## Definition

**WRED (Weighted Random Early Detection)** is **congestion avoidance**: instead of waiting for the queue to fill and **tail-dropping**, it starts **randomly dropping** (or marking, via ECN) when the average queue depth crosses a threshold — selectively, so **TCP flows slow down early and avoid global synchronization**. "Weighted" = lower-priority (more drop-eligible) traffic is dropped sooner.

## Why It Helps

```text
tail-drop: queue full → drop everything → ALL TCP flows timeout together → 
           global synchronization (sawtooth, wasted bandwidth)
WRED: as depth grows → drop probability rises per class →
      only some flows back off → no synchronization, better utilization
drop profile per class: min threshold → max threshold → mark-probability
```

## Exam Focus

- **"Which tool prevents TCP global synchronization?" → WRED** — the purpose definition; AQM (active queue management).
- **WRED vs tail-drop**: drop before full, randomly and proportionally — the contrast.
- **Weighted = class-aware** (DSCP-based drop eligibility, e.g. AF classes drop in order AF11→AF13) — the "why weighted?" answer.
- ECN variant: mark instead of drop (RFC 3168) — the modern mention.

## Related Terms

- [[Queuing]], [[CBWFQ]], [[DSCP]]
- Level 21 notes: [[Level 21 - QoS/06. Congestion Avoidance]]