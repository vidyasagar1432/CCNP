---
tags: [CCNP, glossary, monitoring, telemetry]
aliases: ["SPAN", "Switched Port Analyzer", "Port Mirroring", "Monitor Session"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Monitoring & Telemetry
created: 2026-08-29
---

# SPAN

## Definition

**SPAN (Switched Port Analyzer)** — port mirroring — **copies traffic** from source interfaces/VLANs to a **destination port** (where a sniffer/analyzer listens). It's **local (same switch)**, typically **one-way**, can mirror RX/TX/both, and the destination port goes out of normal forwarding. Limits: destination must be on the same switch; no L3 crossing — that's what **[[ERSPAN]]** is for.

## The Mirror Setup

```text
monitor session 1 source interface Gi0/1 both (or source vlan 10)
monitor session 1 destination interface Gi0/24
→ Gi0/24 gets a COPY of Gi0/1 traffic; Gi0/24 no longer switches normally
```

## Exam Focus

- **"What mirrors traffic to an analyzer?" → SPAN** — the definition; "local-only" constraint — the limitation question.
- **Sources**: interface, VLAN; directions: RX, TX, both — the keywords.
- **Destination port behavior**: removed from normal switching — the gotcha ("can the destination also be a source?" → the danger, loops).
- SPAN vs TAP: software mirror vs hardware tap — the passive-vs-active distinction.

## Related Terms

- [[ERSPAN]], [[Wireshark]], [[Port Security]]
- Level 26 notes: [[Level 26 - Monitoring & Telemetry/04. SPAN]]