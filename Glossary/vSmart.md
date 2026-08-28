---
tags: [CCNP, glossary, wan, networking]
aliases: ["vSmart", "SD-WAN Control Plane", "OMP", "Overlay Management Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# vSmart

## Definition

**vSmart** is the **control plane** of Cisco [[SD-WAN]]: it runs **OMP (Overlay Management Protocol)** with every [[WAN Edge|WAN Edge]] router, maintains the overlay topology, and **distributes centralized policy** (routes, TLOCs, SLA classes) across the fabric. Edges exchange routes *indirectly through vSmart* — the controller is the route/state authority, not the data path.

## The Control Role

```text
OMP: peer vSmart ↔ edges (over DTLS/TLS) — carries routes, TLOCs,
     app-aware policy; thinks like BGP but purpose-built for the overlay
vSmart computes: topology (all edges → all edges), path preferences,
  centralized policy (data/control policy) authored in [[vManage]]
no user data flows through vSmart — control plane only
```

## Exam Focus

- **"Which component holds SD-WAN's control plane?" → vSmart; protocol? → OMP** — the pair; vSmart≠data path — the "does traffic transit vSmart?" trick (no).
- **OMP vs BGP**: similar family (path attributes, loop prevention) but overlay-specific — the comparison nuance.
- **Centralized vs localized policy**: vSmart=centralized; edge=localized — the policy split question.
- 1–2 vSmarts scale to thousands of edges — the scalability trivia.

## Related Terms

- [[SD-WAN]], [[vManage]], [[vBond]], [[WAN Edge]]
- Level 23 notes: [[Level 23 - Enterprise WAN/09. vSmart]]