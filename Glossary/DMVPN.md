---
tags: [CCNP, glossary, vpn, networking]
aliases: ["DMVPN", "Dynamic Multipoint VPN", "NHRP", "mGRE"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# DMVPN

## Definition

**DMVPN (Dynamic Multipoint VPN)** is Cisco's hub-and-spoke site-to-site VPN that scales to **hundreds/thousands of branches** *and* builds **dynamic spoke-to-spoke tunnels on demand**: branches that need to talk directly bypass the hub (no hub bottleneck, no full-mesh config). Built on **mGRE + NHRP + IPsec** — hub is a single "up" interface; spokes register their public addresses with the hub via **NHRP**.

## The Mechanics

```text
hub: tunnel interface with mGRE (no fixed tunnel destination) + NHRP server
spoke: registers (public IP) with hub via NHRP
spoke A → spoke B traffic: NHRP resolution → temporary direct tunnel → IPsec
phases: Phase 1 = always through hub; Phase 2 = direct spoke-spoke;
Phase 3 = routing scales with phase-2 + prefix propagation
benefits: one hub config, no per-spoke tunnels, dynamic resilience
```

## Exam Focus

- **"Which VPN auto-creates spoke-to-spoke tunnels when traffic demands?" → DMVPN** — vs static full-mesh.
- **Protocol partners**: mGRE (multipoint GRE) + **NHRP** (next-hop resolution) + IPsec — the stack question.
- **Phase distinction**: "when do spokes talk directly?" → Phase 2/3 with NHRP resolution — the architecture phase question.
- Why it scales: hub config is branch-agnostic; adding a branch = just a spoke config — the "adding a 100th site" scenario.

## Related Terms

- [[VPN]], [[Site-to-Site VPN]], [[GRE]], [[IPsec]], [[NHRP]]
- Level 18 notes: [[Level 18 - VPN Technologies/03. DMVPN]]