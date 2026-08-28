---
tags: [CCNP, glossary, mpls, networking]
aliases: ["MPLS", "Multiprotocol Label Switching", "Label Switching"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# MPLS

## Definition

**MPLS (Multiprotocol Label Switching)** forwards packets based on **short fixed labels** instead of IP longest-prefix lookups: at ingress, a packet gets a **label** deciding its path; core routers **swap/forward by label** (fast, deterministic); at egress the label pops and normal IP resumes. The payoff: **traffic engineering, VPNs ([[MPLS VPN]]), and fast reroute** — the invisible carrier behind modern service-provider networks.

## The Two Roles

```text
INGRESS (LER): labels IP packets — pushes label / assigns FEC ([[FEC]])
CORE (LSR): forwards by label only — swap/pop per LFIB ([[LFIB]])
EGRESS (LER): pops label, forwards IP normally
labels live between L2 and L3 headers (shim), 20 bits, range 16–1,048,575
```

## Exam Focus

- **"What does MPLS forward on?" → labels, not IP prefixes** — the core mechanism; "why?" → speed + VPN + TE capabilities.
- **Three operations**: push / swap / pop — the "what does an ingress/core/egress router do?" question.
- **Label range**: 16+ usable; 0–15 reserved (0 = explicit-null, 3 = implicit-null/PHP) — the trivia fact.
- MPLS ≠ tunneling alone — the [[VRF]] + [[MP-BGP]] machinery is what delivers L3VPNs — the scope separation.

## Related Terms

- [[MPLS Label]], [[FEC]], [[LER]], [[LSR]], [[LFIB]], [[VRF]], [[MP-BGP]], [[MPLS VPN]]
- Level 20 notes: [[Level 20 - MPLS/01. MPLS Basics]]