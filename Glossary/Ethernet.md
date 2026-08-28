---
tags: [CCNP, glossary, physical, networking, ethernet]
aliases: ["IEEE 802.3", "Ethernet Standard"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Ethernet

## Definition

**Ethernet (IEEE 802.3)** is the dominant LAN standard: a family of **frame formats, signaling, speeds, and media** from 10 Mbps shared hubs to 400 Gbps switched fabrics. It defines the physical and data-link behavior (frame, addressing with MAC, collision rules) that higher layers rely on.

## The Naming Scheme (see [[Ethernet Standards]])

```text
10      BASE    -T / -SX / -LX / -SR / -LR
^speed (Mbps/Gbps)   ^medium: T=twisted pair, S/L=MMF/SMF, R=PAM signaling
```

## Ethernet Frame (minimum)

| Field | Purpose |
| --- | --- |
| Preamble/SFD | Sync |
| Dst/Src MAC | Addressing |
| Type/Length | EtherType (IPv4 = 0x0800) |
| Payload | 46–1500 bytes (MTU 1500, see [[MTU]]) |
| FCS | CRC error check |

## Exam Focus

- **Ethernet = L1+L2 bundle**: speed/duplex negotiation at L1, framing/MAC at L2.
- The **EtherType 0x0800 (IPv4) / 0x86DD (IPv6)** values are classic picks.
- Half-duplex CSMA/CD is legacy — modern links are full duplex (see [[Duplex]]).

## Related Terms

- [[Ethernet Standards]], [[Duplex]], [[MTU]], [[UTP]], [[Fiber]], [[Connectors]], [[Transceiver]]
- Level 01 notes: [[Level 01 - Physical Layer/02. Ethernet/01. Standards]]