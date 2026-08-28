---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["Unique Local Address", "ULA", "fc00::/7"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# Unique Local

## Definition

**Unique Local Addresses (ULAs, fc00::/7)** are IPv6's private/internal addressing — the analog of RFC 1918 ([[Private IP]]). They are **not globally routable**, can be reused across sites, and are meant for internal networks, VPNs, and lab environments.

## ULA Structure and the fc00 vs fd00 Split

```text
fc00::/7  (fc00:: – fdff:…)
   │
   ├─ fc00::/8  — reserved (defined for future use, NOT for operational use)
   └─ fd00::/8  — locally assigned:  fd + 40-bit global-ID (random) + 16-bit subnet + 64-bit IID
                     e.g. fd12:3456:789a:1::10/64
```

## Exam Focus

- **"Which IPv6 address is used for internal networks?"** → ULA (`fd00::/8` in practice, never `fc00::/8`).
- ULA + NAT66 is the IPv6 analog of private + [[NAT]] — though the design intent is "use GUA everywhere" (NAT-free), ULAs persist for internal-only segments and labs.
- Contrast set: GUA (routable) vs ULA (internal) vs link-local (per-link) — memorize scope, not prefix position.

## Related Terms

- [[IPv6]], [[Global Unicast]], [[Link Local]], [[Private IP]]
- Level 06 notes: [[Level 06 - IPv6/04. Unique Local]]