---
tags: [CCNP, glossary, routing, redistribution]
aliases: ["Route Tag", "Routing Tag", "Tag"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Route Redistribution
created: 2026-08-29
---

# Route Tag

## Definition

A **route tag** is a 32-bit number attached to a redistributed route that travels **inside the routing protocol** (OSPF external LSA tag, EIGRP tag) — invisible to forwarding, invaluable to **policy**: tag at the injection point, then match the tag downstream to filter/adjust routes **without touching specific prefixes**.

## The Pattern

```text
border router: redistribute ospf 100 metric 20000 route-map SET_TAG
  route-map SET_TAG: set tag 100        ← "everything from OSPF gets tag 100"

another router:  route-map CATCH_TAG / distribute-list
  match tag 100 → deny/allow/change metric
  ⇒ "drop everything that came from OSPF" without listing 1000 prefixes
```

Why it beats prefix lists: **scale, semantics, consistency** — the tag says *origin*, not *address*.

## Exam Focus

- **"Which attribute identifies a route's redistribution origin for policy?" → route tag** — the cited purpose.
- Route tags are a key **loop-prevention** ingredient: tag your redistributed routes, filter them at the re-boundary.
- Tag tolerance: OSPF/EIGRP/BGP (community ≈ tag for BGP) all carry it; `show ip route` output shows tags; verify with `show ip route <prefix>`.

## Related Terms

- [[Route Redistribution]], [[Route Filtering]], [[Routing Loop]], [[BGP Communities]]
- Level 13 notes: [[Level 13 - Route Redistribution/06. Route Tags]]