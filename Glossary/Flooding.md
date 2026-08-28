---
tags: [CCNP, glossary, switching, networking]
aliases: ["L2 Flooding", "Unknown Unicast Flood"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Flooding

## Definition

**Flooding** is the L2 behavior of sending a frame **out every port in the same VLAN except the ingress port** — when the destination MAC is **unknown** (not in the [[CAM Table]]), or the frame is a **broadcast** (or flooded multicast).

## When a Switch Floods

| Frame type | Action |
| --- | --- |
| Dest MAC in CAM (unicast) | [[Forwarding|Forward]] out that port only |
| Dest MAC unknown (unicast) | **Flood** (learned later when the host replies) |
| Dest = FF:FF:FF:FF:FF:FF (broadcast) | Flood |
| Dest = multicast & not filtered | Flood (or IGMP snooping limits it) |

```text
unknown-dest unicast flooding is the "learning bootstrap"
  → the reply comes back → MAC learned → subsequent frames forward
```

## Exam Focus

- **Flooding ≠ broadcast**: flooding can send *unicast* frames to all ports; broadcast is only the all-ones destination.
- Flooding wastes bandwidth — the *why* behind VLANs ([[Broadcast Domain]] size) and [[IGMP Snooping]].
- "How does a switch learn MACs?" → by flooding the unknown destination until the host answers.

## Related Terms

- [[CAM Table]], [[MAC Learning]], [[Forwarding]], [[Filtering]], [[Broadcast Domain]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/05. Flooding]]