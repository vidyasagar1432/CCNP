---
tags: [CCNP, glossary, security, hardening]
aliases: ["Device Hardening", "Hardening", "Secure Device Configuration"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# Device Hardening

## Definition

**Device hardening** is the practice of locking down the device itself: **disable unneeded services, enforce strong AAA, encrypt management, secure access lines, control-plane protection, and restrict remote config** so the router/switch is not the soft target. It's the "defense at the box" layer beneath network-wide security.

## The Hardening Checklist (exam-favorite)

| Area | Action |
| --- | --- |
| Management | [[SSH]] only, `transport input ssh`, `exec-timeout` |
| AAA | `aaa new-model`, TACACS+/RADIUS, local fallback |
| Services | `no ip http server` (plain web UI off), disable unused services (finger, tcp-small-servers...) |
| Access lines | `access-class` on VTY, login block-for, `ip telnet source-interface` |
| Passwords | `enable secret` (hashed), `service password-encryption`, role-based access control |
| Control plane | [[CoPP]] |
| Restrict | [[ACL|ACLs]] inbound on edge, uRPF (unicast RPF), BGP/OSPF authentication |

## Exam Focus

- **"Which set of practices secures devices against remote compromise?" → hardening** — with the biggest single answers being SSH-only + strong AAA.
- `service password-encryption` vs `enable secret`: encryption is reversible-obfuscation, secret is hashed — the "which is stronger?" trivia.
- **Role-Based Access Control (RBAC)** and privileged exec levels (`privilege 15`) — authorization granularity questions.
- Pair with the operational side: [[Secure Management]] — how admins reach the box.

## Related Terms

- [[SSH]], [[AAA]], [[TACACS+]], [[CoPP]], [[Secure Management]], [[ACL]]
- Level 17 notes: [[Level 17 - Security/10. Device Hardening]]