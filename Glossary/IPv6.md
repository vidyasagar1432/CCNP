---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["IPv6", "IPv6 Address", "Internet Protocol Version 6"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# IPv6

## Definition

**IPv6** is the network-layer protocol with **128-bit addresses**, designed to replace IPv4: nearly unlimited space, **no broadcast (multicast/anycast instead)**, mandatory security/auto-config, and built-in support for modern routing. It is a **different protocol, not a bigger IPv4** — headers, neighbor discovery, and address categories all changed.

## The 128-Bit Address

- Written as **8 groups of 4 hex digits**: `2001:db8:1:2::10/64` (double-colon compresses one run of zeros).
- Structure: global prefix + subnet + interface ID — but scope categories matter more:

| Category | Prefix | Analogy |
| --- | --- | --- |
| [[Global Unicast]] | 2000::/3 | Public IPv4 |
| [[Link Local]] | fe80::/10 | Auto, per-link |
| [[Unique Local]] | fc00::/7 | Private (RFC 1918) |
| [[IPv6 Multicast]] | ff00::/8 | Class D |
| [[Anycast]] | (from unicast space) | New concept |

## Exam Focus

- **No broadcast exists in IPv6** — "all-nodes" multicast (ff02::1) replaces ARP-broadcast.
- [[Neighbor Discovery|NDP]] replaces ARP; fragment-only-at-source (no mid-path fragmentation).
- IPv4/IPv6 coexistence exam angles: dual-stack, tunneling ([[GRE]], [[IPsec]]), translation.

## Related Terms

- [[IPv4]], [[Global Unicast]], [[Link Local]], [[Unique Local]], [[IPv6 Multicast]], [[Anycast]], [[SLAAC]], [[Neighbor Discovery]]
- Level 06 notes: [[Level 06 - IPv6/01. IPv6 Addressing]]