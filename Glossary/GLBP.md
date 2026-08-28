---
tags: [CCNP, glossary, switching, first-hop]
aliases: ["GLBP", "Gateway Load Balancing Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: First Hop Redundancy
created: 2026-08-29
---

# GLBP

## Definition

**GLBP (Gateway Load Balancing Protocol)** is Cisco's [[First Hop Redundancy Protocol|FHRP]] that fixes the wasted-bandwidth problem: instead of one active gateway, it elects one **AVG (Active Virtual Gateway)** that assigns up to **four AVFs (Active Virtual Forwarders)** — each with its **own virtual MAC** — and **load-balances hosts across them** (round-robin by default). Redundancy AND utilization in one protocol.

## The Two Roles

```text
AVG: one router, owns the virtual IP, replies to ARP —
     hands each host a DIFFERENT AVF's virtual MAC   (load-balancing!)
AVF: up to 3 more, each owns a virtual MAC 0007.b400.XXYY
     forwards traffic for the hosts ARP-assigned to it
AVG dies → next-priority router becomes AVG; AVFs keep forwarding
```

- Weighting/tracking: **weight-based** rather than pure priority (weight 100 default; tracking drops weight → AVF disabled) — GLBP's load-aware failover.
- Multicast **224.0.0.102**, UDP 3222.

## Exam Focus

- **"Which FHRP load-balances default-gateway traffic?" → GLBP** — the one-line separation from HSRP/VRRP.
- **"Virtual IP is answered by the AVG with per-host virtual MACs"** — the ARP behavior question.
- GLBP status verbs: AVG / AVF — the vocabulary check (no "master/backup").

## Related Terms

- [[First Hop Redundancy Protocol]], [[HSRP]], [[VRRP]], [[Object Tracking]]
- Level 14 notes: [[Level 14 - First Hop Redundancy/03. GLBP]]