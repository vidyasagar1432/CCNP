---
tags: [CCNP, glossary, routing, networking]
aliases: ["Routing Table", "RIB", "IP Routing Table", "show ip route"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Routing Table

## Definition

The **routing table** is the router's **control-plane database of known networks** — every destination it can reach and *how* (next hop, interface, source protocol, metric, [[Administrative Distance|AD]]). It is built from connected networks, statics, and [[Dynamic Routing|routing protocols]], and it feeds the [[FIB]] that actually forwards packets.

## Anatomy of a Route (show ip route)

```text
O    10.1.10.0/24 [110/2] via 10.1.0.2, 00:00:12, GigabitEthernet0/0
├─ O       = source (OSPF)  — a random code for the protocol
├─ 10.1.10.0/24 = prefix length, the "what"
├─ [110/2] = [administrative distance / metric]  → the why
├─ via 10.1.0.2 = next hop
└─ GigabitEthernet0/0 = egress interface
```

| Route code | Protocol |
| --- | --- |
| C / L | Connected / Local |
| S | Static |
| D | EIGRP |
| O | OSPF |
| B | BGP |
| i | IS-IS |

## Exam Focus

- **Route selection two-step**: 1) **longest prefix match** on the destination, 2) among equal-length, **lowest AD**, then **lowest metric**. Recite it in that order.
- "Which code does X show?" — memorize the `show ip route` legend (D=EIGRP, O=OSPF, B=BGP…).
- The routing table is the **RIB** — the FIB is its forwarding-optimized copy ([[FIB]] vs [[RIB]]).

## Related Terms

- [[Administrative Distance]], [[Metrics]], [[FIB]], [[RIB]], [[Static Routing]], [[Default Route]], [[Dynamic Routing]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/01. Routing Table]]