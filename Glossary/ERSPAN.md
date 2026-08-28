---
tags: [CCNP, glossary, monitoring, telemetry]
aliases: ["ERSPAN", "Encapsulated Remote SPAN", "Remote SPAN", "RSPAN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Monitoring & Telemetry
created: 2026-08-29
---

# ERSPAN

## Definition

**ERSPAN (Encapsulated Remote SPAN)** mirrors traffic **across a routed/IP network**: mirrored packets are **encapsulated in IP + GRE** and sent to a **destination on any reachable router/switch** — analyzer can be anywhere, unlike local **[[SPAN]]** (same box). The GRE-encapsulated copies ride normal routing; the destination decapsulates and hands them to the analyzer.

## How It Differs

| Aspect | SPAN | RSPAN | ERSPAN |
| --- | --- | --- | --- |
| Scope | Same switch | Same L2 (VLAN) | Anywhere on IP |
| Encapsulation | None | VLAN tag | IP/GRE |
| Need | Simple local capture | L2 remote | L3 remote |

## Exam Focus

- **"Which mirroring works across routed networks?" → ERSPAN** — vs SPAN (local) / RSPAN (L2-only) — the scope question.
- **The triple wrap**: original frame → GRE → IP — "how is the copy transported?" answer.
- Destination: any router/switch with ERSPAN support (not a plain PC NIC) — the requirement fact.
- Cloud/labs: ERSPAN into cloud-VPC analyzers — modern use ([[Telemetry]] tie-in).

## Related Terms

- [[SPAN]], [[Wireshark]], [[GRE]]
- Level 26 notes: [[Level 26 - Monitoring & Telemetry/05. ERSPAN]]