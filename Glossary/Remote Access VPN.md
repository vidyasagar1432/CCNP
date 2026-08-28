---
tags: [CCNP, glossary, vpn, networking]
aliases: ["Remote Access VPN", "RA VPN", "Client VPN", "AnyConnect"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# Remote Access VPN

## Definition

A **remote-access (RA) VPN** connects **individual users** to the corporate network over the Internet — each user runs a **VPN client** (Cisco AnyConnect is the flagship answer: **TLS/DTLS** or **IKEv2** to the headend). After auth (usually **AAA/RADIUS + MFA**), the user gets an address on the inside and protected access as if on campus.

## The User Flow

```text
user laptop → AnyConnect → ASA/Firepower headend (public IP)
  auth: username/password (+ cert/OTP) via RADIUS/AAA
  tunnel: SSL/TLS (443!) or IPsec IKEv2 (UDP 500/4500)
  posture: optional (ISE) + split tunnel vs full tunnel (ACL/policy)
  inside: virtual IP + routes from the headend
```

## Exam Focus

- **"Which VPN needs a client on each user's device?" → remote access** — vs [[Site-to-Site VPN]] which doesn't.
- **AnyConnect = TLS (443)** — "traffic over standard web ports" is the firewall-friendly fact.
- Secure credentialing: **MFA/OTP, certificates, posture checks** — the security-layer question.
- Split tunneling (only corp subnets through VPN) vs full tunnel (everything) — the routing-policy decision.

## Related Terms

- [[VPN]], [[SSL VPN]], [[IKEv2]], [[AAA]], [[Site-to-Site VPN]]
- Level 18 notes: [[Level 18 - VPN Technologies/10. Remote Access VPN]]