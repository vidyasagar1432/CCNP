---
tags: [CCNP, glossary, high-availability, networking]
aliases: ["VSS", "Virtual Switching System", "StackWise", "StackWise Virtual", "Switch Stacking", "StackWise-480"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: High Availability
created: 2026-08-29
---

# Virtual Switching System

## Definition

**Stacking technologies make multiple physical switches behave as ONE logical switch** — one control plane, one management, chassis-like simplicity at box scale. Cisco flavors: **StackWise** (stackable Catalyst: 3750/3850/9300, special stacking cables, master/standby + members) and **VSS (Virtual Switching System)** (two chassis as one via **VSL** links — mostly legacy 4500/6500) and its successor **StackWise Virtual** on Catalyst 9000.

## The One-Switch Illusion

```text
StackWise: up to 9 switches, one master active + standby member, unified config
VSS: two chassis → one logical switch; VSL (10G links) carries control+data
benefits: single STP instance, single management IP, EtherChannel across members
member/link failure: traffic continues via remaining members (stateful, with SSO)
```

## Exam Focus

- **"What makes several switches act as one?" → stacking (StackWise) or VSS/StackWise Virtual** — the definition; "one control plane, one config".
- **Master/standby election** (StackWise) and **VSL** (VSS) — the mechanics questions.
- **Why stack?** → fewer STP instances, easier mgmt, cross-member EtherChannel — the design value.
- **Stack vs chassis**: box limits vs scalability — the capacity angle; stack failover via Stateful Switchover ([[SSO]]).

## Related Terms

- [[SSO]], [[High Availability]], [[EtherChannel]], [[STP]]
- Level 27 notes: [[Level 27 - High Availability/07. StackWise VSS]]