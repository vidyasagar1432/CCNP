---
tags: [CCNP, glossary, routing, networking]
aliases: ["Dynamic Routing", "Routing Protocol", "Interior Gateway Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Dynamic Routing

## Definition

**Dynamic routing** is when **routing protocols** discover and maintain routes automatically — routers exchange reachability info, compute best paths, and **converge** on topology changes without an admin. The big family: link-state ([[OSPF]], [[IS-IS]]), distance-vector ([[EIGRP]] — technically hybrid, [[RIP]]), and path-vector ([[BGP]]).

## The Family Tree

| Protocol | Type | Metric | Scope |
| --- | --- | --- | --- |
| OSPF | Link-state (SPF) | Cost (BW) | IGP |
| IS-IS | Link-state (SPF) | Metric | IGP (SP backbone) |
| EIGRP | Advanced DV (DUAL) | Composite | IGP (Cisco) |
| RIP | Distance-vector | Hops (≤15) | IGP (course drop) |
| BGP | Path-vector | Attributes | EGP (Internet) |

```text
convergence = the time between "topology change" and "all routers agree"
             (link-state = fast, SPF; distance-vector = slower, count-to-infinity)
```

## Exam Focus

- **"Which term describes protocols that share routes and adapt automatically?" → dynamic routing** — as opposed to [[Static Routing]].
- Know who calculates with SPF (OSPF/IS-IS) vs DUAL (EIGRP) vs attributes (BGP) — one-line "who uses what algorithm".
- Routing **loops**: distance-vector's count-to-infinity vs link-state's per-link flooding — the protocol-behavior comparison is classic.

## Related Terms

- [[OSPF]], [[EIGRP]], [[BGP]], [[Routing Table]], [[Metrics]], [[Administrative Distance]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/12. Dynamic Routing]]