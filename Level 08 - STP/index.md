---
tags: [CCNP, MOC]
aliases: ["Level 08 - STP"]
status: complete
level: 08
exam: ENCOR-350-401
type: index
---

# Level 08 - STP

Covers Spanning Tree Protocol and its variants — RSTP, PVST+, Rapid PVST+, and MST — that prevent Layer 2 loops. Includes the mechanics of root bridge election, port roles and states, BPDUs, and the protection features like PortFast, BPDU Guard, Root Guard, and Loop Guard, plus EtherChannel link aggregation.

### Spanning Tree Protocols

1. [[01. STP]] - Classic 802.1D spanning tree operation
2. [[02. RSTP]] - Rapid Spanning Tree Protocol (802.1w)
3. [[03. PVST+]] - Per-VLAN Spanning Tree Plus
4. [[04. Rapid PVST+]] - Per-VLAN rapid spanning tree
5. [[05. MST]] - Multiple Spanning Tree (802.1s)

### STP Mechanics

6. [[06. Root Bridge]] - Root bridge election and placement
7. [[07. Port Roles]] - Root, designated, and blocking roles
8. [[08. Port States]] - Listening, learning, forwarding, blocking, disabled
9. [[09. BPDU]] - Bridge Protocol Data Units

### STP Protection

10. [[10. PortFast]] - Fast transition for access ports
11. [[11. BPDU Guard]] - Shutting down ports receiving unexpected BPDUs
12. [[12. Root Guard]] - Preventing rogue root bridge election
13. [[13. Loop Guard]] - Detecting unidirectional link failures

### Link Aggregation

14. [[14. EtherChannel/01. LACP]] - IEEE 802.3ad link aggregation
15. [[14. EtherChannel/02. PAgP]] - Cisco proprietary port aggregation
16. [[14. EtherChannel/03. Static]] - Statically configured EtherChannel

```
├── 14. EtherChannel/
│       ├── 01. LACP.md
│       ├── 02. PAgP.md
│       └── 03. Static.md
├── 01. STP.md
├── 02. RSTP.md
├── 03. PVST+.md
├── 04. Rapid PVST+.md
├── 05. MST.md
├── 06. Root Bridge.md
├── 07. Port Roles.md
├── 08. Port States.md
├── 09. BPDU.md
├── 10. PortFast.md
├── 11. BPDU Guard.md
├── 12. Root Guard.md
└── 13. Loop Guard.md
```
