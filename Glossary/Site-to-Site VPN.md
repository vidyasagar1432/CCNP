---
tags: [CCNP, glossary, vpn, networking]
aliases: ["Site-to-Site VPN", "S2S VPN", "LAN-to-LAN VPN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# Site-to-Site VPN

## Definition

A **site-to-site (S2S) VPN** connects **entire networks** through routers/firewalls at each site — LAN-to-LAN over the Internet, invisible to the hosts inside. Implementation is device-to-device: **IPsec** (with GRE/VTI for routing), **DMVPN** for hub-and-spoke scale, or **FlexVPN** for flexible policies.

## The Pattern

```text
[LAN A]──router A──Internet──router B──[LAN B]
     tunnel (encrypted) carries LAN A ↔ LAN B traffic
routers peer via IKE/IPsec; encapsulated traffic rides the tunnel
hosts: no client, no config — the router does the work
(remote users instead need [[Remote Access VPN]])
```

## Exam Focus

- **"Which VPN connects whole networks without client software?" → site-to-site** — versus remote-access's per-user clients.
- **Routing over S2S**: GRE tunnels or VTI carry routing protocols; IPsec alone carries only the negotiated subnets — design nuance questions.
- **Hub-and-spoke** (DMVPN) vs full mesh vs point-to-point — architecture scenarios ("many branches → which S2S design?").
- IPsec profiles: IKEv2 + ESP transforms — the "what parameters matter?" question reuses [[IKEv2]]/[[IPsec]].

## Related Terms

- [[VPN]], [[IPsec]], [[IKEv2]], [[GRE]], [[DMVPN]], [[FlexVPN]], [[GET VPN]], [[Virtual Tunnel Interface]]
- Level 18 notes: [[Level 18 - VPN Technologies/06. Site-to-Site VPN]]