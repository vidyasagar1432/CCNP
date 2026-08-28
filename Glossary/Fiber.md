---
tags: [CCNP, glossary, physical, networking]
aliases: ["Fiber Optic Cable", "Single-Mode Fiber", "Multi-Mode Fiber", "SMF", "MMF"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Fiber

## Definition

**Fiber optic** cabling carries **light pulses** through a glass core via **total internal reflection**. It beats copper on **distance, bandwidth, EMI immunity, and future-proofing** — at higher component cost.

## Single-Mode (SMF) vs Multi-Mode (MMF)

| | Multi-Mode (MMF) | Single-Mode (SMF) |
| --- | --- | --- |
| Core | 50/62.5 µm | 9 µm |
| Light source | LED/VCSEL (850/1300 nm) | Laser (1310/1550 nm) |
| Reach | 300–550 m (10G) | **Kilometers** (metro/WAN) |
| Cost | Cheaper optics/termination | More expensive |
| Typical use | Campus/Data-center | Long-haul, carrier |

## Exam Focus

- **MMF = short reach, cheap; SMF = long reach, laser** — the pairing drives cable-selection questions.
- **Duplex LC connectors are the Ethernet default**; SC is legacy, MPO/MTP for 40/100G parallel optics (see [[Connectors]]).
- Distance plummets as speed rises on MMF (10G=300 m vs 1G=550 m) — watch the numbers.

## Related Terms

- [[UTP]], [[Transceiver]], [[Connectors]], [[Ethernet Standards]]
- Level 01 notes: [[Level 01 - Physical Layer/01. Cables/03. Fiber]]