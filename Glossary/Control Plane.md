---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Control-Plane"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Control Plane

## Definition

The **control plane** is the **slow path brain** of a network device: it **computes and decides** how traffic *should* be forwarded — running routing protocols ([[OSPF]], [[EIGRP]], [[BGP]]), spanning tree ([[STP]]), ARP/ND, and building the FIB that the [[Data Plane]] executes.

## How It Works

```text
control plane (CPU):
  learns neighbors, exchanges routes, elects root
        │ builds
        ▼
  routing table → FIB (pushed to data plane / ASIC)
```

- Work here is **protocol-driven and infrequent** compared to forwarding.
- About **Separation**: SDN ([[Software-Defined Networking]]) **centralizes the control plane** on a controller and leaves switches as dumb [[Data Plane]] forwarders; [[OpenFlow]] is the protocol that programs them.

## Exam Focus

- **Pair of questions:** "who runs OSPF?" → control plane; "who forwards packets?" → data plane. Reliable 2-pointer.
- Control plane overload (e.g., routing-table explosion) → slow convergence and CPU storms — a troubleshooting theme.
- SDN's whole premise is control/data plane **separation** — ENCOR asks you to identify which plane moved where.

## Related Terms

- [[Data Plane]], [[Management Plane]], [[Intermediary Device]], [[BGP]], [[OSPF]], [[EIGRP]]
- Level 00 notes: [[Level 00 - Networking Basics/05. Network Components]]