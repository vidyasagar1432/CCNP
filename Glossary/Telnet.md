---
tags: [CCNP, glossary, network-services, security]
aliases: ["Telnet", "Telnet Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# Telnet

## Definition

**Telnet** is the **legacy remote terminal protocol** — **TCP 23**, **completely plaintext** (credentials AND session). It's the management protocol everyone teaches you to disable: `transport input ssh` on VTY lines is the modern default. It survives only in labs and legacy gear.

## Why It Must Go

```text
telnet 10.1.1.1          → user/password + every command in CLEAR TEXT
sniffer on path          → admin credentials harvested (the classic capture)
hardening: line vty 0 4 → transport input ssh   (and exec-timeout 5)
```

## Exam Focus

- **"Which management protocol sends passwords in cleartext?" → Telnet** — the security answer.
- **Port table question**: Telnet 23 vs [[SSH]] 22 vs [[HTTP]] 80 vs [[HTTPS]] 443 vs [[SNMP]] 161/162 vs syslog 514 — the multi-choice port bank.
- Cisco supports both by default: `transport input all` or `telnet ssh` — the "which config permits only encrypted access?" question expects `transport input ssh`.
- Related irritant: Telnet carries **NVT** terminal negotiation — usually only trivia depth.

## Related Terms

- [[SSH]], [[AAA]], [[Syslog]]
- Level 16 notes: [[Level 16 - Network Services/13. Telnet]]