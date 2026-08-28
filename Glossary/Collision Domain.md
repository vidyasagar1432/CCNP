---
tags: [CCNP, glossary, switching, networking]
aliases: ["Collision Domain"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Collision Domain

## Definition

A **collision domain** is an L2 segment whose devices can **collide** by transmitting simultaneously (half-duplex shared medium). **Switches split collision domains (one per port); hubs/repeaters merge them.** Modern full-duplex links have none (see [[Duplex]]).

## The Classical Table

| Device | Collision domains per port | Broadcast domains |
| --- | --- | --- |
| Hub | 1 shared | 1 |
| Switch | **1 per port** | 1 per [[VLAN]] |
| Router | Boundary — never forwards | Boundary — stops broadcasts |

```text
hub: both PC transmissions can collide → shared CD
switch: each port is its own segment → no collisions (full duplex)
router: ends the L2 segment ([[Broadcast Domain]] boundary too)
```

## Exam Focus

- **"How many collision domains does an 8-port switch create?"** → 8 (one per port) — the arithmetic question.
- Collision domains exist = CSMA/CD needed; switches + full duplex eliminate them.
- "Collision vs broadcast domain" confusion is the classic trap — switches cut collisions, routers cut broadcasts.

## Related Terms

- [[Broadcast Domain]], [[Duplex]], [[Forwarding]], [[Ethernet]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/09. Collision Domains]]