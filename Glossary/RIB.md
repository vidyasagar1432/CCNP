---
tags: [CCNP, glossary, routing, networking]
aliases: ["RIB", "Routing Information Base"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# RIB

## Definition

The **RIB (Routing Information Base)** is the router's **control-plane routing database** — the sum of everything every source (connected, [[Static Routing|static]], [[OSPF]], [[EIGRP]], [[BGP]]…) knows, after AD/metric selection. In Cisco terms the RIB **is** the [[Routing Table]] ('show ip route'); the hardware forwarding copy is the [[FIB]].

## RIB in the Pipeline

```text
connected/static    ─┐
OSPF ────────────────┼─► RIB (best routes, AD+metric decided)
EIGRP ───────────────┤        │
BGP (via BGP table) ─┘        ▼
                    CEF builds FIB + adjacencies from RIB
                                 ▼
                         data plane forwards
```

- **BGP keeps its OWN table** (all received paths) and only injects best paths into the RIB — the "BGP table ≠ routing table" fact.
- Platforms may have separate IPv4/IPv6 RIBs (`show ip route` / `show ipv6 route`).

## Exam Focus

- **"Which term names the router's full routing database?" → RIB** (or routing table) — and **FIB** is the hardware forwarding copy. The RIB/FIB pairing question is frequent and the wording matter.
- "BGP paths live only in the BGP table until chosen" — a redistribution/BGP troubleshooting classic.
- Adjacency/nexthop resolution happens as RIB → FIB: [[Recursive Lookup]] is a RIB-level activity, FIB caches the outcome.

## Related Terms

- [[FIB]], [[Routing Table]], [[BGP]], [[CEF]], [[Recursive Lookup]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/06. RIB]]