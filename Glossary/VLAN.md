---
tags: [CCNP, glossary, switching, vlan]
aliases: ["VLAN", "Virtual LAN", "Virtual Local Area Network"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# VLAN

## Definition

A **VLAN (Virtual LAN)** is a logical Layer-2 segmentation of a switch: ports in the same VLAN form **one [[Broadcast Domain|broadcast domain]]**, regardless of physical location, while frames tagged/assigned to different VLANs are isolated at L2. VLANs = security, efficiency, and broadcast control — the same thing separate physical switches used to buy.

## What a VLAN Actually Segments

```text
broadcast domain  → now VLAN-scoped (not switch-scoped)
security          → hosts in VLAN 10 can't L2-talk to VLAN 20 (unless routed)
efficiency        → smaller broadcast domains = less unnecessary flooding
flexibility       → users regrouped by function, not by location
```

| VLAN | Typical name | Purpose |
| --- | --- | --- |
| 1 | default | everything starts here — avoid for user traffic |
| 10 | DATA | user PCs |
| 20 | VOICE | IP phones ([[Voice VLAN]]) |
| 100 | MGMT | management (see [[Management Plane]]) |

## Exam Focus

- **"VLAN separates what?" → broadcast domains** (NOT collision domains — that's ports/[[Duplex]]).
- Inter-VLAN traffic must go through a **Layer-3 device** → [[Inter-VLAN Routing]] (SVI or subinterfaces).
- **VLAN 1 default**: untagged, carries CDP/VTP; best practice: move everything off VLAN 1. Trunks need pruning/security ([[Trunk Port]]).

## Related Terms

- [[Broadcast Domain]], [[Access Port]], [[Trunk Port]], [[Native VLAN]], [[802.1Q]], [[Inter-VLAN Routing]], [[Private VLAN]]
- Level 07 notes: [[Level 07 - VLAN Technologies/01. VLAN]]