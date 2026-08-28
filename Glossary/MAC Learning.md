---
tags: [CCNP, glossary, switching, networking]
aliases: ["MAC Learning", "CAM Learning"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# MAC Learning

## Definition

**MAC learning** is how a switch builds its **[[CAM Table|MAC address table]]**: it inspects the **source MAC** of every received frame and records `{VLAN, source-MAC → ingress port}`, with an aging timer.

## The Algorithm (per received frame)

```text
1. look up (VLAN, src-MAC) in CAM
2. not found   → add entry (port, timestamp)
3. found       → refresh age (and move port if source moved)
4. then handle the frame by DESTINATION MAC: forward / flood / filter
```

- **Learning is inbound; forwarding is outbound** — the classic "learning is based on source, forwarding on destination" statement.
- Learning happens for **unicast source MACs**; multicast/broadcast source MACs are not learned (and violate standards).

## Exam Focus

- **"What does a switch learn and from where?"** → source MAC + ingress port + VLAN.
- Aging (default 300 s), sticky, and MAC moves are the operational facts to know.
- Combined with [[Port Security]] and [[DHCP Snooping]] in security scenarios.

## Related Terms

- [[CAM Table]], [[MAC Address]], [[Forwarding]], [[Flooding]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/04. MAC Learning]]