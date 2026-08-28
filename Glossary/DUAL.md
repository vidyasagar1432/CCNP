---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["Diffusing Update Algorithm"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# DUAL

## Definition

**DUAL (Diffusing Update Algorithm)** is the core math of EIGRP. It guarantees **loop-free paths at every instant** by selecting a primary route ([[Successor]]) and keeping verified backups ([[Feasible Successor|Feasible Successors]]) using the **feasibility condition**.

## How It Works

```text
1. Build topology table from all neighbor advertisements
2. For each destination: pick lowest-metric path → successor
3. Keep loop-free backups whose reported distance < feasible distance
4. On successor loss: promote a feasible successor (no recompute)
5. If none: enter active state → send QUERY to neighbors
   → diffusing computation → reply → new FD chosen
```

Neighboring routers "diffuse" queries and replies through the network; only affected routers recompute — that is why convergence is **fast and bounded** (and why [[EIGRP Stub|stub routers]] matter: they cap query scope).

## Key Concepts

- **Feasible distance (FD):** best metric to a destination from this router.
- **Reported (advertised) distance (RD):** metric a neighbor advertises.
- **Feasibility condition:** RD < FD — proves the neighbor's path cannot loop.

## Exam Focus

- **A feasible successor exists only when RD < FD** — the single most-tested DUAL rule.
- Without an FS, EIGRP goes **active** (route in "active state" = querying). Stuck-in-active (**SIA**) = queries not answered → usually a flapping/lossy link.
- DUAL is *diffusing* because computations propagate to neighbors, unlike SPF which is fully local ([[SPF Algorithm]]).
- Show commands: `show ip eigrp topology` reveals FD, RD, and active routes.

## Related Terms

- [[EIGRP]], [[Successor]], [[Feasible Successor]], [[EIGRP Stub]]
- Level 11 notes: [[Level 11 - EIGRP/01. DUAL]]