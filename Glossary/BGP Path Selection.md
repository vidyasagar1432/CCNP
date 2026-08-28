---
tags: [CCNP, glossary, bgp, routing]
aliases: ["BGP Best Path Selection", "BGP Path Selection Algorithm", "BGP Tie-Breakers"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# BGP Path Selection

## Definition

When BGP receives **multiple paths for the same prefix**, it runs a **deterministic decision process** — a strict priority list — and installs exactly **one best path** in the routing table.

## The Best-Path Steps (ENCOR list)

1. **Weight** (Cisco-proprietary) — highest wins
2. **[[Local Preference]]** — highest wins
3. **Locally originated** (network/aggregate/redistribute)
4. Shortest **[[AS Path|AS_PATH]]**
5. Lowest **[[MED|origin type]]** (IGP < EGP < incomplete)
6. Lowest **MED** (if same neighbor AS)
7. eBGP over iBGP (external preferred)
8. Lowest IGP cost to the **next hop**
9. Oldest eBGP route (or lowest RID) — stability tie-breaker / lowest router-id
10. Lowest neighbor address

```text
reminder: Weight → Local Pref → Originate → AS Path → Origin → MED → eBGP > iBGP → IGP metric → Age/RID → IP
```

## Exam Focus

- **The ordering is the question.** Almost every BGP simulator lab asks the "which path wins?" step.
- MED is compared **only between paths from the same neighbor AS** — a notorious trap.
- **eBGP over iBGP** and **AS path length** beat MED — MED is not a global rank.

## Related Terms

- [[BGP]], [[Local Preference]], [[AS Path]], [[MED]], [[Communities]], [[eBGP]], [[iBGP]]
- Level 12 notes: [[Level 12 - BGP/03. Path Selection]]