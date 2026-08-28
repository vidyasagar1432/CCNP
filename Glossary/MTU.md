---
tags: [CCNP, glossary, physical, networking]
aliases: ["Maximum Transmission Unit"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# MTU

## Definition

**MTU (Maximum Transmission Unit)** is the largest **IP packet** an interface can send in one frame — **1500 bytes** for standard Ethernet (the frame adds ~18 bytes of L2 overhead). Packets larger than the path MTU must be fragmented — or dropped if DF is set.

## How It Works

```text
L3 packet ≤ MTU ──► fits in one Ethernet frame (payload ≤ 1500)
L3 packet  > MTU ──► fragment (IPv4) or drop with ICMP PTB (IPv6, DF)
path MTU (PMTUD) discovers the smallest MTU across the route
```

| Link | Typical MTU |
| --- | --- |
| Ethernet | 1500 |
| Jumbo frames (switched LAN) | 9000 |
| PPPoE (DSL) | 1492 |
| GRE/IPsec tunnel | 1400–1460 (overhead) |

## Exam Focus

- **The 1500 default is the anchor**; tunneling lowers it (GRE/IPsec overhead) — "why can't I ping over the VPN with 1500?" → MTU.
- **IPv6 requires fragmentation only by the source**; path MTU discovery uses ICMPv6 "Packet Too Big" — if ICMP is filtered, traffic dies silently.
- Jumbo frames need **end-to-end** support: one 1500-MTU link and 9000-MTU traffic = fragmentation or drops.

## Related Terms

- [[Ethernet]], [[Ethernet Standards]], [[Fiber]]
- Level 01 notes: [[Level 01 - Physical Layer/02. Ethernet/04. MTU]]