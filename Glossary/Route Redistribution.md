---
tags: [CCNP, glossary, routing, redistribution]
aliases: ["Route Redistribution", "Redistribution", "Mutual Redistribution"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Route Redistribution
created: 2026-08-29
---

# Route Redistribution

## Definition

**Route redistribution** injects routes learned by **one routing protocol into another** (OSPF ↔ EIGRP, EIGRP ↔ BGP, static ↔ anything) so that multi-protocol networks reach everywhere. It is powerful — and dangerous: **different metrics, different loop-avoidance logic, and AD differences** mean redistribution without discipline creates suboptimal paths, routing loops, and table bloat.

## The Classic Setup

```text
OSPF        EIGRP
  |           |
[ABR/ASBR][redistributor]
   └── redistribute ospf 100 metric 20000     (EIGRP side, seed metric!)
   └── redistribute eigrp 100 subnets          (OSPF side, type E2 default)
two-way = MUTUAL redistribution → filters + tags MANDATORY
```

## The Redistribution Toolkit

| Problem | Tool |
| --- | --- |
| New protocol gets unknown metric | [[Seed Metric]] |
| Tracing/HQ-filtering origin info | [[Route Tag]] |
| Limiting what crosses the boundary | [[Route Filtering]] (distribute-list, route-map) |
| Why loops appear | AD asymmetry + [[Routing Loop|loop detection]] (Route Tag + filters) |
| Where routes land in OSPF | E1 vs E2 (external types) — E2 default |

## Exam Focus

- **Seed metric**: redistributed routes fail with "not advertised" until a compatible metric is set (`metric` keyword or default-metric) — top symptom.
- **Loop prevention**: filter BOTH directions + tag — "mutual redistribution between two protocols creates routing loops unless filtered" is the recite-back sentence.
- Know which AD wins at each boundary: OSPF external (110/170), EIGRP external 170 — asymmetric AD *is* the loop mechanism.

## Related Terms

- [[Seed Metric]], [[Route Tag]], [[Route Filtering]], [[Routing Loop]], [[Administrative Distance]]
- Level 13 notes: [[Level 13 - Route Redistribution/01. OSPF to EIGRP]]