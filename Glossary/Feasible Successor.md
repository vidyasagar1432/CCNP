---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["Feasible Successor", "FS", "Backup Path"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# Feasible Successor

## Definition

A **Feasible Successor (FS)** is an EIGRP backup path to a destination that DUAL has proven **loop-free** via the **feasibility condition**. It is held in the topology table, ready to become the [[Successor]] the moment the primary path fails.

## Feasibility Condition

```text
FS ⇔ reported distance (RD) of the neighbor  <  feasible distance (FD)

RD < FD  → the neighbor's route cannot loop back through us
           (it already has a better path independent of ours)
```

## How It Works

```text
desktop route loss
        │
        ▼
  successor fails ──► promote FS instantly (no active state)
                         │
                         ▼
                 route converges without queries
```

If **no** feasible successor exists, DUAL enters the **active state**: it sends queries, neighbors reply, and a new FD is agreed (slower, and the [[EIGRP Stub|stub]] design exists to bound that query storm).

## Exam Focus

- **RD < FD is the entire test** — if RD equals or exceeds FD, the path is rejected even though it may be "working." This is the #1 DUAL question.
- An FS is *not* installed in the routing table — it is a standby.
- Unequal-cost load balancing still requires an FS (or equal-metric successor), which is why **[[Variance]]** only works over loop-free backups.

## Related Terms

- [[DUAL]], [[Successor]], [[EIGRP]], [[Variance]]
- Level 11 notes: [[Level 11 - EIGRP/04. Feasible Successor]]