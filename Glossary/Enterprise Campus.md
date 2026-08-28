---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Enterprise Campus Network", "Campus Network"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Enterprise Campus

## Definition

The **enterprise campus** is the full in-building / between-buildings network serving users — plus its **server, WAN, and security modules**. It is **not a single topology**: it is the complete site architecture assembled from many patterns.

## What Belongs to the Campus

```text
CAMPUS = access + distribution + core blocks ([[Three-Tier]] or [[Collapsed Core]])
       + server farm module (sometimes separate DC)
       + WAN edge ([[WAN]] routers, firewalls)
       + management module (NTP, AAA, monitoring)

internally: extended star wiring, EtherChannel uplinks,
            VLANs + [[STP]], FHRP gateways, [[EtherChannel|LACP]] trunks
```

## Exam Focus

- **Campus vs data center**: campus optimizes user coverage (broad, cheap, resilient); DC optimizes east–west capacity ([[Spine-Leaf]]).
- Campus design answers combine topology + [[VLAN]]/[[STP]]/FHRP practices — "the campus design includes…" multi-selects.
- The name "enterprise campus" mostly appears in Cisco reference-architecture questions (CVD).

## Related Terms

- [[Three-Tier]], [[Collapsed Core]], [[Spine-Leaf]], [[LAN]], [[Enterprise Network Architecture]]
- Level 02 notes: [[Level 02 - Network Topologies/09. Enterprise Campus]]