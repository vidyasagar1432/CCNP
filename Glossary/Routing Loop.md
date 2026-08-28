---
tags: [CCNP, glossary, routing, redistribution]
aliases: ["Routing Loop", "Routing Loops", "Count to Infinity", "Ping-Pong"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Route Redistribution
created: 2026-08-29
---

# Routing Loop

## Definition

A **routing loop** is when packets **ping-pong between routers forever** because each router thinks the other is the path to the destination. Causes: **inconsistent AD across protocols** (mutual [[Route Redistribution|redistribution]]), **count-to-infinity** in distance-vector, faulty aggregation, or stale routes — always a forwarding-consistency failure, never a hardware fault.

## How Redistribution Creates Loops

```text
mutual redistribution, SAME prefix, different AD:
  OSPF side: EIGRP route arrives as O E2 [110/20]     ← OSPF route wins locally
  EIGRP side: OSPF route arrives as D EX [170/x]      ← EIGRP's OWN wins locally
  ⇒ each domain prefers its native route and points at the OTHER domain
  ⇒ packets bounce across the boundary forever  (the redistribute ping-pong)
```

Prevention toolkit: **filter both directions, tag everything, mind the ADs, use route-maps**.

## Exam Focus

- **"What two things MUST accompany mutual redistribution?" → filters and loop control (tags)** — the safety-pair answer.
- **Count-to-infinity**: distance-vector's bad-news problem (RIP's 16 = unreachable; split horizon / poison reverse mitigate) — protocol-specific loop questions.
- Traceroute symptom: packet TTL-1 hops alternate across the same two routers → recite "AD asymmetry at the redistribution boundary".

## Related Terms

- [[Route Redistribution]], [[Route Tag]], [[Route Filtering]], [[Administrative Distance]], [[RIP]]
- Level 13 notes: [[Level 13 - Route Redistribution/08. Loop Prevention]]