---
tags: [CCNP, glossary, qos, networking]
aliases: ["DSCP", "Differentiated Services Code Point", "PHB", "Expedited Forwarding", "Assured Forwarding", "EF", "AF", "Class Selector"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# DSCP

## Definition

**DSCP (Differentiated Services Code Point)** is the **6-bit field** in the IP header (ToS byte redefined; originally the 3-bit IP precedence) that selects a **PHB (per-hop behavior)** under [[DiffServ]]. The PHB classes: **EF** (Expedited Forwarding = voice, low loss/latency/jitter), **AF** (Assured Forwarding = 4 classes × 3 drop precedences, `AFxy`), **CS** (Class Selector, backward compat with IP precedence), **default/BE**.

## The Code Point Table

| Traffic | DSCP | Binary |
| --- | --- | --- |
| Voice | EF | 101110 |
| Video conferencing | AF41 | 100010 |
| Bulk data | AF11–AF13 | 001010–001110 |
| Best effort | 0 (CS0) | 000000 |
| CS6 (routing) / CS7 | 110000 / 111000 | — |

## Exam Focus

- **"How many bits is DSCP / how many values?" → 6 bits, 64 values** — the field question (3 bits → 8 for the old precedence).
- **EF vs AF vs CS**: EF = one low-latency class; AF = 12 (4×3) with drop precedences; CS = backward compat — the PHB identification.
- **Binary→decimal quickly**: EF = 46, AF41 = 34, AF21 = 18, CS3 = 24 — the numeric conversions exams love.
- DSCP is carried through MPLS as EXP / through L2 as 802.1p — the mapping question.

## Related Terms

- [[DiffServ]], [[QoS Marking]], [[WRED]], [[QoS Classification]]
- Level 21 notes: [[Level 21 - QoS/11. DSCP PHB Deep-Dive]]