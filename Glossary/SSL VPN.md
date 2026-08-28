---
tags: [CCNP, glossary, vpn, security]
aliases: ["SSL VPN", "TLS VPN", "WebVPN", "Clientless VPN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# SSL VPN

## Definition

An **SSL/TLS VPN** rides on **TLS (TCP 443)** — the same port/encryption as [[HTTPS]] — which sails through almost any firewall. Two flavors: **clientless** (browser-only access to web apps) and **client-based** (full tunnel via AnyConnect). Remote users love it because 443 is rarely blocked.

## The Two Flavors

| | Clientless (WebVPN) | Client-based (full tunnel) |
| --- | --- | --- |
| Client | Browser only | AnyConnect client |
| Access | Web apps / portal | Full network access |
| Transport | HTTPS | TLS/DTLS (or IKEv2) |
| Use | Quick app access | Full teleworker |

## Exam Focus

- **"Which VPN type uses TLS on 443?" → SSL VPN** — the port/transport fact.
- **Clientless vs client-based** — "no software installed?" → clientless; "full network access?" → client-based.
- DTLS = UDP variant for better real-time over lossy paths — the "why UDP for a TLS VPN?" nuance.
- SSL VPN vs [[IPsec]] RA: both do remote access; SSL = easier egress (443), IPsec = mature/standard — the compare-and-contrast question.

## Related Terms

- [[VPN]], [[Remote Access VPN]], [[HTTPS]], [[IPsec]], [[IKEv2]]
- Level 18 notes: [[Level 18 - VPN Technologies/05. SSL VPN]]