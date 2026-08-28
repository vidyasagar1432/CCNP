---
tags: [CCNP, glossary, switching, first-hop]
aliases: ["VRRP", "Virtual Router Redundancy Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: First Hop Redundancy
created: 2026-08-29
---

# VRRP

## Definition

**VRRP (Virtual Router Redundancy Protocol)** is the **open/IEEE 3761 (RFC 9568)** [[First Hop Redundancy Protocol|FHRP]] — Cisco's answer to the multi-vendor need HSRP initially missed. Routers share a **virtual IP** and a **virtual MAC `0000.5e00.01XX`**; one is **Master**, the rest **Backup**. Unique trait: the **virtual IP can be one router's real IP** (the "address owner").

## VRRP vs HSRP at a Glance

| | VRRP | HSRP |
| --- | --- | --- |
| Vendor | Open standard | Cisco proprietary |
| VIP ownership | May be a real router IP (owner) | Always virtual, never a member's |
| Roles | Master / Backup | Active / Standby |
| Virtual MAC | `0000.5e00.01XX` | `0000.0c07.acXX` |
| Hello | 1 s (advertisement), 3 × missed | 3 s / 10 s |
| Transport | IP protocol 112, multicast 224.0.0.18 | UDP 1985, 224.0.0.2 |

## Exam Focus

- **"Which FHRP works across vendors?" → VRRP** — the open-standard answer; "which One has an address owner?" → VRRP.
- Preemption **defaults ON** in VRRP (HSRP defaults OFF) — a favorite inverter.
- Same election logic, different vocabulary: **priority** (255 max, 100 default, owner = 255) decides Master — the numbers are quizzed.

## Related Terms

- [[First Hop Redundancy Protocol]], [[HSRP]], [[GLBP]], [[Object Tracking]]
- Level 14 notes: [[Level 14 - First Hop Redundancy/02. VRRP]]