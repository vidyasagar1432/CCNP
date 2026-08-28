---
tags: [CCNP, glossary, wan, networking]
aliases: ["WAN Edge", "vEdge", "cEdge", "SD-WAN Edge Router", "WAN Edge Router"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# WAN Edge

## Definition

**WAN Edge** is the [[SD-WAN]] name for the **routers at each site**: **vEdge** (Viptela OS) or **cEdge** (IOS-XE 16.12+). They **terminate the secure overlay tunnels** (IPsec/DTLS), run **OMP** with [[vSmart|vSmart]], classify/forward application traffic per centralized policy, and connect every **TLOC** (transport locator = interface+IP that anchors a tunnel) to the fabric.

## The Edge Duties

```text
underlay: one or more transports (MPLS, broadband, LTE) — each a TLOC
overlay: full-mesh secure tunnels with peers; OMP to vSmart
forwarding: app-aware SLA steering, local internet breakout option
platforms: vEdge (Viptela) vs cEdge (IOS-XE) — same fabric, different OS
```

## Exam Focus

- **"What is a WAN Edge?" → the site router (vEdge/cEdge) in SD-WAN** — vs the controller planes ([[vManage]]/[[vSmart]]/[[vBond]]) — the plane map.
- **TLOC**: transport locator (IP+interface+color) — what anchors tunnels — the sometimes-asked term (usually deep-dive).
- **vEdge vs cEdge**: OS and feature differences — the platform question (cEdge = IOS-XE, integrations).
- Edge roles in policy: localized policy (QoS/path) vs vSmart centralized — the distribution question.

## Related Terms

- [[SD-WAN]], [[vSmart]], [[vManage]], [[vBond]], [[IPsec]]
- Level 23 notes: [[Level 23 - Enterprise WAN/11. WAN Edge]]