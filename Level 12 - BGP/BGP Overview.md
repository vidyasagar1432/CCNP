---
tags: [CCNP, MOC]
aliases: ["Level 12 - BGP"]
status: complete
created: 2026-08-28
difficulty: medium
level: 12
exam: ENCOR-350-401
type: index
---

# Level 12 - BGP

Covers the [[BGP|Border Gateway Protocol]], the routing protocol of the internet. Explains [[eBGP]] and [[iBGP]] operation, the [[BGP Path Selection|path selection]] process, and the path attributes such as [[AS Path|AS path]], [[Local Preference|local preference]], and [[MED]]. Also covers [[Communities|communities]], [[Route Reflector|route reflectors]], [[Confederation|confederations]], [[BGP Aggregation|aggregation]], [[Policy-Based Routing|policy routing]], and the [[Prefix List|prefix-list]] and [[Route Map|route-map]] tools used to influence BGP behavior.

## BGP Fundamentals

1. [[01. eBGP]] - External BGP between autonomous systems
2. [[02. iBGP]] - Internal BGP within an autonomous system
3. [[03. Path Selection]] - The BGP best-path selection algorithm
4. [[04. AS Path]] - Tracking AS hops and loop prevention
5. [[05. Local Preference]] - Influencing outbound path selection
6. [[06. MED]] - Multi-Exit Discriminator for inbound routing
7. [[07. Communities]] - Tagging and signaling path policy

## Scaling BGP

8. [[08. Route Reflector]] - Scaling iBGP full-mesh
9. [[09. Confederation]] - Dividing an AS into sub-ASes
10. [[10. Aggregation]] - Summarizing BGP prefixes

## Policy & Control

11. [[11. Policy Routing]] - Applying routing policy
12. [[12. Prefix Lists]] - Matching network prefixes in filters
13. [[13. Route Maps]] - Conditional route manipulation
14. [[14. Troubleshooting]] - Diagnosing common BGP problems

```
├── 01. eBGP.md
├── 02. iBGP.md
├── 03. Path Selection.md
├── 04. AS Path.md
├── 05. Local Preference.md
├── 06. MED.md
├── 07. Communities.md
├── 08. Route Reflector.md
├── 09. Confederation.md
├── 10. Aggregation.md
├── 11. Policy Routing.md
├── 12. Prefix Lists.md
├── 13. Route Maps.md
├── 14. Troubleshooting.md
└── BGP Overview.md
```

## Glossary Terms Used

- [[BGP]], [[eBGP]], [[iBGP]], [[BGP Path Selection]], [[AS Path]], [[Local Preference]], [[MED]], [[Communities]], [[Route Reflector]], [[Confederation]], [[BGP Aggregation]], [[Policy-Based Routing]], [[Prefix List]], [[Route Map]]
