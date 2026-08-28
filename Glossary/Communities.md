---
tags: [CCNP, glossary, bgp, routing]
aliases: ["BGP Communities", "Community Attribute"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# Communities

## Definition

**Communities** are **optional transitive** tags (32-bit values) attached to BGP routes so operators can group routes and apply **policy remotely** — the sender tags, the receiver (or upstream) acts on the tag. They are the Internet's standard mechanism for "do this to these routes for me."

## How It Works

```text
R1 tags route with community 100:200
    │
    ▼
neighbor (upstream) matches community and applies its own policy
    (e.g., local-pref, no-export, prepend)

well-known: NO_EXPORT (0xFFFFFF01), NO_ADVERTISE (0xFFFFFF02), NO_EXPORT_SUBCONFED
custom:     2-octet AS:2-octet value (e.g., 65001:100)
```

```cisco
route-map TAG permit 10
 set community 65001:100
router bgp 65001
 neighbor 203.0.113.2 send-community both   ! must enable sending
```

## Exam Focus

- **`send-community` must be configured** — without it communities never leave the router.
- **Transitive** = travels with the route across ASes (unlike [[MED]]).
- Well-known values (NO_EXPORT etc.) behave like reserved communities — expect a "what does NO_EXPORT mean?" question.
- Communities prefer to **group routes** — a route-map can set one community for many prefixes; match policy is applied at the far end.

## Related Terms

- [[BGP]], [[Route Map]], [[Local Preference]], [[MED]], [[BGP Path Selection]]
- Level 12 notes: [[Level 12 - BGP/07. Communities]]