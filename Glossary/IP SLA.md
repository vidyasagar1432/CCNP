---
tags: [CCNP, glossary, monitoring, telemetry]
aliases: ["IP SLA", "IP Service Level Agreement", "IP SLA Probe", "Synthetic Probe", "Track Object"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Monitoring & Telemetry
created: 2026-08-29
---

# IP SLA

## Definition

**IP SLA** generates **synthetic probes** between routers to measure **latency, jitter, loss, and availability** along a real path — without waiting for real traffic to complain. Even better: results can **trigger actions** via a `track` object → **routing changes** (floating static, HSRP priority shift) or **SNMP/ syslog** alerts when thresholds trip.

## The Probe Design

```text
ip sla 1: icmp-echo 10.2.2.2 source-interface lo0, frequency 10
ip sla schedule 1 life forever start-time now
track 1 ip sla 1 reachability → tie into: static route tracking,
HSRP object tracking, EEM alerts
measures: RTT, jitter (sla_jitter), MOS, packet loss, threshold reactions
```

## Exam Focus

- **"What measures path quality synthetically?" → IP SLA** — the definition; each probe = scheduled, sourced, measured.
- **"How does a backup route fail over?" → IP SLA tracks + floating static / HSRP priority** — the reaction mechanism (the classic scenario: track WAN link → failover).
- **Jitter/MOS probes**: sla_jitter + udp-jitter for voice readiness — the media-quality question.
- IP SLA vs live monitoring: synthetic vs observed — the difference; complements NetFlow/SNMP.

## Related Terms

- [[SNMP]], [[Syslog]], [[Object Tracking]], [[Floating Static]], [[HSRP]]
- Level 26 notes: [[Level 26 - Monitoring & Telemetry/06. IP SLA]]