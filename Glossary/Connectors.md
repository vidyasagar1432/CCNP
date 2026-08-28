---
tags: [CCNP, glossary, physical, networking]
aliases: ["RJ45", "LC Connector", "SC Connector", "MPO", "Ethernet Connectors"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Connectors

## Definition

**Connectors** terminate the physical medium so it can plug into devices: **RJ45** (8P8C) for copper twisted pair, **LC/SC** for fiber, **MPO/MTP** for parallel optics. Choosing the right connector family matters for density, cost, and polarity.

## The Main Ones

| Connector | Medium | Notes |
| --- | --- | --- |
| RJ45 (8P8C) | Cat5e/6/6a | Copper LAN default |
| LC | Fiber | **Duplex standard** for 1/10/40G (small, high density) |
| SC | Fiber | Legacy simplex/duplex (pushed-pull) |
| MPO/MTP | Fiber | 8/16/24 fibers — 40/100/400G |
| SFP+ cage | Optics | The port-side interface for 10G (see [[Transceiver]]) |

## Exam Focus

- **LC + duplex = the modern fiber answer** for server/switch links; MPO appears with high-speed optical breakout cables.
- RJ45 pinout: T568A/T568B — but **auto-MDIX** makes crossover cables mostly obsolete.
- Connector-speed pairing questions: "10 Gbps copper?" → RJ45, Cat6a; "10 Gbps fiber?" → LC duplex + SFP+.

## Related Terms

- [[UTP]], [[Fiber]], [[Transceiver]], [[Ethernet Standards]]
- Level 01 notes: [[Level 01 - Physical Layer/03. Connectors]]