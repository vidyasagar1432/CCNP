---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Open Shortest Path First", "OSPFv2", "OSPFv3"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# OSPF

## Definition

**OSPF (Open Shortest Path First)** is an open-standard **link-state IGP**: routers flood information about their directly attached links (via [[LSA]]s), build a complete **[[Link State Database]]**, then run the **SPF (Dijkstra)** algorithm to compute shortest paths to every destination.

## Versions

| Version | Protocol | Handles |
| --- | --- | --- |
| OSPFv2 | RFC 2328 | IPv4 |
| OSPFv3 | RFC 5340 | IPv6 (and IPv4 with address families) |

## How It Works

```text
1. Hello protocol → discover neighbors (see Neighbor States)
2. Database exchange (LSA flooding) → identical LSDB per area
3. SPF computation → loop-free shortest-path tree
4. Route installation into the routing table
```

Key attributes:

- **Areas** ([[OSPF Area]]) give scalability — routers only keep full LSDB detail *within* their area.
- All routers in an area must have an **identical LSDB** to compute a consistent tree.
- Cost = reference bandwidth / interface bandwidth (see [[OSPF Cost]]).
- Fast convergence (event-driven, no periodic full updates) and native support for VLSM/CIDR.

## Exam Focus

- OSPF is **link-state**, not distance-vector: ads describe links, not destinations.
- **Two routers must agree on Hello/Dead intervals, area, network type, authentication, and subnet** before forming an adjacency (see [[OSPF Neighbor States]]).
- The backbone **area 0** must be contiguous — that is what [[Virtual Link]]s and ABR conventions exist for.
- Hierarchy is by **area**, not by classful network.

## Related Terms

- [[LSA]], [[Link State Database]], [[OSPF Area]], [[OSPF Router ID]], [[OSPF Neighbor States]], [[DR BDR]], [[ABR]], [[ASBR]], [[OSPF Cost]], [[OSPFv3]]
- Level 10 notes: [[Level 10 - OSPF/OSPF Overview]]