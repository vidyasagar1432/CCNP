---
tags: [CCNP, glossary, labs, networking]
aliases: ["Network Simulator", "Network Emulator", "Lab Platform", "Packet Tracer", "CML", "GNS3", "EVE-NG"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Labs
created: 2026-08-29
---

# Network Simulator

## Definition

A **network simulator/emulator** is software that runs networks on your own hardware for practice. **Packet Tracer** = free but **low fidelity** (great for ENCOR basics); **CML (ex-VIRL)** = official Cisco, runs **real [[Cisco IOS]]/[[IOS XE]] images** via web UI + API; **GNS3** = free GUI running **real images + [[Docker]] containers**; **EVE-NG** = web-based platform running real images (IOS, NX-OS, ASA, third-party VMs). Real images → real exam value; the API personas (CML, [[Ansible]]/[[Python]]-driven) double as automation sandboxes.

## Choosing a Platform

```text
Packet Tracer — no install pain, switches/router simulation only; exam basics
CML — a real lab: IOS images, API, topologies of any size (free up to 20 nodes)
GNS3 — free, flexible: IOS + QEMU VMs + containers
EVE-NG — datacenter-style web lab, multi-tenant, runs anything image-like
```

## Exam Focus

- **"Which tool runs actual Cisco IOS?" → CML/GNS3/EVE-NG, not Packet Tracer** — the fidelity divide (simulator vs emulator).
- **CML** = the official Cisco answer for CCNP/CCIE labbing — recognition + API/automation support ([[NETCONF]]-friendly).
- Packet Tracer = fast topologies, limited protocol depth — the "good for basics" answer.
- All of them are lab-only; they don't replace real-hardware validation — the "so what" statement.

## Related Terms

- [[Cisco IOS]], [[IOS XE]], [[Docker]], [[Python]], [[Ansible]], [[Troubleshooting]]
- Level 30 overview: [[Level 30 - Labs/Labs Overview]], notes: [[Level 30 - Labs/01. Cisco Packet Tracer]], [[Level 30 - Labs/02. Cisco Modeling Labs (CML)]], [[Level 30 - Labs/03. GNS3]], [[Level 30 - Labs/04. EVE-NG]]