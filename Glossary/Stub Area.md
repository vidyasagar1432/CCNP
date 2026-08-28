---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Stub Area"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# Stub Area

## Definition

A **stub area** is an [[OSPF Area]] that **blocks external (Type-5) LSAs** to reduce DB size and flooding. Since external destinations become unreachable for routing purposes, the ABR injects a **default route** into the stub.

## What Enters / Leaves a Stub

| LSA type | Allowed? |
| --- | --- |
| Type 1, 2 (intra-area) | Yes |
| Type 3 (inter-area summary) | Yes |
| Type 4 (ASBR summary) | No (no ASBRs allowed inside) |
| Type 5 (external) | **No — blocked** |
| Type 7 (NSSA external) | Not a stub concept |

```text
ABR ──► injects default (0.0.0.0/0) into stub area
Stub routers reach the outside world via the default route
```

## Requirements

- **No ASBR** (no redistribution) inside — that is what NSSA is for.
- **No virtual links transiting** the stub area.
- All routers in the area must have the area configured as stub (`area X stub`).

## Exam Focus

- Stub = blocks **Type 5**, keeps Type 3 — while [[Totally Stubby Area|totally stubby]] also blocks Type 3.
- Default route appearance is automatic from the ABR — an exam-tested behavior.
- If only *some* routers in an area are configured stub, adjacencies fail (inconsistent area type — see [[OSPF Neighbor States]]).

## Related Terms

- [[OSPF Area]], [[LSA]] (blocked types), [[Totally Stubby Area]], [[NSSA]], [[ABR]]
- Level 10 notes: [[Level 10 - OSPF/09. Stub]]