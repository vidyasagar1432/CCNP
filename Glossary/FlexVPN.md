---
tags: [CCNP, glossary, vpn, networking]
aliases: ["FlexVPN", "Flexible VPN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# FlexVPN

## Definition

**FlexVPN** is Cisco's **modern, unified IPsec VPN framework built entirely on IKEv2** — it replaces the old one-trick solutions (DMVPN, GET VPN, EasyVPN, site-to-site) with a single feature set that can do **hub-and-spoke, spoke-to-spoke, remote access, and site-to-site** depending on how you configure the IKEv2 profiles and what roles you assign (`spoke`, `hub`, `client`). One protocol, many topologies.

## The Mental Model

```text
everything = IKEv2 profiles (identity/psk/authorization) + IPsec profiles
roles:  network-role hub | spoke | client
spoke config ≈ DMVPN behavior (mGRE + NHRP) when you add multipoint…
remote access ≈ EasyVPN/AnyConnect-style client when role = client
site-to-site ≈ classic IPsec VTI when point-to-point
```

## Exam Focus

- **"Which VPN architecture is Cisco's single IKEv2-based framework?" → FlexVPN** — the definition; IKEv2 is the tell.
- **FlexVPN vs DMVPN**: both do hub/spoke; FlexVPN = IKEv2-everything (DMVPN is IPsec but predates/mixed) — the "which one phrase" comparison.
- Roles (hub/spoke/client) and profiles = the config vocabulary — `crypto ikev2 profile` = recognition point.
- Interop: IKEv2-based → standard-compliant peers work — the "why choose it?" design answer.

## Related Terms

- [[VPN]], [[IKEv2]], [[DMVPN]], [[IPsec]], [[Site-to-Site VPN]], [[Remote Access VPN]]
- Level 18 notes: [[Level 18 - VPN Technologies/04. FlexVPN]]