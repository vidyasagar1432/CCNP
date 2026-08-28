---
tags: [CCNP, glossary, switching, networking]
aliases: ["Ethernet Frame", "Frame Format", "Ethernet II"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Ethernet Frame

## Definition

An **Ethernet frame** is the **Layer 2 PDU** that transports upper-layer protocols ([[IPv4]], [[IPv6]], [[ARP]]) across Ethernet. The de facto format is **Ethernet II (DIX)**: addressing, EtherType, payload, and error check.

## Layout

```text
| Preamble 7B | SFD 1B | Dst MAC 6B | Src MAC 6B | Type 2B | Payload 46–1500B | FCS 4B |
```

| Field | Purpose |
| --- | --- |
| Dst/Src MAC | L2 delivery (see [[MAC Address]]) |
| EtherType | Payload protocol: **0x0800 = IPv4, 0x86DD = IPv6, 0x0806 = ARP** |
| Payload | 46–1500 bytes (min size with padding; see [[MTU]]) |
| FCS | CRC-32 — errors detected, frames dropped |

## Exam Focus

- **EtherType values are guaranteed trivia**: 0x0800 / 0x86DD / 0x0806.
- 802.3 "Length" vs Ethernet II "Type" distinction (length fields were pre-EtherType) is a classic walk-the-line question.
- **Min frame 64 bytes, max 1518** (without preamble/FCS); jumbo = bigger [[MTU]] payloads on switched LANs.

## Related Terms

- [[MAC Address]], [[MTU]], [[Encapsulation]], [[PDU]], [[MAC Learning]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/02. Ethernet Frame]]