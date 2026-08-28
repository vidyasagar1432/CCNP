---
tags: [CCNP, glossary, bgp, routing, policy]
aliases: ["Prefix List", "Prefix-list"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Policies
created: 2026-08-29
---

# Prefix List

## Definition

A **prefix list** matches routes by **prefix and prefix length** — the preferred tool for BGP filtering (route-maps, distribute-lists, neighbor filters) because it is more precise, faster, and easier to read than long ACLs for routes.

## How It Works

```text
ip prefix-list ALLOW-24 permit 10.0.0.0/8 le 24
     matches any route within 10.0.0.0/8 with mask ≤ 24 bits

ge (greater-or-equal) / le (less-or-equal) control the range:
     10.0.0.0/8          → exactly /8
     10.0.0.0/8 le 24    → /8 through /24
     10.0.0.0/8 ge 25    → /25 through /32
     10.0.0.0/8 ge 16 le 24 → /16 through /24
```

- Implicit **deny all** at the end — same as ACLs.
- Matching uses **exact and mask rules**, unlike IPv4 ACLs which match by wildcard.

## Exam Focus

- **`le`/`ge` semantics is the #1 prefix-list question** — practice "10.1.0.0/16 le 24 catches /16../24" style queries.
- Prefix lists only match **routes** (not data-plane packets) — a classic distinction from ACLs.
- First match wins; order matters; `seq` numbers keep it editable (similar to [[Route Map]]).
- Used with `neighbor ... prefix-list ... in/out`.

## Related Terms

- [[Route Map]], [[Policy-Based Routing]], [[BGP]]
- Level 12 notes: [[Level 12 - BGP/12. Prefix Lists]]