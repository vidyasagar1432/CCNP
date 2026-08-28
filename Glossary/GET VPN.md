---
tags: [CCNP, glossary, vpn, security]
aliases: ["GET VPN", "Group Encrypted Transport VPN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# GET VPN

## Definition

**GET VPN (Group Encrypted Transport VPN)** encrypts traffic **without tunnels**: all sites share one **group key** (via a **Key Server** using GDOI/IKE), and packets are encrypted **hop-by-hop in the clear** — preserving the original IP headers (and thus **QoS, multicast, and routing behavior**). No tunnel endpoints = no topology change; designed for **MPLS/VPN backbones and mesh WANs**.

## The Model

```text
[KS key server] ── GDOI → registers each group member (routers)
members receive the GROUP SA (shared keys, rekeying)
site A → site B: encrypt+send directly (SP network routes it normally)
headers kept (no new IP! ) → multicast/routing/QoS keep working
perfect for SP/MPLS backbones — no spoke-hub hairpin, no tunnel overhead
```

## Exam Focus

- **"Which VPN encrypts without tunnels, preserving headers?" → GET VPN** — the signature property; GDOI = the key-distribution protocol fact.
- Why it matters: **multicast and routing protocols traverse it** (tunnel-free) — the "which VPN supports multicast transport?" answer.
- **MPLS/VPN SP services** are GETVPN's home — enterprise over SP MPLS WAN scenario.
- Weakness to know: it needs the SP transit to be trusted/controlled (keys protected but the path is the carrier's) — the security-model caveat question.

## Related Terms

- [[VPN]], [[IPsec]], [[Site-to-Site VPN]], [[GDOI]]
- Level 18 notes: [[Level 18 - VPN Technologies/09. GET VPN]]