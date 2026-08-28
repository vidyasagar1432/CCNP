---
tags: [CCNP, glossary, monitoring, telemetry]
aliases: ["NetFlow", "Flow Record", "Flow Collector", "NetFlow v9", "IPFIX"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Monitoring & Telemetry
created: 2026-08-29
---

# NetFlow

## Definition

**NetFlow** exports **flow records — metadata about conversations, not packets** — to a collector (the "who talked to whom, how much" view). A flow = unidirectional sequence with the classic 7-tuple key (src/dst IP, src/dst port, protocol, ToS, input iface). NetFlow powers **traffic analysis, capacity planning, and security visibility** (anonymized research data). Successor: **[[Flexible NetFlow]] & IPFIX**.

## The Flow Concept

```text
aggregate packets into flows: key = srcIP,dstIP,srcPort,dstPort,proto,ToS,input
record fields: packets/bytes counters, timestamps, flags — cached on the device
export: UDP to collector (port 2055 typical), v5 (fixed records) / v9 (template)
use: top talkers, app identification, DDoS forensics, billing
```

## Exam Focus

- **"What does NetFlow export?" → flow metadata (not packets, not config)** — the definition; "what identifies a flow?" → the 7-tuple.
- **NetFlow vs SNMP**: per-conversation detail vs interface counters — the visibility contrast (SNMP = SNMP term).
- **v5 vs v9**: fixed vs template-based records — the version question (v9/IPFIX = flexible).
- NetFlow vs packet capture: metadata vs full packet content — "what do you get with a capture you don't get with NetFlow?" → payload.

## Related Terms

- [[Flexible NetFlow]], [[SNMP]], [[Telemetry]], [[Wireshark]]
- Level 26 notes: [[Level 26 - Monitoring & Telemetry/02. NetFlow]]