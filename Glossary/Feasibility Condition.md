---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["Feasibility Condition", "FC"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# Feasibility Condition

## Definition

The **feasibility condition (FC)** is the mathematical rule [[DUAL]] uses to accept a neighbor's route as loop-free: the neighbor's **reported distance (RD) must be strictly less than the router's own feasible distance (FD)** for that destination.

```text
RD < FD   →  neighbor cannot route back through us → loop-free → candidate FS
RD ≥ FD   →  reject (would create a potential loop)
```

## Why It Works

If a neighbor's metric *to its own destination* is already lower than our best metric, then any path that comes back through us only adds metric — so the neighbor never needs us as a transit. That proves loop-freedom **without** any query broadcast.

## Exam Focus

- The FC defines a valid **[[Feasible Successor]]**; the successor itself wins simply by lowest metric.
- **Strict inequality matters:** a tie (`RD == FD`) does NOT create a feasible successor (a famous trap — "RD equal to FD" is not loop-free per DUAL).
- If topology changes drop all FS candidates, EIGRP sends [[DUAL|queries]] (active state) — the FC is what normally avoids that.

## Related Terms

- [[DUAL]], [[Feasible Successor]], [[Successor]], [[EIGRP]]
- Level 11 notes: [[Level 11 - EIGRP/01. DUAL]], [[Level 11 - EIGRP/04. Feasible Successor]]