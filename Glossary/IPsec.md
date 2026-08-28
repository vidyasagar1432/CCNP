---
tags: [CCNP, glossary, vpn, security]
aliases: ["IPsec", "IP Security", "ESP", "AH"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# IPsec

## Definition

**IPsec** is the protocol suite that provides **confidentiality, integrity, authentication, and anti-replay** for IP traffic — the encryption engine behind site-to-site and remote-access VPNs. Two sides: **IKE** ([[IKEv2|IKEv1/v2]] key management, UDP 500/4500) and **ESP** (encapsulating security payload, IP protocol 50 — the actual encrypted tunnel). Reality: **ESP only, IKEv2 only** — AH/IKEv1 are legacy.

## The IPsec Pieces

```text
IKE phase 1: authenticate peers, build ISAKMP SA (main/aggressive, DH, PSK/certs)
IKE phase 2: negotiate ESP SA pair + keys (quick mode; PFS optional)
ESP: encrypts payload (+ auth trailer) — transport or tunnel mode
crypto ipsec transform-set ESP-AES256-SHA256
crypto map / tunnel protection ipsec profile
```

## Exam Focus

- **"Which suite gives VPNs their encryption?" → IPsec (ESP)** — and "which protocol is the encrypted data carrier?" → ESP (proto 50), not AH (proto 51, auth-only, legacy).
- **IKE role**: establishes/negotiates the SAs — "what does UDP 500 do?" → IKE key exchange.
- Transport vs Tunnel mode: tunnel (SP-to-SP, new IP header) vs transport (host-to-host, payload only) — the mode question.
- **Anti-replay** (sequence numbers) and **PFS** — the security-option recognition facts.

## Related Terms

- [[IKEv2]], [[Site-to-Site VPN]], [[GRE]], [[DMVPN]], [[FlexVPN]], [[GET VPN]]
- Level 18 notes: [[Level 18 - VPN Technologies/02. IPsec]]