---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Wide Area Network"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# WAN

## Definition

A **Wide Area Network (WAN)** connects **geographically distant sites** — cities, states, countries — usually by leasing capacity from a service provider. WAN links are the **expensive, slower, provider-managed** edges between a company's [[LAN|LANs]].

## Key Characteristics

| Aspect | WAN |
| --- | --- |
| Scope | Metro → intercity → international |
| Ownership | Provider's transport (leased lines, MPLS, Internet VPN) |
| Cost/latency | Higher cost, higher latency than LAN |
| Technologies | MPLS, point-to-point, Internet/[[VPN]] (IPsec, DMVPN, SD-WAN) |
| Speed | Typically lower and asymmetric vs campus LAN |

## How It Relates

- WAN links connect sites whose LANs are designed identically (hierarchical campuses).
- Modern enterprise WAN = **[[SD-WAN]]** / DMVPN over the Internet (see [[Level 23 - Enterprise WAN]]), replacing expensive private circuits.
- WAN traffic engineering relies on routing protocols and [[QoS]] to survive limited bandwidth.

## Exam Focus

- **WAN vs LAN distinction** — scope, ownership, and performance appear in scenario questions ("which technology for a two-branch company?").
- WAN is the provider-managed piece; **the enterprise still owns its LAN edge**.
- In ENCOR the WAN theme is SD-WAN architecture and VPN flavors — know MPLS and Internet-based options.

## Related Terms

- [[LAN]], [[MAN]], [[VPN]], [[MPLS]], [[Enterprise Network Architecture]]
- Level 00 notes: [[Level 00 - Networking Basics/02. Network Types (LAN, WAN, MAN, PAN, WLAN, SAN, VPN)]]