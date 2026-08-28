---
tags: [CCNP, glossary, monitoring, telemetry]
aliases: ["Flexible NetFlow", "FNF", "NetFlow Record", "NetFlow Monitor", "NetFlow Exporter", "IPFIX"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Monitoring & Telemetry
created: 2026-08-29
---

# Flexible NetFlow

## Definition

**Flexible NetFlow (FNF)** is the configurable NetFlow engine: **you define the records** — `match` = the flow key fields, `collect` = the extra fields to gather (which switches/extended features first made this usable). Built from three pieces: **record → exporter → monitor** (bound to an interface). It's also how **IPFIX** works on Cisco (IPFIX = IETF standard FNF).

## The FNF Pipeline

```text
flow record: match ipv4 source address, match ipv4 destination address,
             collect counter packets, collect counter bytes…  (your key+data)
flow exporter: destination 10.1.1.50 (collector), transport udp 2055
flow monitor: record X, exporter Y → applied to interface (input/output)
```

## Exam Focus

- **"Which NetFlow lets you define your own records?" → Flexible NetFlow** — the definition; record/exporter/monitor = the three config components.
- **match vs collect**: key fields vs additional data — the semantic split.
- **IPFIX = IETF-standard FNF** — the standardization question.
- Application recognition (NBAR) integration: FNF can key on app ID — the modern capability.

## Related Terms

- [[NetFlow]], [[Telemetry]], [[SNMP]]
- Level 26 notes: [[Level 26 - Monitoring & Telemetry/03. Flexible NetFlow]]