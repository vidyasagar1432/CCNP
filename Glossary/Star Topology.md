---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Star Topology", "Hub and Spoke", "Star-Wired"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Star Topology

## Definition

**Star** means every device connects **point-to-point to one central device** — historically a hub, in practice a **switch**. It is the physical foundation of modern Ethernet wiring: each host has its own cable back to the wiring closet.

## Why It Won

```text
        host 1
          │
host 2 ── switch ── host 3
          │
        host 4
  central device: hub (shared) or switch (per-port collision domain)
```

| Aspect | Hub-based star | Switch-based star |
| --- | --- | --- |
| Collision domain | One shared | **One per port** |
| Performance | Shared bandwidth | Full-duplex per port |
| Failure | Hub fails = all down | One link fails = that host only |

## Exam Focus

- **Star = the wiring pattern of every modern LAN** — "which topology is a switched LAN?" → star (or extended star), not bus.
- The switch turns star into per-host collision domains and full duplex (see [[Duplex]]).
- Extended star (switches uplinked) is how real campuses scale (see [[Three-Tier|hierarchy]]).

## Related Terms

- [[Bus Topology]], [[Ring Topology]], [[Mesh Topology]], [[Hybrid Topology]], [[LAN]]
- Level 02 notes: [[Level 02 - Network Topologies/02. Star]]