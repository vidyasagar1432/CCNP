---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["IPv4 Address", "IPv4 Addressing", "Internet Protocol Version 4"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# IPv4

## Definition

**IPv4 (Internet Protocol version 4)** is the network-layer protocol that gives every interface a **32-bit address** (4 octets, e.g. `192.168.10.5/24`) used for **end-to-end delivery** across routed networks. It defines addressing, fragmentation, and the packet header — the foundation of today's Internet.

## The Header Essentials

| Field | Meaning |
| --- | --- |
| Version/IHL | 4; header length in 32-bit words |
| TTL | Decremented per hop — 0 = drop (loop protection) |
| Protocol | Payload: 1=ICMP, 6=TCP, 17=UDP |
| Src/Dst | 32-bit addresses |
| Fragmentation | ID/offset/flags — mid-path fragmentation allowed |

## Address Facts

```text
32 bits  →  4,294,967,296 addresses (exhausted → private + NAT + IPv6)
subnet mask / prefix length defines network vs host bits
special ranges: private ([[Private IP]]), loopback, multicast, broadcast
```

## Exam Focus

- **TTL and protocol-field meanings are constant exam trivia** (ICMP=1, TCP=6, UDP=17).
- IPv4 vs [[IPv6]] comparisons: 32 vs 128 bits, broadcast vs multicast/anycast, ARP vs NDP.
- Addressing math lives in [[CIDR]], [[VLSM]], [[Subnet]] skills — IPv4 itself is the header + the address space.

## Related Terms

- [[IPv4 Classes]], [[Private IP]], [[Public IP]], [[APIPA]], [[Loopback Address]], [[CIDR]], [[IPv4 Broadcast]], [[IPv4 Multicast]]
- Level 05 notes: [[Level 05 - IPv4/01. Address Structure]]