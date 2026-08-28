---
tags: [CCNP, glossary, physical, networking]
aliases: ["SFP", "SFP+", "QSFP", "Optics", "GBIC"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Transceiver

## Definition

A **transceiver** (optic module) converts the switch/router port's electrical signaling into **light (fiber)** or copper signaling — e.g., **SFP (1G)**, **SFP+ (10G)**, **QSFP/QSFP28 (40/100G)**. The module type dictates reach and media, independent of the port.

## The Family

| Module | Speed | Common optics |
| --- | --- | --- |
| SFP | 1 Gbps | 1000BASE-T (copper RJ45), SX (MMF 550 m), LX (SMF 10 km) |
| SFP+ | 10 Gbps | 10GBASE-SR (MMF 300 m), LR (SMF 10 km) |
| QSFP+ / QSFP28 | 40 / 100 Gbps | SR4/LR4, MPO or LC breakout |

## How It Works

```text
port (fixed) ── SFP/SFP+ module ── fiber/copper patch to the far end
swap the module → change the medium/reach without changing the switch
```

- Modules are **port-agnostic**: the same 10G switch port runs SR (short) or LR (long) depending on the optic.
- **DBOM/DDM** telemetry reads temperature/laser power; dirty or weak optics show as link flaps / FCS errors.
- "Optics mismatch" (e.g., LR fiber but SR module at the far end) = link up, high errors or no light.

## Exam Focus

- **Module = reach/fiber-type decision point**: "access switch to core, 200 m MMF, 10G" → SFP+ with 10GBASE-SR.
- Link-flap symptoms often trace to **dirty/damaged optics or power budget** — expect a "check the SFP light levels" answer.
- Never forget duplex LC fiber with LC-transceiver optics.

## Related Terms

- [[Fiber]], [[Connectors]], [[Ethernet Standards]], [[Ethernet]]
- Level 01 notes: [[Level 01 - Physical Layer/04. Transceivers]]