---
tags: [CCNP, glossary, security, switching]
aliases: ["Port Security", "MAC Address Security", "sticky MAC", "port-security"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# Port Security

## Definition

**Port security** binds a switch port to **specific MAC addresses**: only those devices may use it. Actions when a violation occurs: **shutdown** (errdisable), **restrict** (drop + log), **protect** (silent drop). It stops MAC spoofing, rogue laptops, and MAC-flooding attacks at the access edge.

## The Setup

```text
switchport port-security
switchport port-security maximum 2          ← how many MACs allowed
switchport port-security mac-address sticky  ← learn + keep (survives reboot)
switchport port-security violation shutdown  ← default; errdisable afterwards
switchport port-security aging time 10      ← reclaim stale entries
```

## Exam Focus

- **"Which feature permits only known MACs on an access port?" → port security** — the definition; violation modes = the follow-up (shutdown/restrict/protect).
- **PortFast + BPDUguard + port-security** is the access-port hardening trio — the "which three?" scenario.
- **Security traps**: maximum 1 + no sticky = reboot clears; **errdisable recovery** (`errdisable recovery cause psecure-violation`) = the auto-recovery command.
- MAC flooding defense: a switch with port security can't be flooded into fail-open — the attack-motivation answer.

## Related Terms

- [[MAC Address]], [[DHCP Snooping]], [[Dynamic ARP Inspection]], [[IP Source Guard]], [[Access Port]]
- Level 17 notes: [[Level 17 - Security/05. Port Security]]