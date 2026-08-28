---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["Supernetting", "Supernet", "CIDR Aggregation"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# Supernetting

## Definition

**Supernetting** is grouping **multiple smaller networks into one larger prefix** with a mask that is *shorter* than the classful default (e.g. four class-C /24s → one /22). It is literally **[[Summarization]] applied to classful blocks** — the technique behind CIDR's Internet-scale route reduction (the 1990s "supernet" boom years).

## How /24s Become a /22

```text
199.10.0.0/24        = 11000111 00001010 00000000 XXXXXXXX
199.10.1.0/24        = ... 00000001 ...
199.10.2.0/24        = ... 00000010 ...
199.10.3.0/24        = ... 00000011 ...
common bits: 22        → 199.10.0.0/22  (supernet)
```

## Exam Focus

- **Supernetting vs summarization**: same math; "supernet" specifically means the block is **bigger than classful** (multiple class C's aggregated). On the exam treat them as synonyms with CIDR.
- "CIDR allows supernetting at the Internet level" — that's how today's BGP tables stay sane ([[BGP Aggregation]] uses it).
- Alignment rule still applies: the supernet must start on a boundary equal to its block size.

## Related Terms

- [[Summarization]], [[CIDR]], [[Route Aggregation]], [[BGP Aggregation]]
- Level 05 notes: [[Level 05 - IPv4/15. Supernetting]]