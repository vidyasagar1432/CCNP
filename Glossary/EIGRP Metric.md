---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["EIGRP Metric", "Composite Metric", "EIGRP K Values"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# EIGRP Metric

## Definition

The **EIGRP composite metric** ranks routes to a destination. Unlike [[OSPF Cost|OSPF cost]] (one link factor) it combines **bandwidth, delay, load, reliability, and MTU** — by default only **bandwidth and delay** are used (K1=K3=1, K2=K4=K5=0).

## The Formula (defaults)

```text
metric = 256 × [ (10⁷ / minimum bandwidth) + (Σ delays / 10) ]
```

- **Bandwidth term:** the *minimum* bandwidth along the path (kbps).
- **Delay term:** the *sum* of delays of all outbound interfaces (tens of microseconds).
- Delay dominates at 256×; bandwidth catches slow links.

## What Matters in Practice

| Fact | Meaning |
| --- | --- |
| Only K1 + K3 active by default | Load/reliability rarely shuffle the ranking |
| Metric is **end-to-end cumulative** | Same principle as OSPF path cost |
| Paths differ only by delay | Same bandwidth → delay decides |

## Exam Focus

- **The default formula uses bandwidth + delay only** — a frequent question stalls on "does EIGRP count load?" → only if K2 is enabled.
- **Bandwidth term uses the *minimum* bandwidth hop; delay is summed.**
- Changing `bandwidth` on an interface changes the metric — the classic "why did the EIGRP path change?" scenario.

## Related Terms

- [[EIGRP]], [[DUAL]], [[Successor]], [[OSPF Cost]] (contrast)
- Level 11 notes: [[Level 11 - EIGRP/03. Successor]]