---
tags: [CCNP, MOC]
aliases: ["Level 04 - Ethernet & Switching"]
status: complete
level: 04
exam: ENCOR-350-401
type: index
---

# Level 04 - Ethernet & Switching

Delves into the Layer 2 fundamentals of Ethernet: MAC addressing, frame structure, and the switching logic of learning, flooding, forwarding, and filtering used to build the CAM table. Also covers broadcast and collision domains, ARP behavior, and a first look at Cisco Express Forwarding.

### Addressing & Frames

1. [[01. MAC Address]] - Layer 2 addressing and its format
2. [[02. Ethernet Frame]] - The structure of an Ethernet frame
3. [[03. CAM Table]] - The content-addressable memory used for forwarding

### Switching Logic

4. [[04. MAC Learning]] - How switches learn source MAC addresses
5. [[05. Flooding]] - Sending unknown unicast and broadcast frames to all ports
6. [[06. Forwarding]] - Delivering frames based on the CAM table
7. [[07. Filtering]] - Dropping frames destined for the source segment

### Domains

8. [[08. Broadcast Domains]] - The boundary of Layer 2 broadcast propagation
9. [[09. Collision Domains]] - Where frames can collide on the wire

### ARP

10. [[10. ARP]] - Address Resolution Protocol for IP-to-MAC resolution
11. [[11. Gratuitous ARP]] - Unsolicited ARP announcements and their uses
12. [[12. Proxy ARP]] - A device answering ARP on behalf of another

### Forwarding Acceleration

13. [[13. CEF Basics]] - Cisco Express Forwarding fundamentals

```
├── 01. MAC Address.md
├── 02. Ethernet Frame.md
├── 03. CAM Table.md
├── 04. MAC Learning.md
├── 05. Flooding.md
├── 06. Forwarding.md
├── 07. Filtering.md
├── 08. Broadcast Domains.md
├── 09. Collision Domains.md
├── 10. ARP.md
├── 11. Gratuitous ARP.md
├── 12. Proxy ARP.md
└── 13. CEF Basics.md
```
