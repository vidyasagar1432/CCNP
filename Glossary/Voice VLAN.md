---
tags: [CCNP, glossary, switching, vlan]
aliases: ["Voice VLAN", "VOICE VLAN", "Auxiliary VLAN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# Voice VLAN

## Definition

A **voice VLAN** is a dedicated VLAN for **IP-phone traffic**, separated from data. The switch port **auto-assigns** the phone to the voice VLAN by recognizing **CDP** (Cisco) or LLDP-MED, while the PC behind the phone stays in the data VLAN. The phone's frames are **802.1Q-tagged**; typical data frames stay untagged.

## The Dual-Purpose Port

```text
switchport mode access
switchport access vlan 10        ← data (untagged for the PC behind)
switchport voice vlan 20         ← phone (tagged with VLAN 20)

phone uses 802.1Q tag 20 for its voice traffic
PC behind the phone uses untagged → data VLAN 10
(CDP tells the phone which VLAN to tag; LLDP-MED works too)
```

## Why QoS Pairing Matters

- Voice is delay-sensitive, data is not ([[QoS]] marks: voice EF 46, then trust).
- **Auto QoS / trust boundaries**: the port trusts the phone's marking, but *re-classifies* the PC's.
- PoE: phones ride the same cable ([[Power over Ethernet]] ties in).

## Exam Focus

- **"Which VLAN carries VoIP on an access port?" → the voice VLAN** — remember the phone TAGS with 802.1Q; data is untagged.
- `switchport voice vlan <n>` — the command to recognize; CDP advertises it.
- Voice VLAN is also a security target: DHCP snooping + IP source guard often applied to phones/PCs.

## Related Terms

- [[VLAN]], [[Access Port]], [[802.1Q]], [[QoS]]
- Level 07 notes: [[Level 07 - VLAN Technologies/02. Voice VLAN]]