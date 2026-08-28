---
tags: [CCNP, glossary, switching, networking]
aliases: ["Broadcast Domain", "L2 Broadcast"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Broadcast Domain

## Definition

A **broadcast domain** is the set of L2 devices/interfaces that receive a **Layer-2 broadcast** (FF:FF:FF:FF:FF:FF). **Routers stop broadcasts; switches forward them within a VLAN.** A broadcast domain ≈ an unsegmented [[VLAN]].

## How It's Bounded

```text
broadcast sent ──► every port in the SAME VLAN (flooded)
                    routers do NOT forward broadcasts (L3 boundary)
  → one VLAN = one broadcast domain
  → splitting VLANs shrinks the broadcast domain

in the data plane's terms ([[Flooding]]): broadcast = always flooded
```

## Exam Focus

- **"What separates broadcast domains?"** → routers (and VLANs on an L3 boundary). Switches never do.
- **"What separates collision domains?"** → switches. Keep the two separated-in-name questions straight (see [[Collision Domain]]).
- Broadcast storms / too-large domains are why VLANs exist (storm control + segmentation answer).

## Related Terms

- [[Collision Domain]], [[VLAN]], [[Flooding]], [[MAC Address]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/08. Broadcast Domains]]