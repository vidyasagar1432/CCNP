---
tags: [CCNP, glossary, physical, networking]
aliases: ["Unshielded Twisted Pair", "Cat5e", "Cat6", "Cat6a"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# UTP

## Definition

**Unshielded Twisted Pair (UTP)** is the dominant copper LAN cabling: four twisted pairs of wire carrying signals **differentially**. Twisting + balanced signaling cancels noise (crosstalk/EMI) without needing shields, keeping cost low.

## Categories That Matter

| Category | Rate | Use |
| --- | --- | --- |
| Cat5e | 1 Gbps | Common legacy LAN |
| Cat6 | 1 Gbps (10 Gbps ≤ 55 m) | Standard new installs |
| Cat6a | 10 Gbps (100 m) | Data-center / 10G runs |
| Cat7/8 | 10/40 Gbps | Specialized, shielded |

## Exam Focus

- **Category = speed/length limit** — "which cable for 10 Gbps over 80 m?" → Cat6a+.
- UTP max segment for Ethernet = **100 m** (90 m solid + 10 m patch) — a classic exam number.
- **T568A/T568B pinouts** and straight-through vs crossover: modern gear auto-MDIX nullifies the old crossover rule.

## Related Terms

- [[Shielded Twisted Pair]], [[Ethernet]], [[Connectors]], [[Ethernet Standards]]
- Level 01 notes: [[Level 01 - Physical Layer/01. Cables/01. UTP]]