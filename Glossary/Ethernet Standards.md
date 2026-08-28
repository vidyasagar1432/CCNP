---
tags: [CCNP, glossary, physical, networking, ethernet]
aliases: ["Ethernet Naming Scheme", "100BASE-TX", "1000BASE-T", "10GBASE-T", "Gigabit Ethernet"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Ethernet Standards

## Definition

**Ethernet standards (IEEE 802.3 sub-amendments)** encode **speed–signaling–medium** in one name: e.g. **1000BASE-T** = 1 Gbps, BASEband signaling, twisted pair. Decoding the name answers "what cable/optics and what cap?"

## Decoder

```text
<speed><BASE><medium>
1000   BASE  T   = 1 Gbps, baseband, copper (UTP)
10G    BASE  SR  = 10 Gbps, short-reach multimode (SR=MMF 850nm)
10G    BASE  LR  = 10 Gbps, long-reach single-mode
100    BASE  FX  = 100 Mbps fiber
```

| Name | Speed | Medium | Max length |
| --- | --- | --- | --- |
| 10BASE-T | 10 Mbps | Cat3+ UTP | 100 m |
| 100BASE-TX | 100 Mbps | Cat5 UTP | 100 m |
| 1000BASE-T | 1 Gbps | Cat5e+ | 100 m |
| 10GBASE-T | 10 Gbps | Cat6a | 100 m (55 m on Cat6) |
| 10GBASE-SR | 10 Gbps | MMF | 300 m (OM3) |
| 10GBASE-LR | 10 Gbps | SMF | 10 km |

## Exam Focus

- **Decode-don't-memorize**: the suffix (T/SR/LR/ER) reveals medium and reach — exam questions give a name and ask "which cable/optics?"
- "Which standard for 10 Gbps over 80 m of copper?" → **10GBASE-T + Cat6a** (not SFP+ optics).
- The standard family name to quote is always **IEEE 802.3**.

## Related Terms

- [[Ethernet]], [[UTP]], [[Fiber]], [[Transceiver]], [[Duplex]]
- Level 01 notes: [[Level 01 - Physical Layer/02. Ethernet/01. Standards]]