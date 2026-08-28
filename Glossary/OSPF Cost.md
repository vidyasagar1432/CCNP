---
tags: [CCNP, glossary, ospf, routing]
aliases: ["OSPF Cost", "OSPF Metric", "Reference Bandwidth"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# OSPF Cost

## Definition

**OSPF cost** is the metric used to select the best path — the **sum of costs along a route**. It is derived from interface bandwidth: **cost = reference bandwidth / interface bandwidth** (default reference 100 Mbps on Cisco).

## Cost Formula

```text
Cost = reference-bandwidth / bandwidth
 Default reference: 100 Mbps

100 Mbps link   → 100/100   = 1
1 Gbps link     → 100/1000  = 1    (Cisco rounds up; default ref favors slow links)
10 Mbps link    → 100/10    = 10
```

For high-speed links, raise the reference:

```cisco
router ospf 1
 auto-cost reference-bandwidth 1000   ! treat 1 Gbps as cost 1
```

## Path Selection

```text
Path cost = Σ of each outgoing interface cost toward the destination
Lowest cumulative cost wins (SPF)
```

Unlike RIP's hop count, OSPF cost reflects **link speed**, so the "most hops" path can win if it is faster.

## Exam Focus

- **Reference bandwidth defaults differ conceptually by platform** — the exam focuses on the formula and on changing it for Gigabit+ links (cost 1000 Mbps/1 Gbps = 1).
- Interface cost can be overridden manually (`ip ospf cost X`) — used for traffic engineering.
- Cost to a route is **cumulative over the path**, not per-hop equal.

## Related Terms

- [[OSPF]], [[OSPF Area]], [[SPF Algorithm]]
- Level 10 notes: [[Level 10 - OSPF/01. OSPFv2]], [[Level 10 - OSPF/07. SPF Algorithm]]