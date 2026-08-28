---
tags: [CCNP, glossary, stp, switching]
aliases: ["Per-VLAN Spanning Tree Plus", "PVST"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# PVST+

## Definition

**PVST+ (Per-VLAN Spanning Tree Plus)** is Cisco's per-VLAN implementation of spanning tree: it runs a **separate STP instance per VLAN**, so each VLAN can elect its own [[Root Bridge]] and block different ports.

## How It Works

- One [[STP]] instance per active VLAN, each with its own [[Bridge ID]] (which embeds the VLAN via the extended system ID).
- On a trunk, BPDUs are tagged so they carry the right VLAN association across the link.
- Load balancing is possible by design: VLAN 10 blocks one uplink while VLAN 20 blocks the other.

```text
        SW1                 SW2
       /    \              /    \
     fwd   blk           blk   fwd
VLAN 10: uplink A forwards    VLAN 20: uplink B forwards
```

## Rapid PVST+

Applying [[RSTP]] (802.1w) per VLAN gives **Rapid PVST+** — per-VLAN instances with fast convergence. This is the default spanning-tree mode on modern Cisco IOS/IOS XE switches (`spanning-tree mode rapid-pvst`).

## Exam Focus

- **PVST+ ≠ load balancing by itself** — per-VLAN instances *enable* it; the actual blocking/forwarding pattern is still chosen by STP logic per VLAN.
- Each VLAN has its own root and timers; a switch can be root in VLAN 10 and subordinate in VLAN 20.
- Cisco default is **PVST+**; enable rapid mode with `spanning-tree mode rapid-pvst`.

## Related Terms

- [[STP]], [[RSTP]], [[Bridge ID]], [[Root Bridge]], [[MST]]
- Level 08 notes: [[Level 08 - STP/03. PVST+]], [[Level 08 - STP/04. Rapid PVST+]]