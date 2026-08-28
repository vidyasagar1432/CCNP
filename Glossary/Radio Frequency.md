---
tags: [CCNP, glossary, physical, networking]
aliases: ["Radio Frequency", "RF", "RF Signal"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Radio Frequency

## Definition

**Radio frequency (RF)** is the electromagnetic wave medium used by wireless links — from Wi-Fi (2.4/5/6 GHz) to cellular and microwave. At the physical layer, RF replaces a cable with modulated RF waves shared over the air.

## Physical-Layer Behavior That Matters

- **Shared, half-duplex medium**: only one client should talk per channel at a time (CSMA/CA in 802.11).
- **Signal degradation**: attenuation, reflection, absorption, and **interference** from other transmitters.
- **Range vs throughput**: higher bands (5/6 GHz) = more capacity but shorter range; 2.4 GHz penetrates walls better but suffers more contention.
- Regulatory bands differ by region (channels 1–11 vs 1–13, DFS).

## Exam Focus

- **"Why does wireless slow down?"** usually comes back to RF: interference, co-channel overlap, retries.
- RF fundamentals feed the [[WLAN]]/Wi-Fi level directly — know the 2.4 vs 5/6 GHz trade-off table.
- Physical layer "wireless vs wired" comparisons: RF has no 100%-duplex guarantee.

## Related Terms

- [[WLAN]], [[Fiber]], [[UTP]]
- Level 01 notes: [[Level 01 - Physical Layer/01. Cables/04. Wireless]]