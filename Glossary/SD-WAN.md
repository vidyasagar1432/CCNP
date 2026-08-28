---
tags: [CCNP, glossary, wan, networking]
aliases: ["SD-WAN", "Software-Defined WAN", "Cisco SD-WAN", "Viptela", "Overlay", "Secure Tunnel"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# SD-WAN

## Definition

**Cisco SD-WAN (Viptela)** is the WAN architecture that **abstracts the underlay**: it builds a **secure overlay (IPsec/DTLS tunnels)** across ANY transport (**MPLS, broadband, LTE**) and steers traffic with **business policy** instead of provider fate. The fabric splits planes: **[[vManage]]** (management), **[[vSmart]]** (control, via **OMP**), **[[vBond]]** (orchestration/authentication), and **[[WAN Edge|WAN Edge]]** routers (vEdge/cEdge) at the sites.

## The Underlay/Overlay Idea

```text
underlay: whatever WAN you have (MPLS + broadband + LTE = transport diversity)
overlay: full-mesh secure tunnels between edges — one logical WAN
policy: application-aware routing (SLA-based per app), local internet breakout
control: OMP (Overlay Management Protocol) edge↔vSmart, IPv4/IPv6
```

## Exam Focus

- **"What does SD-WAN add over MPLS?" → transport independence + app-aware steering + policy** — the value question; overlay over mixed underlays.
- **The four planes**: vBond (orchestration) / vSmart (control) / vManage (management) / edges (data) — the plane-to-component match (exam favorite).
- **OMP = the SD-WAN BGP-like control protocol** — connectivity + route exchanges between edge and controller.
- **vEdge vs cEdge**: Viptela OS vs IOS-XE (16.12+) — the platform question.

## Related Terms

- [[vManage]], [[vSmart]], [[vBond]], [[WAN Edge]], [[IPsec]], [[MPLS WAN]]
- Level 23 notes: [[Level 23 - Enterprise WAN/07. SD-WAN]]