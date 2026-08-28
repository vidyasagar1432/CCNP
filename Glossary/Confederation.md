---
tags: [CCNP, glossary, bgp, routing]
aliases: ["BGP Confederation", "Confederations"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# Confederation

## Definition

**BGP confederation** is the alternative to [[Route Reflector|route reflectors]] for scaling iBGP: a single AS is **subdivided into sub-ASes** that peer with **eBGP-like** sessions internally, while appearing as **one AS** to the outside world.

## How It Works

```text
AS 65001 split into sub-AS 65011, 65012, 65013
  sub-ASes peer eBGP-style among themselves (TTL, next-hop handling internal)
  external neighbors still see ONE AS: 65001

loop prevention: AS_CONFED_SEQUENCE is checked INSIDE the confederation
                 but removed/stripped before advertising outside
   → AS path to outsiders shows 65001 only, not the sub-AS numbers
```

```cisco
router bgp 65011            ! sub-AS number
 bgp confederation identifier 65001
 bgp confederation peers 65012 65013
```

## Exam Focus

- **Confederation peers look like eBGP internally but act like iBGP externally** — keep the mental model: eBGP semantics inside, single AS outside.
- **AS_CONFED_SEQUENCE is not part of the external AS_PATH** — outsiders see no sub-AS numbers.
- Route reflectors + confederations can be combined — a classic advanced-scaling question.
- MED comparisons across confederations are still sub-AS-scoped.

## Related Terms

- [[BGP]], [[iBGP]], [[Route Reflector]], [[eBGP]], [[AS Path]]
- Level 12 notes: [[Level 12 - BGP/09. Confederation]]