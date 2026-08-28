---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Designated Router", "Backup Designated Router", "DR", "BDR"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# DR/BDR

## Definition

On **multi-access (broadcast) networks**, OSPF elects a **Designated Router (DR)** and a **Backup Designated Router (BDR)** to reduce LSAs and adjacencies: every router forms a full adjacency only with the DR and BDR, not with each other.

## Why They Exist

On an N-router broadcast segment, full-mesh adjacencies would create N×(N−1)/2 adjacencies. With a DR:

```text
Adjacencies: every router ↔ DR and BDR  (2N, instead of ~N²)
Type-2 Network LSA: generated only by the DR
```

All other routers stop the neighbor state machine at **2-Way** with each other (see [[OSPF Neighbor States]]).

## Election Rules

1. Highest **priority** (default 1, per interface `ip ospf priority`) — 0 means *never* DR/BDR.
2. Highest **[[OSPF Router ID]]** as tie-breaker.

```text
Election is non-preemptive: on failure, BDR becomes DR and a new BDR is elected.
```

## Exam Focus

- **DR election occurs at 2-Way** — before that state, no election happens; after, results stand.
- DR/BDR selection is **per network segment**, not per area.
- On point-to-point links there is **no DR/BDR** — a common "does OSPF do DR election on serial links?" trap.
- A new router with the highest RID joining an existing segment does **not** steal the DR role (non-preemptive).

## Related Terms

- [[OSPF]], [[OSPF Neighbor States]], [[LSA]], [[OSPF Router ID]]
- Level 10 notes: [[Level 10 - OSPF/05. DR BDR]]