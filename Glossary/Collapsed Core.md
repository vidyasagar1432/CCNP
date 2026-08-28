---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Two-Tier Architecture", "Collapsed Core", "Two-Tier"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Collapsed Core

## Definition

**Collapsed core (two-tier)** merges the distribution and core into **one layer** on top of the access layer — so traffic between access switches crosses a single pair of "core/distribution" devices. The standard choice for small and mid-size sites.

## Two-Tier vs Three-Tier

```text
TWO-TIER:        access ──► collapsed core (pair)
THREE-TIER:      access ──► distribution ──► core

two-tier = fewer devices, less cost, simpler
three-tier = more scale headroom, cleaner failure domains
```

| Factor | Two-tier | Three-tier |
| --- | --- | --- |
| Cost/complexity | Lower | Higher |
| Size fit | Small/mid campus, single building | Multi-building, larger campuses |
| Failure domain | Pair of cores = shared risk | Each distribution block isolated |

## Exam Focus

- **"When is collapsed core appropriate?"** → small sites / single building where a separate core tier is overkill.
- The upgrade path question: "site growing, two-tier under pressure → move to three-tier."
- Same principles apply as [[Three-Tier]] — collapsing layers doesn't remove the roles, it merges them.

## Related Terms

- [[Three-Tier]], [[Enterprise Network Architecture]], [[Spine-Leaf]], [[Network Design Principles]]
- Level 02 notes: [[Level 02 - Network Topologies/07. Two-Tier]]