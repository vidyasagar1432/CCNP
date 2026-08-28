---
tags: [CCNP, glossary, ospf, routing]
aliases: ["OSPF Area", "Area 0", "Backbone Area", "OSPF Areas"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# OSPF Area

## Definition

An **OSPF area** is a group of routers and links that maintain **one shared [[Link State Database]]** (identical LSAs). Areas are the primary OSPF scaling mechanism; every router in an area runs SPF over the same topology data.

## Core Rules

- **Area 0 (backbone) is mandatory and must be contiguous** — all other areas attach to it.
- Routers inside an area see full intra-area detail; other areas are summarized via Type-3 LSAs (see [[LSA]]).
- A router with interfaces in multiple areas is an **[[ABR]]**; one that redistributes external routes is an **[[ASBR]]**.

```text
Area 0 (backbone)
  ├── Area 1 (standard)
  ├── Area 2 (stub)
  └── Area 3 (NSSA)
All connect through Area 0 via ABRs
```

## Area Types

| Area type | Features |
| --- | --- |
| Standard | Full LSA spectrum, external routes allowed |
| Stub | Blocks Type 5; injects default route |
| Totally stubby | Also blocks Type 3/4 |
| NSSA | Allows Type 7 external import outside backbone |
| Totally NSSA | NSSA + no inter-area summaries |

Related area notes: [[Stub Area]], [[Totally Stubby Area]], [[NSSA]].

## Exam Focus

- **All routers in an area must agree on the area number** — mismatched area = no adjacency.
- **Backbone contiguity is the #1 area design rule**; broken Area 0 is fixed with [[Virtual Link]]s (last resort).
- SPF runs per area; ABRs keep one SPF per connected area.

## Related Terms

- [[OSPF]], [[Link State Database]], [[ABR]], [[ASBR]], [[LSA]], [[Stub Area]], [[Totally Stubby Area]], [[NSSA]], [[Virtual Link]]
- Level 10 notes: [[Level 10 - OSPF/08. Areas]]