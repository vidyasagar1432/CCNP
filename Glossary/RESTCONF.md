---
tags: [CCNP, glossary, sdn, automation]
aliases: ["RESTCONF", "REST Config Protocol", "IETF RESTCONF"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# RESTCONF

## Definition

**RESTCONF** (RFC 8040) is the **IETF standard that exposes [[YANG]] models over HTTP(S) using REST verbs** — the REST-friendly sibling of [[NETCONF]]. It uses GET/POST/PUT/PATCH/DELETE against **YANG-defined resources** with **JSON or XML** payloads, on **HTTP(S) port 443** (often with basic/token auth). Simpler than NETCONF: no SSH sessions, no RPC ceremony — curl-friendly.

## RESTCONF vs NETCONF

| Aspect | NETCONF | RESTCONF |
| --- | --- | --- |
| Transport | SSH (RFC 6242) | HTTP(S)/REST |
| Data format | XML | JSON (and XML) |
| Operations | RPCs (get, get-config, edit-config…) | HTTP verbs on datastore paths |
| Feel | RPC/structured | Web/API |

## Exam Focus

- **"Which protocol does REST-over-YANG?" → RESTCONF** — vs NETCONF's SSH/RPC — the transport contrast.
- **Port 443, HTTP verbs, JSON payloads** — the fact set.
- RESTCONF vs plain REST: RESTCONF's resources are **YANG-modeled datastore paths** — the modeling difference.
- Quick-curl wins over NETCONF for one-off automation — the practical choice question.

## Related Terms

- [[NETCONF]], [[YANG]], [[REST API]], [[JSON]], [[XML]]
- Level 24 notes: [[Level 24 - SDN & Automation/07. RESTCONF]]