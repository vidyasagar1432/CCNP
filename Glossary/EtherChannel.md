---
tags: [CCNP, glossary, high-availability, networking]
aliases: ["EtherChannel", "Link Aggregation", "LAG", "Port Channel", "LACP", "PAgP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: High Availability
created: 2026-08-29
---

# EtherChannel

## Definition

**EtherChannel** bundles **parallel physical links into one logical link** — more bandwidth, link-level redundancy, and loop-free simplicity (the bundle is ONE STP port). Negotiation: **LACP (IEEE 802.3ad, standard)** or **PAgP (Cisco)**; static channels also exist. All links must match (speed/duplex/VLANs) and traffic is **load-balanced per flow** (hash on src/dst MAC/IP).

## The Bundle

```text
interfaces gi0/1-4 → channel-group 1 mode active (LACP) → Port-channel1
properties: one logical interface for config/STP; any member failure = automatic failover
load balance: hash of src+dst MAC or IP → flows stick to one link
modes: LACP active/passive | PAgP desirable/auto | on (static)
```

## Exam Focus

- **"What combines links into one logical port?" → EtherChannel** — the definition; bandwidth + redundancy + no STP loop.
- **LACP vs PAgP**: IEEE standard vs Cisco proprietary — the protocol question; modes active/passive vs desirable/auto.
- **Consistency requirements**: same speed/duplex/trunk allowed-VLANs — "why won't the channel form?" troubleshooting.
- **Load balancing**: per-flow hash, not per-packet — the "does a single flow use both links?" trick (no).

## Related Terms

- [[STP]], [[Link Aggregation]], [[Trunk Port]]
- Level 27 notes: [[Level 27 - High Availability/04. Link Redundancy]]