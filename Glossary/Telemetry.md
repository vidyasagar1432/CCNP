---
tags: [CCNP, glossary, monitoring, telemetry]
aliases: ["Telemetry", "Streaming Telemetry", "Push Model", "Model-Driven Telemetry", "gRPC", "gNMI"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Monitoring & Telemetry
created: 2026-08-29
---

# Telemetry

## Definition

**Streaming telemetry** **pushes** subscriptions of device data to collectors **continuously** — the modern answer to **[[SNMP]]'s pull/poll model**. Devices encode data as **protobuf/JSON** (over **gRPC/gNMI**, or TCP/UDP) and stream on a schedule or on change; collectors (InfluxDB/Prometheus) get **high-frequency, on-change visibility** — the backbone of monitoring at scale and of DNA Center assurance.

## Push vs Pull

| Aspect | SNMP (pull) | Telemetry (push) |
| --- | --- | --- |
| Model | Poller asks (GET) | Device streams |
| Frequency | Poll interval (20–60 s) | Sub-second / on-change |
| Data | MIB/OID (limited) | YANG-modeled, rich |
| Scale | Poller-bound | Scales to thousands of devices |

## Exam Focus

- **"What replaced SNMP polling at scale?" → streaming telemetry (push)** — the model contrast; "which is push?" → telemetry.
- **Mechanisms**: subscriptions, encodings (protobuf/JSON), transports (gRPC/gNMI) — the component question.
- **Push benefits**: immediate change detection, no polling gaps — the "why better for assurance?" answer.
- Tie-ins: DNA Center assurance, ThousandEyes, SD-WAN analytics all consume telemetry — the ecosystem.

## Related Terms

- [[SNMP]], [[NetFlow]], [[Flexible NetFlow]], [[DNA Center]]
- Level 26 notes: [[Level 26 - Monitoring & Telemetry/08. Telemetry]]