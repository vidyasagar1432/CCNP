---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Ring Topology", "Token Ring", "FDDI"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Ring Topology

## Definition

In a **ring topology** every device connects to **exactly two neighbors**, forming a closed loop; frames travel in one direction (Token Ring, FDDI). Access is controlled by a **token** — only the token holder transmits, which prevents collisions but adds latency.

## How It Works

```text
device A ──► device B ──► device C
   ▲                        │
   └────────device D ◄──────┘
  token circulates; each node retransmits; broken ring = dead network
  (FDDI dual ring adds a backup counter-rotating ring)
```

| Trait | Token Ring / FDDI |
| --- | --- |
| Access | Token passing (no collisions) |
| Fault | Single break kills the ring (FDDI self-heals via second ring) |
| Status | Legacy — replaced by switched [[Ethernet]] star |

## Exam Focus

- **"No collisions thanks to token passing"** is the defining exam fact of ring.
- Recognize FDDI's **dual counter-rotating ring** as its resilience mechanism.
- The topology ladder question still asks: star, bus, ring, mesh — one-line definitions each.

## Related Terms

- [[Bus Topology]], [[Star Topology]], [[Mesh Topology]], [[Hybrid Topology]]
- Level 02 notes: [[Level 02 - Network Topologies/03. Ring]]