---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Hybrid Topology", "Tree Topology"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Hybrid Topology

## Definition

A **hybrid topology** combines two or more base topologies — [[Bus Topology|bus]], [[Star Topology|star]], [[Ring Topology|ring]], [[Mesh Topology|mesh]], tree — into one network. **Real networks are almost always hybrids**: the term means "this network is a mix, not a pure textbook geometry."

## Typical Example

```text
extended star (switches uplinked = "tree")
        │
        └── partial mesh between core switches
        └── ring trick at the fiber plant (redundant path)
```

- Campus: star/access + partial-mesh core = hybrid.
- WAN: hub-and-spoke (star) + partial mesh between regional hubs.
- Data center: [[Spine-Leaf]] + top-of-rack stars.

## Exam Focus

- **The exam asks "which pure topology is this?" knowing the answer is often 'hybrid'** — don't force one geometry onto a real drawing.
- The useful skill is spotting the *dominant* pattern (star wiring) while noting mesh redundancy links.
- Remember: topology choice is a **[[Network Design Principles|design-principle]] decision** (cost, redundancy, failure domain).

## Related Terms

- [[Bus Topology]], [[Star Topology]], [[Ring Topology]], [[Mesh Topology]], [[Spine-Leaf]], [[Enterprise Campus]]
- Level 02 notes: [[Level 02 - Network Topologies/05. Hybrid]]