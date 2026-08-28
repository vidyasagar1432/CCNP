---
tags: [CCNP, glossary, routing, networking]
aliases: ["Metrics", "Routing Metric", "Composite Metric"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Metrics

## Definition

A **metric** is the *within-protocol* cost a router uses to pick the **best path among routes learned from the SAME protocol** — lower is better. Each protocol invents its own: **OSPF cost (bandwidth)** , **EIGRP composite (bandwidth+delay…)** , **RIP hop count**, **BGP path attributes**. Different protocols' metrics are **not comparable** — that's what [[Administrative Distance|AD]] is for.

| Protocol | Metric = | Basis |
| --- | --- | --- |
| OSPF | Cost = 10⁸/bandwidth | Reference 100 Mbps |
| EIGRP | Composite: (K1·BW + K2·BW/(256−load) + K3·delay)·256… | BW, delay, load, reliability (K-values) |
| RIP | Hop count (≤15) | Hops |
| IS-IS | Metric (default 10 per interface) | Manual/auto |

## Exam Focus

- **"Which metric does OSPF use?" → cost from bandwidth; "EIGRP?" → composite; "RIP?" → hops.** The triad.
- Per-interface tweaks: `ip ospf cost <n>` overrides bandwidth math; EIGRP `bandwidth` + `delay` commands change the composite.
- **Metric comparison across protocols is invalid** — the question that tests this pairs two different protocols and expects "compare by AD first".

## Related Terms

- [[Administrative Distance]], [[Routing Table]], [[OSPF Cost]], [[EIGRP Metric]], [[Dynamic Routing]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/03. Metrics]]