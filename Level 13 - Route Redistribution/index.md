---
tags: [CCNP, MOC]
aliases: ["Level 13 - Route Redistribution"]
status: complete
level: 13
exam: ENCOR-350-401
type: index
---

# Level 13 - Route Redistribution

Covers the process of exchanging routes between different routing protocols. Explains protocol-to-protocol redistribution scenarios (OSPF/EIGRP/BGP), seed metric handling, administrative distance considerations, route tagging, filtering, and the loop-prevention techniques needed when multiple redistribution points exist.

### Redistribution Scenarios

1. [[01. OSPF to EIGRP]] - Redistributing OSPF routes into EIGRP
2. [[02. OSPF to BGP]] - Redistributing OSPF routes into BGP
3. [[03. EIGRP to BGP]] - Redistributing EIGRP routes into BGP

### Mechanics

4. [[04. Seed Metrics]] - Assigning metrics to redistributed routes
5. [[05. Administrative Distance]] - AD impact on redistributed routes
6. [[06. Route Tags]] - Using tags to track route origin

### Control & Safety

7. [[07. Filtering]] - Controlling which routes are redistributed
8. [[08. Loop Prevention]] - Avoiding routing loops in multi-point redistribution

```
├── 01. OSPF to EIGRP.md
├── 02. OSPF to BGP.md
├── 03. EIGRP to BGP.md
├── 04. Seed Metrics.md
├── 05. Administrative Distance.md
├── 06. Route Tags.md
├── 07. Filtering.md
└── 08. Loop Prevention.md
```
