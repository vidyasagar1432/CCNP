---
tags: [CCNP, MOC]
aliases: ["Level 09 - Routing Fundamentals"]
status: complete
created: 2026-08-28
difficulty: medium
level: 09
exam: ENCOR-350-401
type: index
---

# Level 09 - Routing Fundamentals

Introduces how routers make forwarding decisions: the routing table, metrics, and administrative distance, along with the control-plane structures like the RIB, FIB, and CEF. Also covers static and default routing, floating static routes, and route summarization before moving into dynamic routing protocols.

## Forwarding Structures

1. [[01. Routing Table]] - How routes are stored and selected
2. [[02. Administrative Distance]] - Trustworthiness ranking of route sources
3. [[03. Metrics]] - How distance is measured for routing decisions
4. [[04. Recursive Lookup]] - Resolving next hops that require another lookup
5. [[05. FIB]] - Forwarding Information Base for fast lookup
6. [[06. RIB]] - Routing Information Base storing all routes
7. [[07. CEF]] - Cisco Express Forwarding architecture

## Static Routing

8. [[08. Static Routing]] - Manually configured routes
9. [[09. Floating Static]] - Backup static routes with high AD
10. [[10. Default Route]] - The 0.0.0.0/0 catch-all route

## Route Optimization

11. [[11. Route Summarization]] - Reducing routing table size
12. [[12. Dynamic Routing]] - Introduction to routing protocol operation

```
├── 01. Routing Table.md
├── 02. Administrative Distance.md
├── 03. Metrics.md
├── 04. Recursive Lookup.md
├── 05. FIB.md
├── 06. RIB.md
├── 07. CEF.md
├── 08. Static Routing.md
├── 09. Floating Static.md
├── 10. Default Route.md
├── 11. Route Summarization.md
└── 12. Dynamic Routing.md
```
