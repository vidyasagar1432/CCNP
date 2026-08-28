---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Local Area Network"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# LAN

## Definition

A **Local Area Network (LAN)** is a network confined to a **small geographic area** — a home, office, floor, or campus building — typically owned by a single organization. It offers **high bandwidth, low latency**, and is the unit across which [[EtherChannel|Ethernet]] switching and VLANs (see [[VLAN]]) operate.

## Key Characteristics

| Aspect | LAN |
| --- | --- |
| Scope | Single site / building / campus (< ~1–2 km of premises cabling) |
| Ownership | One organization (you own the switches, cables, design) |
| Speed/latency | High bandwidth, low delay |
| Addressing | Private [[IPv4|IPv4]]/[[IPv6]] space typical |
| Failure domain | Small, bounded (good default per fault domain) |

## How It Relates

- Many LANs are bridged/switched domains ([[Level 04 - Ethernet & Switching]]) with VLAN segmentation.
- A LAN connects to the outside via a **[[WAN]]** at an edge router.
- Modern campus LANs use the hierarchical [[Enterprise Network Architecture|core/distribution/access]] design.

## Exam Focus

- Know the **scope-based classification ladder**: [[PAN]] → LAN → **MAN** → **WAN** — the exam tests "what scale is a MAN vs LAN" edge cases.
- The exam contrasts LAN (you control everything) with WAN (provider-managed transport between sites).

## Related Terms

- [[WAN]], [[MAN]], [[PAN]], [[WLAN]], [[IPv4]], [[VLAN]]
- Level 00 notes: [[Level 00 - Networking Basics/02. Network Types (LAN, WAN, MAN, PAN, WLAN, SAN, VPN)]]