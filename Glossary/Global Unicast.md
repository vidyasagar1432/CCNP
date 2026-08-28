---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["Global Unicast Address", "GUA", "2000::/3"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# Global Unicast

## Definition

A **Global Unicast Address (GUA)** is IPv6's public, Internet-routable address — scope **2000::/3** (2000:: to 3fff:…). A typical GUA: `2001:db8:1:2::101/64` (global prefix, site subnet, interface ID). Assigned by **RIR → ISP → customer**, or configured statically/SLAAC/DHCPv6.

## Anatomy of a GUA

```text
2001:0db8:0001:0002:0000:0000:0000:0101/64
├─ 2001:0db8:0001 ─ global routing prefix (48 bits)
├─ 0002 ─────────── subnet ID (16 bits)
└─ …:0101 ─────── interface ID (64 bits, EUI-64 or random by SLAAC)
```

## Exam Focus

- **Any GUA ≠ unique**: "2001::/32" research block vs real assignment; exam asks "is 2001:db8::/32 routable on the Internet?" → NO, it's documentation-only.
- **Every interface also keeps a [[Link Local]] address** — GUAs are an *additional* address, not a replacement.
- Traffic to a GUA leaves the link; traffic to link-local never does — the fundamental scope test.

## Related Terms

- [[IPv6]], [[Link Local]], [[Unique Local]], [[SLAAC]], [[DHCPv6]]
- Level 06 notes: [[Level 06 - IPv6/02. Global Unicast]]