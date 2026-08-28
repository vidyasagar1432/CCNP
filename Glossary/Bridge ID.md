---
tags: [CCNP, glossary, stp, switching]
aliases: ["Bridge Priority", "Extended System ID", "System ID Extension"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# Bridge ID

## Definition

The **Bridge ID** uniquely identifies a switch in a spanning-tree topology and is the **first tie-breaker** in root election and port-role selection. Lower is better.

## Components

| Component | Size | Notes |
| --- | --- | --- |
| Bridge priority | 4 bits (quantum 4096) | 0–61440, configurable step 4096 |
| Extended system ID | 12 bits | Carries the VLAN number (per-VLAN STP) |
| MAC address | 48 bits | Tie-breaker when priority + VLAN are equal |

```text
Bridge ID = Priority | Extended System ID | MAC
             32768       + VLAN 10          + aaaa.bbbb.cccc
```

## How It Works

- Cisco switches run per-VLAN STP, so the effective priority is **TCP priority + VLAN number**:
  - `spanning-tree vlan 10 priority 32768` → effective 32776 for VLAN 10.
- During election, the lowest bridge ID wins → becomes [[Root Bridge]].
- The same bridge ID is carried in every **[[BPDU]]** so all switches agree on the root.

## Exam Focus

- Priority is configured in **multiples of 4096** (default 32768; `root primary` drops it to 24576, `root secondary` to 28672).
- Longer-MAC vs shorter-MAC: when priority and VLAN are identical, the **lower MAC** wins.
- The extended system ID is why the byte order looks odd in `show spanning-tree` output — it embeds the VLAN.

## Related Terms

- [[Root Bridge]], [[BPDU]], [[STP]], [[PVST+]]
- Level 08 notes: [[Level 08 - STP/06. Root Bridge]], [[Level 08 - STP/01. STP]]