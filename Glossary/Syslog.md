---
tags: [CCNP, glossary, network-services, monitoring]
aliases: ["Syslog", "Syslog Server", "logging", "Syslog Facility"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# Syslog

## Definition

**Syslog** is the standard **event-logging** service: devices send timestamped, severity-tagged messages to local buffers and/or a **syslog server** (**UDP 514**). Levels 0–7 (emergency→debug); facility tags identify origin. It's the forensic foundation of every "what happened at 02:00?" investigation.

## Severity Levels (memorize)

| Lvl | Word | Meaning |
| --- | --- | --- |
| 0 | Emergency | System unusable |
| 1 | Alert | Immediate action |
| 2 | Critical | Critical condition |
| 3 | Error | Error condition |
| 4 | Warning | Warning condition |
| 5 | Notice | Normal but notable |
| 6 | Informational | Info messages |
| 7 | Debug | Debug-level |

```text
logging host 10.1.99.10          (server, UDP 514)
logging trap 6                   (send ≤ severity 6)
logging console 3 / logging buffered 5   (local destinations, own levels each)
show logging                      (buffer + hosts + levels)
```

## Exam Focus

- **Severity number ↔ word mapping** — likely memorized trivia (3=error, 6=informational…).
- **Timestamps depend on [[NTP]]** — "why do syslog times disagree across devices?" → clock skew, no NTP.
- Traps vs syslog confusion: both event-driven; syslog is the log stream, SNMP is the query/management channel — keep them separate.
- Debugging: `debug ip ospf events` → logs go to console/buffer as debug (7) — the "which level is debug" answer.

## Related Terms

- [[NTP]], [[SNMP]], [[Management Plane]]
- Level 16 notes: [[Level 16 - Network Services/07. Syslog]]