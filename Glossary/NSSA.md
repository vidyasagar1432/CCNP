---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Not-So-Stubby Area", "NSSA"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# NSSA

## Definition

A **Not-So-Stubby Area (NSSA)** is a stub-like area that **still allows external routes to be imported** — an ASBR inside an NSSA originates external routes as **Type-7 LSAs**, which the ABR translates to **Type-5** for the rest of the OSPF domain.

## Why It Exists

A pure [[Stub Area]] forbids ASBRs entirely. Real designs often have a stub-like area that *must* receive external routes (e.g., a remote site with a redistributed static). NSSA allows that while keeping the LSA diet on a stub diet.

## Behavior

```text
NSSA ASBR ──► Type 7 LSA  (external, N1/N2 metrics)
      │
      ▼
ABR translates  Type 7 ──► Type 5  (only at NSSA boundary)
      │
      ▼
floods outside the NSSA
```

- Inside the NSSA, no Type-5 LSAs — same default-route/diet logic as stub areas.
- External metrics inside NSSA are shown as **N1/N2** (Type-7); after translation they are viewed as normal E1/E2 elsewhere.
- Config: `area X nssa` (optionally `default-information-originate` to inject default).

## Exam Focus

- **The ABR performs Type-7 → Type-5 translation** — the single most-tested NSSA behavior.
- NSSA is *not* the same as stub: stub forbids external routes; NSSA *permits* them internally but keeps them out of the standard Type-5 form inside.
- P-bit (propagate bit) controls which Type-7 LSAs the ABR translates — exam-level detail worth knowing.

## Related Terms

- [[OSPF Area]], [[Stub Area]], [[Totally Stubby Area]], [[LSA]], [[ASBR]], [[ABR]]
- Level 10 notes: [[Level 10 - OSPF/11. NSSA]]