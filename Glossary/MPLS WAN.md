---
tags: [CCNP, glossary, wan, networking]
aliases: ["MPLS WAN", "MPLS WAN Service", "L3 WAN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# MPLS WAN

## Definition

An **MPLS WAN** uses the provider's **[[MPLS VPN|L3VPN]]** (Level 20 note 09) to connect enterprise sites: the SP furnishes **PE routers** carrying customer routes (CE–PE via eBGP/OSPF), and customers get **any-to-any private IP connectivity** with SLAs — no tunnels, no per-site VPN config. The customer buys "routing as a service" and the WAN becomes someone else's MPLS domain.

## The Enterprise View

```text
CE (your router) → PE (provider edge) → MPLS backbone → PE → CE (other site)
CE–PE: eBGP (typical), OSPF redistribution, or static routes
customer gets: private addressing, QoS priority classes, any-to-any mesh
provider gets: the L3VPN/VRF machinery ([[VRF]], [[MP-BGP]])
```

## Exam Focus

- **"What does the enterprise actually connect to?" → PE routers, via CE** — the edge picture; CE–PE protocol pairs (eBGP most common).
- **Why MPLS WAN?** → SLA, QoS, any-to-any, no tunnel mgmt — vs Internet VPNs — the decision question.
- **Cease the roles**: CE = customer-owned; PE = SP-owned (VRF) — "who runs BGP where?" answer.
- Modern trend: SD-WAN overlay ON TOP of (or replacing) MPLS WAN — the evolution mention ([[SD-WAN]]).

## Related Terms

- [[MPLS VPN]], [[VRF]], [[MP-BGP]], [[SD-WAN]], [[Metro Ethernet]]
- Level 23 notes: [[Level 23 - Enterprise WAN/04. MPLS WAN]]