---
tags: [CCNP, glossary, wan, networking]
aliases: ["Broadband", "Broadband Access", "DSL", "Cable", "FTTH"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# Broadband

## Definition

**Broadband** WANs ride **DSL, cable, or fiber (FTTH/GPON)** over a **shared access network** — cheap, ubiquitous, but **asymmetric, contended, and best-effort**. The enterprise uses it as the **inexpensive transport or backup** under the [[SD-WAN]] architecture, almost always with **[[PPPoE]]** (or IPoE) as the session/auth/IP-delivery layer and a simple **DHCP**-assigned addressing model.

## The Reality Check

```text
DSL: phone-line plant, asymmetric (down >> up), distance-sensitive
cable: HFC plant, shared neighborhood node, speed varies by load
FTTH: fiber to the home, best of the three (symmetric options)
carrier-grade NAT / dynamic IPs happen → VPNs need NAT traversal
```

## Exam Focus

- **"What transport is cheapest but contended?" → broadband** — the trade-off; vs [[MPLS WAN|MPLS]] (SLA) — the decision contrast.
- **PPPoE is the typical session layer over DSL** — the pairing (see [[PPPoE]]).
- Asymmetry + contention → why QoS/bandwidth math differs per direction — the design nuance.
- In SD-WAN, broadband = one of many underlay transports (and often the backup) — the integration answer ([[SD-WAN]]).

## Related Terms

- [[PPPoE]], [[DHCP]], [[SD-WAN]], [[Metro Ethernet]], [[LTE]]
- Level 23 notes: [[Level 23 - Enterprise WAN/05. Broadband]]