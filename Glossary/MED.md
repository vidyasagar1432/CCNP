---
tags: [CCNP, glossary, bgp, routing]
aliases: ["MED", "Multi-Exit Discriminator", "Metric BGP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# MED

## Definition

**MED (Multi-Exit Discriminator)** is the **optional non-transitive** attribute that tells a **neighbor AS** which of **your exit points** to prefer for **inbound** traffic. **Lower MED is better**. It is advertised **outbound** and evaluated **only among paths from the same neighbor AS**.

## How It Works

```text
You (AS 65001) advertise a prefix to your provider (AS 65002)
  via R1 with MED 50, via R2 with MED 100
  → the provider prefers R1 (lower MED) for inbound traffic
```

```cisco
route-map LOWER-MED permit 10
 set metric 50            ! sets MED
router bgp 65001
 neighbor 203.0.113.2 route-map LOWER-MED out
```

## Rules that Matter

- MED = **the "metric" in `show ip bgp`** — it is BGP's fourth-best "metric"-like knob.
- Compared **only if both paths came from the same neighbor AS** (a famous exam trap).
- It is **non-transitive**: does not cross AS boundaries beyond the immediate neighbor.

## Exam Focus

- **MED = inbound; local pref = outbound** — pair it with [[Local Preference]] in any policy question.
- Lower is better; default treated as 0.
- MED is outranked by weight, local pref, origin, and AS path length — even a "good" MED loses to a shorter AS path.

## Related Terms

- [[BGP]], [[BGP Path Selection]], [[Local Preference]], [[AS Path]], [[eBGP]]
- Level 12 notes: [[Level 12 - BGP/06. MED]]