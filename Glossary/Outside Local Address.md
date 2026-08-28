---
tags: [CCNP, glossary, nat]
aliases: ["Outside Local"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Outside Local Address

## Definition

The **outside local address** is the address of an *outside* host **as it is represented to the inside network** — the address an inside host uses as the destination when talking to that outside host.

## How It Works

For the common Internet case where the outside host is **not** translated:

```text
Outside Local = Outside Global
```

The inside host simply sees the server's real public address.

Can they differ? Yes — in **outside source translation** ([[Outside Source NAT]]), the router rewrites the source address of packets coming *from* the outside. After that rewrite:

```text
Inside host sees: 203.0.113.99   ← outside local
Internet host is: 198.51.100.99  ← outside global
```

This is used for overlapping address spaces and dual-NAT / VPN partner designs.

## Example

```text
Router:  ip nat outside source static 203.0.113.99 198.51.100.99

Inside host ──► server
  dst: 203.0.113.99        source: 198.51.100.99
       └── outside local   └── outside global
```

## Exam Focus

- **Outside local = what the inside network thinks the outside host's address is.**
- When outside NAT is *not* applied, outside local equals outside global — the default exam scenario.
- The four terms are a 2×2 grid; the most common error is claiming "outside local is always public." It is the *representation*, which can be private in overlapping designs.

## Related Terms

- [[Outside Global Address]], [[Inside Local Address]], [[Inside Global Address]], [[Outside Source NAT]], [[NAT]]
- Level 15 notes: [[Level 15 - NAT/01. Static NAT]], [[Level 15 - NAT/04. Policy NAT]]