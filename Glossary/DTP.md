---
tags: [CCNP, glossary, switching, vlan]
aliases: ["DTP", "Dynamic Trunking Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# DTP

## Definition

**DTP (Dynamic Trunking Protocol)** is Cisco's proprietary protocol that **negotiates trunking between switches** automatically — a port can offer to trunk, and its neighbor replies in kind. It is **off by default in modern IOS configurations** because auto-negotiated trunks violate security best practice.

## The Modes (memorize the pairings)

```text
switchport mode access          static access — NEVER trunk
switchport mode dynamic auto    offers nothing; accepts an OFFER    (must be asked)
switchport mode dynamic desirable  actively OFFERS to trunk (Cisco classic)
switchport mode trunk           always trunk, DTP frames still sent
switchport nonegotiate          kills DTP entirely (static trunk/access)
```

| Mode A | Mode B | Result |
| --- | --- | --- |
| dynamic desirable | dynamic auto | trunk |
| dynamic desirable | trunk | trunk |
| dynamic auto | trunk | trunk |
| dynamic auto | dynamic auto | access (nobody asked) |

## Exam Focus

- **"Which feature dynamically negotiates trunk links?" → DTP** — and the correct hardening answer is `switchport nonegotiate` + manual mode.
- **VLAN-hopping vector**: a DTP-offering port can turn a host's port into a trunk — attack lives off negotiated trunks.
- Participation rule: **DTP talks only between switches** (access ports to PCs don't matter); DTP frames belong to the native VLAN.

## Related Terms

- [[Trunk Port]], [[Access Port]], [[Native VLAN]], [[VLAN]]
- Level 07 notes: [[Level 07 - VLAN Technologies/08. DTP]]