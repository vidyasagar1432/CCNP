---
tags: [CCNP, glossary, routing, redistribution]
aliases: ["Route Filtering", "distribute-list", "Route Map Filter", "Prefix Filtering"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Route Redistribution
created: 2026-08-29
---

# Route Filtering

## Definition

**Route filtering** controls **which routes a router advertises or accepts** — the firewall of routing. Tools: **distribute-lists** (access-list or prefix-list), **route-maps**, and **protocol-specific filters** (OSPF area filters, BGP neighbor filters). In [[Route Redistribution|redistribution]] it's what stops leaked routes and loops.

## The Toolbox

| Filter | What it matches | Where |
| --- | --- | --- |
| `distribute-list` | ACL/prefix-list on in/out | Per interface (EIGRP out) / per process type (OSPF in) |
| prefix-list | Prefix + length exactly (`ge/le`) | Most precise, outbound favorite |
| route-map `match` | Prefix-list / tag / metric / next-hop | Redistribution + advanced policy (`set` too) |
| `ip prefix-list` | `seq 5 permit 10.1.0.0/16 le 24` | The syntax examiners quiz |

```text
redistribution loop-proof pattern:
  redistribute ospf 100 ... route-map ACCEPT_OSPF
  route-map ACCEPT_OSPF deny 10
    match tag 100        ← drop what WE injected into the other protocol
```

## Exam Focus

- **"Which tool restricts routes by exact prefix and length?" → prefix-list**, with `ge`/`le` — the precision question.
- **Prefix-list math**: `permit 10.0.0.0/8 le 24` = routes with /8–/24 covered — "the /9 gaps aren't permitted" trap.
- Distribute-list **in vs out** semantics: in = filter what you *accept* (affects the table), out = filter what you *send* (affects neighbors only) — a frequently inverted pair.

## Related Terms

- [[Prefix List]], [[Route Map]], [[Route Redistribution]], [[Route Tag]]
- Level 13 notes: [[Level 13 - Route Redistribution/07. Filtering]]