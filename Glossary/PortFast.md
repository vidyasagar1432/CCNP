---
tags: [CCNP, glossary, stp, switching]
aliases: ["Edge Port", "spanning-tree portfast"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# PortFast

## Definition

**PortFast** makes a switch port attached to an **end host** (PC, server, IP phone, printer) skip the classic STP listening/learning sequence and transition **immediately to Forwarding** — improving host boot/connect time.

```cisco
interface GigabitEthernet0/1
 spanning-tree portfast
```

## How It Works

- Typically enabled **per access port**, never on uplinks/trunks to other switches.
- The port still participates in STP and remains a Known role (usually Designated); PortFast only bypasses the forward-delay wait.
- RSTP equivalent: **edge port** (PortFast is the Cisco implementation of it).
- Often combined with [[BPDU Guard]]:

```cisco
spanning-tree portfast
spanning-tree bpduguard enable
```

## Exam Focus

- **PortFast does not disable STP on the port** — it shortens the initial transition. If a BPDU arrives on a PortFast port (rogue switch), the port acts as a normal STP port (unless BPDU Guard shuts it down).
- Never place PortFast on inter-switch links: it re-creates the exact loops STP exists to prevent.
- Watch for **portfast trunk** — only for specific designs (e.g., directly connected to end devices needing trunking), treated differently in exams.

## Related Terms

- [[STP]], [[STP Port States]], [[BPDU Guard]], [[BPDU Filter]], [[RSTP]]
- Level 08 notes: [[Level 08 - STP/10. PortFast]]