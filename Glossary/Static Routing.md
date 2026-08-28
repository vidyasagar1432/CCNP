---
tags: [CCNP, glossary, routing, networking]
aliases: ["Static Routing", "Static Route"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Static Routing

## Definition

**Static routing** is manually configured routing — an admin writes each destination's next hop. It is **simplest, most predictable, least resource-hungry** (no protocol hellos/topology), and perfect for **stubs, default routes, and failover via floating statics** — but it does not adapt: **every change is manual**.

## The Command Forms

```text
ip route 10.1.10.0 255.255.255.0 10.1.0.2        (next-hop style)
ip route 10.1.10.0 255.255.255.0 g0/1            (exit-interface style — RIB-dependent, learns at cable-plug level)
ip route 10.1.10.0 255.255.255.0 10.1.0.2 150    (floating static → AD 150)
ip route 0.0.0.0 0.0.0.0 10.1.0.1                (default route)
```

## Design Guidance

- **Stub networks** → one static each way (loopback-edges, small branches).
- **Default routes** at the edge (next hop = ISP router).
- **Floating statics** (higher AD, e.g. 150) back up a dynamic route: only active when the primary is gone — the failover pair.
- Static routes **don't adapt** — a dead next hop keeps the route in the table unless proven unreachable (recursion check).

## Exam Focus

- **"Which path is never advertised/learned dynamically?" → static** — AD 1, code `S` in [[Routing Table]] output.
- Floating static = "secondary path with higher AD" — the exam definition of failover-by-AD.
- Next-hop-IP vs exit-interface trivia: exit-interface statics show up differently and behave differently on multi-access links — `show ip route` reading question.

## Related Terms

- [[Floating Static]], [[Default Route]], [[Routing Table]], [[Administrative Distance]], [[Recursive Lookup]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/08. Static Routing]]