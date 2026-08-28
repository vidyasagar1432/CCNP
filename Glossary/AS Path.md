---
tags: [CCNP, glossary, bgp, routing]
aliases: ["AS Path", "AS_PATH"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# AS Path

## Definition

**AS_PATH** is the **well-known mandatory** BGP attribute listing the sequence of ASes a route traversed. It is the core BGP **loop-prevention** mechanism and a top **best-path tie-breaker** (shortest wins).

## Behavior

- **At eBGP**: each eBGP speaker **prepends its own AS** before advertising onward to another AS.
- **At iBGP**: the path is passed **unchanged** (see [[iBGP]]).
- **Loop prevention**: a router **rejects** a route whose AS_PATH already contains its own AS.

```text
R1 (AS 65001) ─► R2 (AS 65002) ─► R3 (AS 65003)
   path at R3 = "65001 65002"   (read right-to-left: first origin on the right)

AS path prepending (policy): advertise to peers as "65001 65001 65002"
     ▶ used to make a path look longer (inbound traffic engineering)
```

## Exam Focus

- **AS_PATH is the only true BGP "metric-like" loop guard:** it is compared *globally* (step 4), unlike MED.
- **AS path length counts ASes in the path, not prefixes** — aggregation and prepending are the ways to influence it.
- `show ip bgp` displays it; **`as-path prepend`** manipulates it for inbound traffic control (with [[BGP Aggregation]] it shapes the Internet table).
- AS_SET / AS_SEQUENCE details are more of a CCNP Service Provider topic — know the basics (sequence, no loop → accepted).

## Related Terms

- [[BGP]], [[eBGP]], [[iBGP]], [[BGP Path Selection]], [[BGP Aggregation]]
- Level 12 notes: [[Level 12 - BGP/04. AS Path]]