---
tags: [CCNP, glossary, routing, networking]
aliases: ["Recursive Lookup", "Recursive Route Resolution"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Recursive Lookup

## Definition

A **recursive lookup (recursive route resolution)** is how a router turns "via 10.1.0.2" into a usable **next hop + egress interface**: the next hop is itself a network in the [[Routing Table]], so the router **looks it up again** until it finds an entry that lists an actual outgoing interface. Statics, BGP, and even OSPF next hops frequently resolve this way.

## The Two-Step Resolution

```text
ip route 10.1.10.0/24 10.1.0.2          (nh = 10.1.0.2, no interface given)
     └─► lookup 10.1.0.0/30 … found:
          → "via 10.1.0.1, GigabitEthernet0/0"  (direct/connected)
⇒ resolved: 10.1.10.0/24 via g0/0, next hop 10.1.0.1
Õfast path: the FIB caches the RESOLVED result
```

- If the next hop is unreachable → route "inactive" (`show ip route` shows it with no via / ignored).
- The **FIB ([[FIB]]) pre-resolves** this at build time, so the data plane never does the recursion.

## Exam Focus

- **"A route's next hop is not directly connected — how does the router forward?" → recursive lookup** — it resolves the gateway address through the table.
- Symptom to recognize: static route present but **not in the table** because its next hop isn't reachable (the recursion failed) — a top troubleshooting question.
- "Dual recursion" (next hop behind another recursive sub…)” — static via static — exists; each level must resolve.

## Related Terms

- [[Routing Table]], [[FIB]], [[Static Routing]], [[RIB]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/04. Recursive Lookup]]