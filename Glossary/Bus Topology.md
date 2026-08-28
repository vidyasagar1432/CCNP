---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Bus Topology", "10BASE2", "10BASE5"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Bus Topology

## Definition

In a **bus topology**, all devices share a **single transmission medium** — originally a coaxial backbone (10BASE2 "thinnet" / 10BASE5 "thicknet"). Every frame travels the whole segment; every device hears it. A Bus network is one shared **collision and broadcast domain**.

## Characteristics

```text
device ─ device ─ device ─ device ─ device          (one shared wire)
 Terminators on both ends; one broken link splits the network
```

| Trait | Value |
| --- | --- |
| Media | One shared coaxial segment |
| Collision domain | One big (CSMA/CD at 10 Mbps) |
| Failure mode | **Single break = whole segment down** |
| Status | Legacy/historical |

## Exam Focus

- **Common collision + broadcast domain** and single-point-of-failure are the two exam points.
- Identified in questions via "coaxial", "terminators", "10BASE2/10BASE5".
- Contrast with [[Star Topology]] (the modern Ethernet replacement): hub/switch centralizes the failure point but isolates per-link faults with switches.

## Related Terms

- [[Star Topology]], [[Ring Topology]], [[Mesh Topology]], [[Hybrid Topology]], [[Ethernet]]
- Level 02 notes: [[Level 02 - Network Topologies/01. Bus]]