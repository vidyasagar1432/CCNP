---
tags: [CCNP, glossary, stp, switching]
aliases: ["Bridge Protocol Data Unit", "Config BPDU", "TCN BPDU"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# BPDU

## Definition

A **Bridge Protocol Data Unit (BPDU)** is the STP control message exchanged between switches to build and maintain the spanning tree. Without BPDUs, switches would not know the topology — or that it changed.

## BPDU Types

| Type | Purpose |
| --- | --- |
| Configuration BPDU | Advertises root bridge ID, root path cost, sender bridge ID, sender port ID — used for election and role decisions |
| TCN (Topology Change Notification) BPDU | Flags that the topology changed, triggering recalculation |

## Key Fields

- Root bridge ID
- Root path cost / sender's cost to root
- Sender bridge ID ([[Bridge ID]])
- Sender port ID
- Message age, max age, hello, forward delay ([[STP Timers]])

## How They Flow

- **Classic STP**: hello BPDUs sourced from the root every 2 s and relayed (not always flooded) throughout the tree.
- **RSTP**: BPDUs are sent from *every* switch every hello interval, and carry role/state info — enabling fast failure detection.

## Exam Focus

- A **component receiving a BPDU** is by definition STP-capable — hence [[BPDU Guard]] shuts the port down as protection.
- **TCN BPDUs** cause switches to shorten MAC-address aging (forward delay) temporarily — exam-relevant with `show spanning-tree` and topology-change counters.
- BPDUs are sent to the **STP multicast address** `01:80:c2:00:00:00`; PVST+ uses a Cisco-specific extension so VLANs can be identified (see [[PVST+]]).

## Related Terms

- [[STP]], [[Root Bridge]], [[Bridge ID]], [[STP Timers]], [[BPDU Guard]], [[BPDU Filter]], [[Root Guard]], [[Loop Guard]]
- Level 08 notes: [[Level 08 - STP/09. BPDU]]