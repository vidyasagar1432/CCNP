---
tags: [CCNP, glossary, vpn, networking]
aliases: ["VPN", "Virtual Private Network", "Tunnel"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# VPN

## Definition

A **VPN (Virtual Private Network)** delivers **private networking over a shared/public transport** by tunneling + (usually) encrypting traffic — giving remote sites or users "as if on the private LAN" connectivity across the Internet. The family: site-to-site ([[Site-to-Site VPN]]), remote access ([[Remote Access VPN]]), and the many flavors ([[IPsec]], [[DMVPN]], [[FlexVPN]], [[SSL VPN]], [[GET VPN]]).

## The VPN Family Tree

| Type | Who connects | Example tech |
| --- | --- | --- |
| [[Site-to-Site VPN]] | Networks (router↔router) | IPsec, GRE-over-IPsec, DMVPN, FlexVPN, GETVPN |
| [[Remote Access VPN]] | Users (client→gateway) | AnyConnect (SSL/TLS), IPsec IKEv2 |
| Overlay | Sites over provider | MPLS L3VPN/L2VPN (SP-managed!) |

```text
tunneling = a payload wrapped in new headers ([[GRE]])
security  = confidentiality + integrity + auth ([[IPsec]])
```

## Exam Focus

- **VPN = tunnel + encryption** — the "what makes it private?" answer is encryption, not the tunnel alone.
- **Passive vs active tunneling protocols**: [[GRE]]/IPsec are *active* (packet-by-packet); provider MPLS/[[QinQ]] are passive (label/tag-based) — the exam's "which is a tunneling protocol?" discrimination.
- Remote access security = the modern campus/WFH scenario (AnyConnect, TLS) — expect the "which VPN for home workers?" → SSL VPN/anyconnect.

## Related Terms

- [[Site-to-Site VPN]], [[Remote Access VPN]], [[IPsec]], [[GRE]], [[DMVPN]], [[FlexVPN]], [[SSL VPN]], [[GET VPN]]
- Level 18 notes: [[Level 18 - VPN Technologies/11. VPN Technology Comparison]]