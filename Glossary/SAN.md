---
tags: [CCNP, glossary, fundamentals, networking, storage]
aliases: ["Storage Area Network"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# SAN

## Definition

A **Storage Area Network (SAN)** is a dedicated high-speed network that connects **servers to shared storage** (disk arrays), moving storage traffic off the client LAN. It is a network built *for* storage traffic, not a general-purpose client network.

## How It Works

```text
servers ── FC (Fibre Channel) / FCoE / iSCSI ──► storage arrays
                     ▲
      separate fabric from the client LAN traffic
```

- **Fibre Channel** SANs use FC switches and fabric zoning (**zoning**, LUN masking) for isolation.
- **iSCSI** runs storage over Ethernet/IP — often isolated on VLANs/[[ACL]]s for security and performance.
- SAN vs NAS: SAN = block storage over a private network; NAS = file storage as a network share.

## Exam Focus

- **SAN classification is by function, not geography** — like [[WLAN]], the exam places it in the "network types by medium/purpose" group.
- Understand it as a *separate* fabric, not "the storage VLAN everyone uses."
- In ENCOR, SAN concepts surface mostly as iSCSI/FCoE awareness and storage segmentation in data-center designs.

## Related Terms

- [[LAN]], [[WAN]], [[VLAN]], [[ACL]]
- Level 00 notes: [[Level 00 - Networking Basics/02. Network Types (LAN, WAN, MAN, PAN, WLAN, SAN, VPN)]]