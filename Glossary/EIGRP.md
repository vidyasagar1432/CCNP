---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["Enhanced Interior Gateway Routing Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# EIGRP

## Definition

**EIGRP (Enhanced Interior Gateway Routing Protocol)** is a Cisco-proprietary, **advanced distance-vector (hybrid) IGP** that combines distance-vector simplicity with link-state-like fast convergence, thanks to the **[[DUAL]]** algorithm and a reliable transport ([[RTP]]).

## Key Characteristics

| Feature | Value |
| --- | --- |
| Algorithm | [[DUAL]] — loop-free backups precomputed |
| Transport | [[RTP]] over multicast 224.0.0.10 (unicast for updates) |
| Metric | Composite of bandwidth, delay, load, reliability, MTU |
| Updates | **Partial, bounded** — only changed routes, only affected routers |
| AD | 90 internal / 170 external |
| Neighbor discovery | [[Hello]] every 5 s (default, up to 60 s on slow links), hold 15 s |

It is called "hybrid" because it keeps neighbor tables and advertises only routes (distance-vector traits) while relying on topology info and diffusing computations (link-state traits) for loop freedom.

## Exam Focus

- **EIGRP is not a pure distance-vector protocol** — the topology table + feasibility condition make it hybrid. A classic trap.
- Convergence is fast because **backup paths ([[Feasible Successor|FS]]) are known in advance** — no re-computation needed.
- The [[OSPF|other]] IGP comparisons (EIGRP vs OSPF vs RIP) are common ENCOR items: AD values 90 vs 110 vs 120.

## Related Terms

- [[DUAL]], [[RTP]], [[Successor]], [[Feasible Successor]], [[Variance]]
- Level 11 notes: [[Level 11 - EIGRP/EIGRP Overview]]