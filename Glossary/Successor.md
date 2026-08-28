---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["EIGRP Successor"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# Successor

## Definition

A **successor** is the EIGRP route with the **best (lowest) composite metric** to a destination. Its next hop is the neighbor that advertised it, and the route is installed in the routing table. It is the "winner" selected by [[DUAL]] from the topology table.

## How It Works

```text
Topology table entry per destination:
  FD (feasible distance) = best metric from this router
  RD (reported distance) = metric advertised by each neighbor

Successor = neighbor with the smallest RD (that satisfies the loop-free rules)
              → its path = FD
```

Properties:

- A successor's route is **always loop-free** by construction.
- If the successor link fails, EIGRP immediately promotes a **[[Feasible Successor]]** — no recomputation, near-instant convergence.
- A destination may have **multiple successors** of equal metric (equal-cost load balancing).

## Exam Focus

- **Successor = best path installed in the routing table**; FS = backup in the topology table only.
- Equal-cost multipath: several successors can coexist for one prefix.
- `show ip eigrp topology` marks successors (references) vs feasible successors.
- AD: successors are internal routes with AD 90.

## Related Terms

- [[EIGRP]], [[DUAL]], [[Feasible Successor]], [[Variance]]
- Level 11 notes: [[Level 11 - EIGRP/03. Successor]]