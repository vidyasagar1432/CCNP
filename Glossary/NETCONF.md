---
tags: [CCNP, glossary, sdn, automation]
aliases: ["NETCONF", "Network Configuration Protocol", "RFC 6241", "Capability Exchange"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# NETCONF

## Definition

**NETCONF** (RFC 6241) is the **IETF standard for managing network devices over SSH using XML RPCs**: `<get-config>`, `<edit-config>`, `<commit>` against **[[YANG]]-modeled datastores**. It supports **transactions/rollback** (candidate/running datastores), **filtering**, and **event notifications** — the "deep" programmatic interface (vs lighter [[RESTCONF]]).

## The NETCONF Exchange

```text
transport: SSH (default port 830) — session, not polling
messages: <rpc> <rpc-reply> XML; ops: get, get-config, edit-config, commit
datastores: running (live), candidate (staged), startup — commit = atomic
capability exchange: server announces which YANG models it supports
```

## Exam Focus

- **"Which standard manages config over SSH/XML-RPC?" → NETCONF** — the definition; port 830 — the port fact.
- **Edit-config + commit = transactional** — "can you roll back?" → candidate/commit — the reliability answer.
- **YANG is NETCONF's data model** — the inseparable pairing (RFC 6020).
- NETCONF vs SNMP: config/transactional vs read/monitor — the era contrast.

## Related Terms

- [[YANG]], [[RESTCONF]], [[XML]], [[SSH]], [[Telemetry]]
- Level 24 notes: [[Level 24 - SDN & Automation/08. NETCONF]]