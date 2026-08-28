---
tags: [CCNP, glossary, wan, networking]
aliases: ["Metro Ethernet", "E-LINE", "E-LAN", "E-TREE", "Ethernet Service"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# Metro Ethernet

## Definition

**Metro Ethernet** delivers **WAN connectivity using Ethernet services** across a metro/SP network — cheap, fast, simple, and familiar. Standard service types (MEF): **E-LINE** (point-to-point virtual circuit), **E-LAN** (multipoint/broadcast, like a giant switch), **E-TREE** (hub-and-spoke). It can be pure **L2** (customer keeps L3) or ride an **[[MPLS VPN|L3VPN]]** (SP does the routing).

## Service Menu

| Service | Shape | Use |
| --- | --- | --- |
| E-LINE (EVPL) | P2P Ethernet circuit | Site-to-site, like a leased line |
| E-LAN | Multipoint | Full mesh sites, broadcast domain |
| E-TREE | Hub + spokes | Hub-and-spoke / broadcast-video trees |

## Exam Focus

- **"Which Ethernet WAN service connects two sites?" → E-LINE**; "many-to-many?" → E-LAN — the service-matching questions.
- **Metro Ethernet = L2 extension**: STP/loops, broadcast domains stretch — the "danger of running spanning-tree across a WAN" scenario.
- **EVPL/E-LAN on provider** = VLAN-tagged services — the VLAN interplay.
- Metro Ethernet vs MPLS WAN: Layer 2 simplicity vs Layer 3 services — the provider-choice question.

## Related Terms

- [[Ethernet]], [[VLAN]], [[MPLS VPN]], [[WAN]]
- Level 23 notes: [[Level 23 - Enterprise WAN/03. Metro Ethernet]]