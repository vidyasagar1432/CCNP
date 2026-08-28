---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["EIGRP Variance", "Variance Command"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# Variance

## Definition

**`variance`** (default 1) tells EIGRP which alternate paths count as **"almost as good"** as the best path, enabling **[[Unequal-Cost Load Balancing|unequal-cost load balancing]]**:

```text
Candidate qualifies ⇔  FS metric       ≤  variance × best-metric (FD)
                                             │
                                    (and it is a feasible successor)
```

```cisco
router eigrp CCNP-NET
 address-family ipv4
  topology base
  variance 4
```

## How It Works

- With `variance 4`, any feasible path up to **4× the FD** joins the routing table alongside the successor.
- If a path also needs to be preferred by **traffic share**, `traffic-share min across-interfaces` balances proportionally to metric.
- **The path must still satisfy the feasibility condition** — variance enables *selection*, it does not relax loop-freedom.

## Exam Focus

- **Variance expands the routing-table candidates; FS ([[Feasibility Condition|RD < FD]]) is still mandatory** — a candidate that fails the FC never appears even with variance 1000.
- Default variance = 1 → only equal-cost multipath (all successors).
- The exam pairs variance with [[Feasible Successor|FS]] questions: "which of these backup paths can variance enable?"

## Related Terms

- [[EIGRP]], [[Unequal-Cost Load Balancing]], [[Feasible Successor]], [[Successor]], [[EIGRP Metric]]
- Level 11 notes: [[Level 11 - EIGRP/09. Variance]]