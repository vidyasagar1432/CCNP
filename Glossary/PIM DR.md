---
tags: [CCNP, glossary, multicast, routing]
aliases: ["PIM DR", "Designated Router", "PIM Assert", "Assert"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# PIM DR

## Definition

The **PIM Designated Router (DR)** is the one router elected **per multi-access LAN segment** to be the **representative for multicast**: it sends **IGMP host queries** on behalf of the segment and (in sparse mode) is the **forwarder toward the RP** for local sources. Election: **highest IP**, tie-broken by highest IP address. Related: the **Assert** mechanism decides when multiple routers on one LAN forward for the same (S,G) — one winner gets to forward.

## The LAN Mechanics

```text
PIM hellos (224.0.0.13) on the segment → DR election (highest priority/IP wins)
DR jobs: query hosts (IGMP), announce sources to the RP (PIM-SM)
ASSERT: two routers both forwarding the same (S,G) on a LAN →
        assert messages compare metric → loser prunes → ONE forwarder
```

## Exam Focus

- **"Who sends IGMP queries / represents the segment in PIM?" → the DR** — the role definition; election by highest IP (or priority).
- **Assert**: "two routers duplicated multicast on the LAN — what fixes it?" → PIM assert — the dedup mechanism.
- DR is per-LAN (multi-access links ONLY; point-to-point has no DR) — the "when is there no DR?" nuance.
- OSPF DR vs PIM DR confusion: OSPF DR = LSDB efficiency; PIM DR = multicast representation — keep the two "DRs" apart.

## Related Terms

- [[PIM]], [[PIM-SM]], [[IGMP]], [[DR BDR]]
- Level 19 notes: [[Level 19 - Multicast/09. PIM Designated Router (DR) & Assert]]