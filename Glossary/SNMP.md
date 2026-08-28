---
tags: [CCNP, glossary, network-services, monitoring]
aliases: ["SNMP", "Simple Network Management Protocol", "SNMPv3", "MIB", "OID"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# SNMP

## Definition

**SNMP (Simple Network Management Protocol)** is the monitoring/management protocol: a **manager (NMS)** polls **agents** (routers/switches) for values from the **MIB** (a tree of object IDs = **OIDs**) and receives **traps/informs** on events. **UDP 161** (polling), **UDP 162** (traps). Versions: **v1/v2c** (community strings, plaintext), **v3** (user + auth + encryption).

## The Model

```text
NMS manager ── GET/GETNEXT/SET ──► agent (device, snmp-server …)
agent ── TRAP (fire-and-forget) / INFORM (acknowledged) ──► manager
snmp-server community public RO      (v2c, read-only — legacy/hardening red flag)
snmp-server host 10.1.99.5 version 3 priv user1 auth sha … 
MIB = database schema; OID = address of one value (e.g. 1.3.6.1.2.1.1.5 = sysName)
```

## Exam Focus

- **Ports: 161/162; versions: v3 = auth+encryption** — the security answer is always v3.
- **Trap vs poll**: traps are push (events), GETs are pull — the model question.
- **MIB/OID vocabulary**: "which tree value is the NMS reading?" → the OID in the MIB — recognize `show snmp` output and config lines.
- Informs add reliability (ACK + retransmit) over traps — the subtle differencer.

## Related Terms

- [[Syslog]], [[NTP]], [[Telemetry]]
- Level 16 notes: [[Level 16 - Network Services/06. SNMP]]