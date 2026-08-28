---
tags: [CCNP, glossary, mpls, networking]
aliases: ["VRF", "Virtual Routing and Forwarding", "VRF-Lite", "Route Distinguisher", "Route Target"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# VRF

## Definition

A **VRF (Virtual Routing and Forwarding)** is a **separate routing table + forwarding table** on a router: each VRF = its own RIB, its own interfaces, its own services — **overlapping prefixes live side by side without conflict**. The engine of **L3VPNs** (one physical PE, many virtual routing domains). Two identifiers matter: **RD (route distinguisher)** keeps routes unique across VRFs in BGP; **RT (route target)** says which VRFs may import/export a route.

## How It Fits

```text
PE: customer A → VRF red (own RIB, own VRF interfaces)
    customer B → VRF blue — same 10.0.0.0/8? no problem
MP-BGP carries routes with {RD:RT} → import/export rules populate VRFs
label in the L3VPN = identifies the VRF at the far PE
VRF-Lite = VRFs without MPLS (pure L3 separation on a single box)
```

## Exam Focus

- **"What lets two customers use the same IP space on one PE?" → VRFs** — the definition; per-VRF RIB/FIB/interface.
- **RD vs RT**: RD = uniqueness (identifies the route); RT = policy (who gets it) — the classic confuse-them question.
- "show ip route vrf X" — VRFs are a CLI reality on any PE — the practical recognition.
- VRF-Lite extends the same isolation without a provider backbone — the "when no MPLS?" variant.

## Related Terms

- [[MPLS]], [[MPLS VPN]], [[MP-BGP]], [[BGP]], [[Routing Table]]
- Level 20 notes: [[Level 20 - MPLS/07. VRF]]