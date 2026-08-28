---
tags: [CCNP, glossary, vpn, networking]
aliases: ["Virtual Tunnel Interface", "VTI", "IPsec VTI", "Tunnel Mode IPsec"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# Virtual Tunnel Interface

## Definition

A **VTI (Virtual Tunnel Interface)** is a **routable tunnel interface whose entire traffic is protected by IPsec** (`tunnel protection ipsec profile`). Unlike GRE-over-IPsec (two protocols to manage) or crypto maps (per-traffic classification), the VTI is one clean interface: **route into it, and IPsec secures everything** — the modern point-to-point IPsec design.

## VTI vs the Old Ways

| | Crypto map | GRE-over-IPsec | IPsec VTI |
| --- | --- | --- | --- |
| Tunnel | None (traffic ACLs) | GRE + IPsec | IPsec-only interface |
| Routing | Static/ACL based | Dynamic protocols inside GRE | Dynamic protocols directly! |
| Config | Complex (map+ACL) | Two parts | One interface |

```text
interface Tunnel0
  ip address 10.254.0.1 255.255.255.252
  tunnel source g0/0
  tunnel destination 203.0.113.2
  tunnel protection ipsec profile S2S   ← the whole tunnel = IPsec
```

## Exam Focus

- **"Which modern interface carries IPsec routing directly?" → VTI** — vs crypto-map legacy; `tunnel protection ipsec profile` is the identification command.
- **Routing protocols run THROUGH a VTI** (it's a routable interface) — the dynamic-routing-over-IPsec answer.
- VTI versus GRE: no extra GRE header (less overhead), no multicast — "which carries multicast?" stays GRE's answer.
- Static VTI vs dynamic VTI (DMVPN-style): static = fixed peer; dynamic = peer learned — the variant note.

## Related Terms

- [[IPsec]], [[IKEv2]], [[GRE]], [[Site-to-Site VPN]]
- Level 18 notes: [[Level 18 - VPN Technologies/08. Virtual Tunnel Interface]]