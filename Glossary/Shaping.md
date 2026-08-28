---
tags: [CCNP, glossary, qos, networking]
aliases: ["Shaping", "Traffic Shaping", "GTS", "Shaped Rate", "Bc Be"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# Shaping

## Definition

**Shaping** smooths traffic toward a rate by **buffering excess** and releasing it later — **egress-only**, and it **adds delay** (the buffer). Where [[Policing]] drops, shaping holds. Ideal for aligning bursts to a **subscribed line rate** (e.g. a 10 Mbps circuit from a 1 Gbps handoff) or when **dropping is unacceptable** (TCP would just retransmit). Uses the same token-bucket math (CIR/Bc/Be).

## Shaping vs Policing

| Aspect | Policing | Shaping |
| --- | --- | --- |
| Excess handling | Drop / remark | Buffer & delay |
| Interfaces | Ingress + egress | Egress only |
| Latency added | No | Yes (buffering) |
| Output profile | Bursty | Smooth |
| Best fit | Access/ingress limits | Subscribed rates / slow links |

## Exam Focus

- **"Which mechanism buffers instead of drops?" → shaping** — the definition; egress-only constraint.
- **Why shape but not police on a WAN edge?** → no retransmit storms; jitter-tolerant; matches carrier CIR — the scenario.
- Token bucket on shaping: Bc/Be define burst per Tc — the math spot.
- Shaping applies to a class (CB-Shaping) or a whole interface (rate-limit style) — the config variants.

## Related Terms

- [[Policing]], [[MQC]], [[Queuing]]
- Level 21 notes: [[Level 21 - QoS/04. Shaping]]