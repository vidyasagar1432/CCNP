---
tags: [CCNP, glossary, security, identity]
aliases: ["RADIUS", "Remote Authentication Dial-In User Service"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# RADIUS

## Definition

**RADIUS (Remote Authentication Dial-In User Service)** is the **open-standard AAA protocol for network access** — 802.1X, VPN (IPsec/SSL-VPN), wireless — **UDP 1812 (auth) / 1813 (accounting)**. It combines auth + authorization in one exchange and encrypts only the password (shared-secret hashing). The network-access counterpart to [[TACACS+]].

## RADIUS in the Flow

```text
supplicant (PC/phone) → authenticator (switch/AP/WLC) → RADIUS server (ISE, ACS)
switch asks: "is this identity OK?" → server: Accept/Reject + attributes
(802.1X + RADIUS = the dynamic VLAN/ACL delivery path — per-user policy!)
```

## Exam Focus

- **Ports & transport**: UDP 1812/1813 vs TACACS+ TCP 49 — the transport-question pair.
- **"Which protocol authenticates wireless/802.1X users?" → RADIUS** — network-access vs [[TACACS+]]'s device-admin split.
- Password-only encryption: "credentials protected how?" → only the password/keyed digest — the security-limitation question.
- RADIUS accounting attributes feed billing/audit (Acct-Interim-Interval) — the accounting mention.
- Fallback patterns: RADIUS server groups + `local` — server-down resilience same as AAA in general.

## Related Terms

- [[AAA]], [[TACACS+]], [[Port Security]], [[802.1X]]
- Level 17 notes: [[Level 17 - Security/03. RADIUS]]