---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["Unequal Cost Load Balancing", "Unequal-Cost Load Balancing", "UCLB"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# Unequal-Cost Load Balancing

## Definition

**Unequal-cost load balancing** lets EIGRP split traffic over **multiple paths of different metrics** — something OSPF cannot do natively (it requires equal cost). It is enabled by tuning **[[Variance]]** while the paths remain loop-free **[[Feasible Successor|feasible successors]]**.

## How It Works

```text
Best path (successor):       FD = 1000
Backup path (FS, RD < FD):   metric = 3500

variance 4 → 3500 ≤ 4 × 1000 → both paths installed
traffic share = inversely proportional to each path's metric (per-packet distribution)
```

Requirements recap:

- Candidate must qualify under the **feasibility condition**.
- `variance` ≥ ratio of (worst tolerated path / best path).
- Optional `traffic-share min across-interfaces` for proportional balancing.

## Exam Focus

- **EIGRP ≠ OSPF here:** OSPF load balances only equal-cost paths (`maximum-paths`); EIGRP adds unequal-cost via variance. Classic comparison question.
- The **FC gate still applies** — variance alone never admits a looping path.
- `show ip route` with two next hops of different metrics = working unequal-cost LB.

## Related Terms

- [[EIGRP]], [[Variance]], [[Feasible Successor]], [[EIGRP Metric]], [[Successor]]
- Level 11 notes: [[Level 11 - EIGRP/10. Unequal Load Balancing]]