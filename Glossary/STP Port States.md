---
tags: [CCNP, glossary, stp, switching]
aliases: ["Blocking", "Listening", "Learning", "Forwarding", "Disabled", "STP States"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# STP Port States

## Definition

**STP port states** describe the **current behavioral condition** of a port — what it actually does with frames while it is in that state. They are not the same as [[STP Port Roles]].

## Classic STP (802.1D) States

| State | Sends BPDUs | Learns MACs | Forwards frames |
| --- | :--: | :--: | :--: |
| Blocking | Yes | No | No |
| Listening | Yes | No | No |
| Learning | Yes | Yes | No |
| Forwarding | Yes | Yes | Yes |
| Disabled | No | No | No |

A port normally walks **listening → learning → forwarding** over the [[STP Timers|forward delay]].

## RSTP — 3 States, Not 5

| RSTP state | Collapses classic states |
| --- | --- |
| Discarding | Blocking + Listening + Disabled |
| Learning | Learning |
| Forwarding | Forwarding |

## Exam Focus

- The single most-tested trap: **5 classic states, 3 RSTP states, and "Disabled" is administratively off** (not an STP decision).
- **Alternate/Backup ports sit in *blocking* (RSTP: *discarding*) — they are roles, not states.**
- MAC learning only begins in **Learning** — frames dropped in Blocking/Listening are not learned.

## Related Terms

- [[STP]], [[STP Port Roles]], [[STP Timers]], [[RSTP]], [[PortFast]]
- Level 08 notes: [[Level 08 - STP/08. Port States]]