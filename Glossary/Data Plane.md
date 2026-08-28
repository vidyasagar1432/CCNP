---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Forwarding Plane", "Data-Plane"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Data Plane

## Definition

The **data plane** (forwarding plane) is the **fast path**: the part of a network device that actually **forwards traffic** — frames, packets, sessions — as fast as the hardware allows. It is where throughput, latency, and ACL/QoS actions happen.

## How It Works

```text
packet in ──► lookup in hardware (FIB/TCAM) ──► actions (forward, drop, mark) ──► packet out
                 data plane: no protocol decisions, just execution
```

| Plane | Work | Speed |
| --- | --- | --- |
| Data | Forwarding per FIB/ACL rules | Hardware (ASIC), line-rate |
| Control | Routing protocols, [[STP]], ARP | CPU, occasional |
| Management | SSH/SNMP, CLI, NETCONF | CPU, on-demand |

- The **FIB** is a data-plane copy of the routing table (built by the [[Control Plane]]).
- In SDN ([[Software-Defined Networking]]), the data plane is **programmable** via open protocols like [[OpenFlow]] — the controller programs the FIB.

## Exam Focus

- **"Which plane forwards packets?"** → data plane — instantly.
- Evolving from "hardware-only forwarding" to programmable pipelines is an ENCOR SDN theme — you must know that SDN **separates control from data**.
- Traffic that misses the FIB may be punted to CPU — where "slow path" failures (high CPU) start.

## Related Terms

- [[Control Plane]], [[Management Plane]], [[Intermediary Device]], [[End Device]]
- Level 00 notes: [[Level 00 - Networking Basics/05. Network Components]]