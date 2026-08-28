---
tags: [CCNP, glossary, routing, networking]
aliases: ["Administrative Distance", "AD", "Trustworthiness"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Administrative Distance

## Definition

**Administrative Distance (AD)** is Cisco's **trust value for route sources**: 0–255, where **lower = more trusted**. When two protocols offer the same prefix, the **lowest AD wins** — AD resolves *inter-protocol* competition before *metric* (which only compares within one protocol) ever gets a vote.

## The Table (committed to memory)

| Source | AD |
| --- | --- |
| Connected | 0 |
| Static | 1 |
| EIGRP summary | 5 |
| eBGP | 20 |
| EIGRP (internal) | 90 |
| OSPF | 110 |
| IS-IS | 115 |
| RIP | 120 |
| EIGRP (external) | 170 |
| iBGP | 200 |
| Unreachable | 255 |

## Exam Focus

- **"Two protocols advertise 10.0.0.0/8 — OSPF vs EIGRP, who wins?" → EIGRP (AD 90 < 110).** The classic.
- **AD vs metric**: AD chooses *between protocols*; metric chooses *within one* ([[Metrics]]).
- Changeable: `distance 150` under the protocol — used in redistribution filtering scenarios ([[Route Redistribution]]).

## Related Terms

- [[Routing Table]], [[Metrics]], [[Dynamic Routing]], [[Route Redistribution]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/02. Administrative Distance]]