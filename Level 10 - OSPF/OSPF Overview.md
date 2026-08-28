---
tags: [CCNP, MOC]
aliases: ["Level 10 - OSPF"]
status: complete
created: 2026-08-28
difficulty: medium
level: 10
exam: ENCOR-350-401
type: index
---

# Level 10 - OSPF

Covers the [[OSPF|Open Shortest Path First]] link-state routing protocol in depth, from OSPFv2 and OSPFv3 operation to neighbor state machines, DR/BDR election, LSA types, and the SPF algorithm. Also covers [[OSPF Area|area]] design with [[Stub Area|stub]], [[Totally Stubby Area|totally stubby]], and [[NSSA]] areas, [[Virtual Link|virtual links]], [[OSPF Authentication|authentication]], summarization, and troubleshooting.

## Protocol Basics

1. [[01. OSPFv2]] - OSPF for IPv4
2. [[02. OSPFv3]] - OSPF for IPv6
3. [[03. Router ID]] - Router identifier election and selection
4. [[04. Neighbor States]] - The OSPF neighbor state machine
5. [[05. DR BDR]] - Designated and backup designated router election

## LSDB & SPF

6. [[06. LSA Types]] - Link State Advertisement types
7. [[07. SPF Algorithm]] - Dijkstra shortest path computation

## Areas

8. [[08. Areas]] - Area design and ABR/ASBR roles
9. [[09. Stub]] - Stub areas that block external routes
10. [[10. Totally Stubby]] - Stub areas that also block inter-area routes
11. [[11. NSSA]] - Not-So-Stubby areas with external route import
12. [[12. Virtual Links]] - Connecting disconnected areas

## Operations

13. [[13. Authentication]] - Securing OSPF neighbor relationships
14. [[14. Summarization]] - Summarizing routes at area boundaries
15. [[15. Troubleshooting]] - Diagnosing common OSPF problems

```
├── 01. OSPFv2.md
├── 02. OSPFv3.md
├── 03. Router ID.md
├── 04. Neighbor States.md
├── 05. DR BDR.md
├── 06. LSA Types.md
├── 07. SPF Algorithm.md
├── 08. Areas.md
├── 09. Stub.md
├── 10. Totally Stubby.md
├── 11. NSSA.md
├── 12. Virtual Links.md
├── 13. Authentication.md
├── 14. Summarization.md
└── 15. Troubleshooting.md
```

## Glossary Terms Used

- [[OSPF]], [[OSPFv3]], [[OSPF Area]], [[Stub Area]], [[Totally Stubby Area]], [[NSSA]], [[Virtual Link]], [[OSPF Authentication]]
