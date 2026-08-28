---
tags: [CCNP, glossary, switching, vlan]
aliases: ["Access Port", "Access VLAN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# Access Port

## Definition

An **access port** carries traffic for **exactly ONE VLAN** (untagged) and connects to an **end host** — PC, printer, phone (via [[Voice VLAN]]). Everything entering an access port is assumed to belong to that VLAN; no tag is expected or honored.

## Access vs Trunk — the Core Distinction

| | Access port | [[Trunk Port]] |
| --- | --- | --- |
| VLANs | 1 (data) (+ optional voice) | Many (all or allowed list) |
| Tagging | Untagged | 802.1Q tagged (except [[Native VLAN]]) |
| Peer | End host (PC/phone/camera) | Switch/router |
| Command | `switchport mode access` | `switchport mode trunk` |

```text
switchport mode access
switchport access vlan 10        ← single VLAN assignment
switchport voice vlan 20         ← phone rides along (tagged)
```

## Exam Focus

- **"Which port type serves a single PC?" → access** — determinism and security (DHCP snooping, port-security, storm control all start at access ports).
- **"What happens if a tag arrives on an access port?"** → it's dropped or treated per config — the "trunk must be on both sides" trap question.
- Related: **PortFast** — access ports skip STP listening/learning (no loops possible from a single host) → faster boot (see [[STP]]).

## Related Terms

- [[VLAN]], [[Trunk Port]], [[Native VLAN]], [[Voice VLAN]], [[802.1Q]]
- Level 07 notes: [[Level 07 - VLAN Technologies/04. Access Port]]