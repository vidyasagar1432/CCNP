---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Mesh Topology", "Full Mesh", "Partial Mesh"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Mesh Topology

## Definition

In a **mesh topology**, nodes are interconnected with direct links: **full mesh** (every node to every other) or **partial mesh** (only selected pairs). Mesh maximizes redundancy and minimizes hops — at the cost of link count and complexity.

## Full vs Partial

```text
FULL mesh (N nodes): N×(N−1)/2 links
  e.g. 4 nodes = 6 links → every failure has an instant alternate path

PARTIAL mesh: only the important pairs get direct links
  e.g. WAN cores — most sites partial-meshed to two hubs
```

| Aspect | Full mesh | Partial mesh |
| --- | --- | --- |
| Redundancy | Highest (any single failure survivable) | Good for designated paths |
| Link count | Explodes with N | Controlled |
| Practical use | Small cores, data-center fabrics | WAN, campus distribution |

## Exam Focus

- **The N×(N−1)/2 formula** is the standard mesh exam number — "how many links for 6 fully meshed routers?"
- Mesh is *the* redundancy topology — referenced by design principles (see [[Network Design Principles]]).
- Modern **[[Spine-Leaf]]** is a *controlled partial mesh* — every leaf to every spine, no leaf-leaf — asked as "why not full mesh?"

## Related Terms

- [[Bus Topology]], [[Star Topology]], [[Ring Topology]], [[Hybrid Topology]], [[Spine-Leaf]]
- Level 02 notes: [[Level 02 - Network Topologies/04. Mesh]]