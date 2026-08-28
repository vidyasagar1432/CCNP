---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Totally Stubby Area", "Totally Stub"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# Totally Stubby Area

## Definition

A **totally stubby area** takes the [[Stub Area]] idea further: it blocks external **and** inter-area summary LSAs (Types 3, 4, 5). It is a Cisco extension that keeps only **intra-area routes + a default route**.

## LSA Table

| LSA type | Allowed? |
| --- | --- |
| Type 1, 2 (intra-area) | Yes |
| Type 3 (inter-area) | **No — only the default from the ABR** |
| Type 4 (ASBR summary) | No |
| Type 5 (external) | No |

```cisco
area 2 stub no-summary
```

The `no-summary` keyword is what makes a stub *totally* stubby.

## Exam Focus

- **Totally stubby = stub + no-summary**: Type-3 LSAs suppressed except for the injected default route.
- The default route is still advertised by the ABR (as a Type-3), so routers in the area can reach everything else via it.
- Configure **`area X stub no-summary` on the ABR**; the internal routers only need `area X stub`.
- This is a Cisco-specific optimization — the pure IEEE stub area allows Type 3.

## Related Terms

- [[OSPF Area]], [[Stub Area]], [[NSSA]], [[ABR]], [[LSA]]
- Level 10 notes: [[Level 10 - OSPF/10. Totally Stubby]]