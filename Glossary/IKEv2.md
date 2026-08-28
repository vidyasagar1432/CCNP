---
tags: [CCNP, glossary, vpn, security]
aliases: ["IKEv2", "Internet Key Exchange", "IKE", "IKEv1"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# IKEv2

## Definition

**IKEv2 (Internet Key Exchange version 2)** is the modern IPsec key-management protocol — it establishes and maintains the **security associations (SAs)** and session keys used to encrypt traffic. It replaced IKEv1's two-phase complexity with a leaner exchange, built-in **mobility, NAT traversal, and EAP** support, and is the standard everywhere now.

## The Exchange in One Line

```text
IKE_SA_INIT (2 messages: DH + nonces) → IKE_AUTH (2 messages: identity+auth, SAs)
→ child SA creation for bulk traffic (CREATE_CHILD_SA; rekeying/PFS)
UDP 500 (and 4500 for NAT-T)
vs IKEv1: IKEv2 has NO aggressive mode; DPD built-in; EAP for remote access
```

| IKEv1 | IKEv2 |
| --- | --- |
| Phase 1 + Phase 2 | One IKE_SA_INIT + IKE_AUTH flow |
| Main/Aggressive modes | No aggressive mode |
| Fragile NAT traversal | Built-in NAT-T + MOBIKE |
| Legacy configs | Modern standard |

## Exam Focus

- **"Which version of IKE is the modern standard?" → IKEv2** — and why: fewer round trips, built-in NAT-T/DPD, EAP.
- **IKEv2 layout**: IKE_SA_INIT ↔ IKE_AUTH = the four-message core — the course-question two-step.
- Ports: IKE 500; NAT-T 4500 (ESP-in-UDP) — the "which port does VPN use through PAT?" answer.
- IKEv2 + EAP = remote-access VPN auth (AnyConnect-style) — the tie-in to [[Remote Access VPN]].

## Related Terms

- [[IPsec]], [[Site-to-Site VPN]], [[Remote Access VPN]], [[Virtual Tunnel Interface]]
- Level 18 notes: [[Level 18 - VPN Technologies/07. IPsec IKEv2]]