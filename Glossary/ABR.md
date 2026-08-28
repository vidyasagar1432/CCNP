---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Area Border Router"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# ABR

## Definition

An **Area Border Router (ABR)** has interfaces in **more than one [[OSPF Area]]** (at least one must be Area 0). It keeps a separate [[Link State Database]]/SPF tree per area and advertises **inter-area summary (Type-3)** LSAs between areas.

## How It Works

```text
    Area 1         ABR          Area 0
  routers ──────► Router ──────► backbone
              keeps 2 LSDBs, advertises Type 3 between them
```

- ABRs do **not** flood LSA detail across areas — they summarize (with `area X range ...` when configured).
- Every area (except totally-stubby variants) receives the default route and inter-area routes through ABR behavior.

## Exam Focus

- **A router with interfaces in areas 0 and 1 only is an ABR; a router touching one area and external routing is an [[ASBR]].** These roles are different and can coincide.
- ABR routes to *other* areas are advertised as Type-3 — an area's LSDB deliberately lacks other areas' Type-1/2 detail.
- In the exam, "ABR must touch area 0" matters: a router linking two non-backbone areas is **not** an ABR by definition.

## Related Terms

- [[OSPF]], [[OSPF Area]], [[LSA]], [[ASBR]], [[Link State Database]]
- Level 10 notes: [[Level 10 - OSPF/08. Areas]]