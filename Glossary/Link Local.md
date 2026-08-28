---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["Link Local Address", "Link-Local", "fe80::/10", "LL"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# Link Local

## Definition

A **link-local address** (scope **fe80::/10**) is IPv6's always-present, automatically generated address **valid only on its local link** — never routed. It is what NDP uses to find neighbors, what routing protocols use for adjacencies/heartbeats, and what a fresh [[SLAAC]] prefix needs as a next hop.

## Facts to Count On

```text
fe80::/10 — every interface auto-creates one (no config needed)
derived via EUI-64/slaac from the interface MAC (with privacy rules)
  fe80::217:5aff:fe0a:7f48 — the EUI-64 pattern (ff:fe insertion)
never forwarded by routers → routers must use it as NDP next-hop
routing protocols ([[OSPFv3]], [[EIGRP for IPv6]], BGP peering) talk over link-local
when you see "fe80::/64" as a next hop — that's normal IPv6
```

## Exam Focus

- **"Which address does a router always have even with no global config?"** → link-local — auto, per-interface.
- **IPv6 routing-table next hops are link-local**, not GUAs — `show ipv6 route` output shows fe80::/64 nexthops; this is expected, not a bug.
- APIPA's IPv6-sane counterpart: link-local is *by design* on every interface — contrast with IPv4's failure-only 169.254 ([[APIPA]]).

## Related Terms

- [[IPv6]], [[Global Unicast]], [[SLAAC]], [[Neighbor Discovery]], [[OSPFv3]], [[EIGRP for IPv6]]
- Level 06 notes: [[Level 06 - IPv6/03. Link Local]]