---
tags: [CCNP, glossary, network-services, networking]
aliases: ["NTP", "Network Time Protocol", "Stratum", "NTP Server"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# NTP

## Definition

**NTP (Network Time Protocol)** synchronizes device clocks across the network — **UDP 123**, hierarchical **stratum** levels (stratum 0 = atomic/GPS source, 1 = direct servers, n = each hop down). Consistent time matters for **logs, certificates, [[Syslog]] correlation, and protocols** — a campus/DC staple.

## The Essentials

```text
client: ntp server 10.1.99.1            (or pool)
server: ntp master 4                    (self-stratum in labs)
auth:   ntp authentication-key / trusted-key
verify: show ntp status (. stratum, sync)  |  show ntp associations

clock skew facts: NTP adjusts gradually (no jumps) unless drift is huge;
system clock sets the timestamp for every log/syslog/cert operation
```

## Exam Focus

- **"Which service synchronizes router clocks?" → NTP (UDP 123)** — the one-liner.
- Stratum logic: **lower stratum = more authoritative** — a favorite logic flip.
- **Why sync matters**: syslog timestamps, [[SNMP]] uptimes, certificate validity (PKI auth), HSRP/GLBP log forensics — the "uses of accurate time" scenario question.
- NTP security (NTP reflection attacks; authenticate to prevent spoofing) — the modern hardening question.

## Related Terms

- [[Syslog]], [[SNMP]], [[HTTPS]]
- Level 16 notes: [[Level 16 - Network Services/05. NTP]]