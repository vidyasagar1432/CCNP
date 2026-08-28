---
tags: [CCNP, glossary, bgp, routing]
aliases: ["BGP Aggregation", "BGP Summarization"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# BGP Aggregation

## Definition

**BGP aggregation** (summarization) combines **more-specific prefixes into one shorter prefix** before advertising to neighbors — shrinking the global table, hiding flaps, and giving you one policy point instead of thousands.

## How It Works

Two mechanisms:

```text
1. aggregate-address 10.0.0.0/8 summary-only
     → advertise the aggregate only (suppress more specifics)

2. aggregate-address 10.0.0.0/8
     → advertise aggregate + keep more specifics (unless suppressed)
     → generates AS_SET in the path when components come from multiple ASes
```

- **`summary-only`** hides the components (the common production choice).
- Attribute handling: the aggregate **inherits** path attributes from component routes (origin, communities, AS path with AS_SET when mixed).

## Exam Focus

- **Aggregate does not fix routing problems** — it hides topology detail; the more specifics that are *not* suppressed are the trap.
- **AS_SET**: when component routes come from different ASes, the aggregate's AS path contains `{AS_SET}` — required for correctness (loop prevention).
- Combine with **`as-path prepend`** and **/24-or-longer filters** for inbound engineering — a common ENCOR lab theme.

## Related Terms

- [[BGP]], [[AS Path]], [[BGP Path Selection]], [[Route Map]]
- Level 12 notes: [[Level 12 - BGP/10. Aggregation]]