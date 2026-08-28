---
tags: [CCNP, glossary, routing, networking]
aliases: ["Floating Static", "Floating Static Route"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Floating Static

## Definition

A **floating static route** is a static route with an **administrative distance higher than the primary source** (e.g. 150 vs OSPF's 110) — a **standby path that only appears in the routing table when the primary disappears**. It's the cheapest, most common failover trick in the CCNP scope.

## Failover Mechanics

```text
static route 10.1.10.0/24 via 10.1.0.2   → AD 1  (primary dynamic instead:
OSPF 10.1.10.0/24 [110/10] …                    AD 110 primary)
floating  10.1.10.0/24 via 10.1.0.9 150 → AD 150 (installed only if no better AD)
  OSPF dies → AD 110 route gone →
  floating static (AD 150) now wins the table → traffic shifts to the backup link
  OSPF returns → it beats 150 → floating static vanishes again (no false takeover)
```

## When to Use It

- **WAN failover**: primary [[OSPF]]/[[EIGRP]] over circuit A, backup Internet link via floating static.
- **Dynamic-route backstop**: if redistribution slips or the SP dies, the static catches remote subnets.
- Router never load-balances with it: it's **active/standby by design** (AD decides one winner).

## Exam Focus

- **"Which mechanism provides a manual backup path that loses to dynamic routes?" → floating static** (AD 150 myth-busting: 150 is *higher* than most dynamic, *lower* than iBGP's 200 — pick the number that beats your dynamic source).
- Command recognition: `ip route … 150` — that trailing AD is the whole feature.
- `show ip route` moment: backup present only when the primary route is absent — read the table to confirm failover state.

## Related Terms

- [[Static Routing]], [[Administrative Distance]], [[Routing Table]], [[Default Route]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/09. Floating Static]]