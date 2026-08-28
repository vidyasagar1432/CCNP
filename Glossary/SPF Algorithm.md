---
tags: [CCNP, glossary, ospf, routing]
aliases: ["SPF", "Dijkstra", "Shortest Path First", "SPF Algorithm"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# SPF Algorithm

## Definition

The **SPF (Shortest Path First) algorithm** — Dijkstra's algorithm — is how OSPF computes routes from the [[Link State Database]]: each router builds a shortest-path tree rooted at itself, then derives routing-table entries from the tree.

## How It Works

```text
1. Router has an identical LSDB for its area (all LSAs)
2. Treat itself as the root (cost 0)
3. Repeatedly: relax links to neighbors, pick lowest cumulative cost
4. Result: shortest-path tree (per-area)
5. Walk the tree → destination prefixes + next hop + cost
```

SPF is run:

- At OSPF startup,
- When the area's LSDB changes (new LSA),
- Only for the affected area(s) — ABRs run SPF per area.

## Characteristics

- **Fast convergence**: computed from topology, not hop-by-hop rumor like distance-vector protocols.
- **Cost metric**: uses [[OSPF Cost]] (cumulative interface costs), not hop count.
- Deterministic and loop-free: all routers in the area share topology, so they agree on the tree.

## Exam Focus

- **SPF output is the routing table; SPF input is the LSDB.** A change in LSA → recompute.
- "Why is the longer path chosen?" → because **cumulative cost** is lower; cost beats hop count.
- SPF runs **per area**, keeping scale manageable (area design exists partly to bound SPF cost).

## Related Terms

- [[OSPF]], [[Link State Database]], [[LSA]], [[OSPF Cost]], [[OSPF Area]]
- Level 10 notes: [[Level 10 - OSPF/07. SPF Algorithm]]