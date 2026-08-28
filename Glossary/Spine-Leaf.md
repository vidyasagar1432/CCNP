---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Spine-Leaf Architecture", "Leaf Switch", "Spine Switch", "CLOS"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Spine-Leaf

## Definition

**Spine-leaf** is the modern data-center/enterprise switching architecture: every **leaf** (top-of-rack) switch connects to **every spine** switch, and **no leaf connects to another leaf**. It is a non-blocking, predictable partial mesh — the practical successor to the classical **[[Three-Tier|campus three-tier]]** for east–west traffic.

## How It Works

```text
        spine 1        spine 2        spine 3
       /  |  \        /  |  \        /  |  \
     L1  L2  L3     L1  L2  L3     L1  L2  L3      (leaves = ToR)
  traffic leaf→leaf always crosses exactly one spine
  → predictable latency + equal path count to every destination
```

- **Scale-out**: add spines or leaves for more capacity/fanout — linear growth, no re-design.
- **No leaf-to-leaf links by design** — east–west traffic never shortcuts (loop-free by construction, no STP drama).
- Often paired with **BGP/EVPN or VXLAN** overlays and anycast gateways.

## Exam Focus

- **"Why spine-leaf over three-tier?"** → predictable east–west performance, equal-cost paths, linear scale, no oversubscription surprises.
- The exam contrasts: **spine-leaf (data center) vs core/distribution/access (campus)** — each has its place.
- The "no leaf-leaf links" line is the single most-tested spine-leaf fact.

## Related Terms

- [[Three-Tier]], [[Enterprise Campus]], [[Mesh Topology]], [[Enterprise Network Architecture]]
- Level 02 notes: [[Level 02 - Network Topologies/06. Spine-Leaf]]