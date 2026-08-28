---
tags: [CCNP, glossary, multicast, routing]
aliases: ["PIM Sparse Mode", "PIM-SM", "Shared Tree", "SPT Switchover"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# PIM-SM

## Definition

**PIM Sparse Mode (PIM-SM)** builds multicast trees **only where receivers exist** — no flooding. Receivers join a **shared tree (*,G) rooted at the [[Rendezvous Point|RP]]**; when traffic volumes justify it, the tree switches to a **shortest-path tree (S,G)** directly from the source (**SPT switchover**, at the last-hop router). The default mode for enterprise multicast.

## The Life of a Flow

```text
receiver joins → (*,G) join toward the RP (shared tree)
source sends → first-hop router encapsulates/registers toward the RP → down the tree
last-hop router sees volume → SPT switchover: (S,G) join toward the source
  → direct path, RP only for control after that
```

## Exam Focus

- **"Which PIM mode requires an RP and explicit joins?" → sparse mode** — the core identification.
- **Shared tree (*,G) vs shortest-path (S,G)**: * = via RP (start), S = direct (after switchover) — the tree question.
- Default behavior: PIM-SM is the **IOS default** (`ip multicast-routing` + sparse mode) when you enable per-interface sparse — "which mode do you get by default?" → sparse.
- RP selection: static, Auto-RP, BSR — the RP-arcana question ([[Rendezvous Point]]).

## Related Terms

- [[PIM]], [[PIM-DM]], [[Rendezvous Point]], [[Source-Specific Multicast]], [[IGMP]]
- Level 19 notes: [[Level 19 - Multicast/03. PIM Sparse]]