---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["Loopback Address", "127.0.0.1", "Loopback Interface", "Loopback"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# Loopback Address

## Definition

The **loopback address** is the host's address **to itself**: IPv4 `127.0.0.0/8` (typically 127.0.0.1), IPv6 `::1`. Packets to loopback never leave the host. The word also names the **loopback interface** — a virtual interface on routers used for stability and management.

## Two Senses You Must Separate

| | Host loopback (127/8) | Router loopback interface |
| --- | --- | --- |
| Purpose | Test the local stack ("is IP working?") | Stable RID / OSPF router-id, management, iBGP source |
| Traffic | Never leaves host | Loopback = always up (unless the router dies) |
| Exam fact | ping 127.0.0.1 = local stack test | `interface loopback 0` |

## Why Router Loopbacks Matter

- **Never goes down** → optimal [[OSPF Router ID]] source and NTP/DNS source.
- iBGP peering over loopbacks (with `update-source`) survives link flaps.
- Known address for management even when physical links change.

## Exam Focus

- **ping 127.0.0.1 tests L1–L3 on the local host** — first step in host-side troubleshooting.
- "Which interface stays up and is best for OSPF router-id?" → loopback — an OSPF-cold-answer.
- Distinguish `127.0.0.1` (host self) from `interface loopback0` (virtual router interface) on questions using the same word.

## Related Terms

- [[IPv4]], [[OSPF Router ID]], [[Management Plane]], [[First Hop Redundancy Protocol]]
- Level 05 notes: [[Level 05 - IPv4/08. Loopback]]