---
tags: [CCNP, glossary, switching, networking]
aliases: ["CAM Table", "MAC Address Table", "Content-Addressable Memory"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# CAM Table

## Definition

The **CAM (Content-Addressable Memory) table** — the **MAC address table** — is the hardware Layer-2 forwarding database of a switch: it maps **MAC address + VLAN → egress port**, and it is searched in a single clock cycle (that is what "content-addressable" means).

## How It's Built & Used

```text
entry = { VLAN, MAC, port, (age) }
built by: MAC learning (source MAC of received frames)
used by:  forwarding lookups (dest MAC) → forward / flood / filter
cleared by: aging (default 300s), MAC move, port shutdown
```

- **One entry per (VLAN, MAC, port)**; MACs arriving on a different port **move** the entry.
- CAM is limited by hardware size — **MAC table exhaustion** is an attack/DoS vector (see [[Port Security]]).

## Exam Focus

- **"Which table does a switch use to forward frames?"** → CAM table — the L2 twin of the router FIB.
- **show mac address-table** — expected output format in labs and sims.
- CAM ≠ TCAM: TCAM is used for ACLs/QoS (ternary = 0/1/don't-care); CAM is binary exact-match.

## Related Terms

- [[MAC Learning]], [[MAC Address]], [[Forwarding]], [[Flooding]], [[Filtering]], [[Port Security]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/03. CAM Table]]