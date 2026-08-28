---
tags: [CCNP, glossary, multicast, switching]
aliases: ["IGMP Snooping", "Multicast Snooping"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# IGMP Snooping

## Definition

**IGMP snooping** is the **switch's multicast intelligence**: the switch listens to the **IGMP** join/leave messages between hosts and the router, and uses them to build an **L2 multicast forwarding table** — so multicast frames only egress **ports that asked for the group**, instead of flooding everywhere. Without it, multicast = broadcast (flooded, wasteful, insecure).

## The Mechanism

```text
host on port 3 joins group G → sends IGMP report
switch sees the report (snooping!) → 
  multicast forwarding table: G → [uplink router port 1, host port 3]
frames for G replicate only to 1 + 3 — not to ports 2, 4…
leaves/queries time entries out (mrouter port learned from router queries)
```

## Exam Focus

- **"How do switches avoid flooding multicast to all ports?" → IGMP snooping** — the definition; it's ON by default on modern switches (the default-state question).
- **The mrouter port**: the port toward the PIM router (learned from queries) — the "which port is always included?" fact.
- Snooping still needs the L3 PIM machinery upstream — switches snoop, routers route — the scope separation.
- Security nuance: spoofed joins can pull streams to arbitrary ports — the attack mention.

## Related Terms

- [[IGMP]], [[PIM]], [[Multicast]], [[Broadcast Domain]]
- Level 19 notes: [[Level 19 - Multicast/06. IGMP Snooping]]