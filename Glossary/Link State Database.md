---
tags: [CCNP, glossary, ospf, routing]
aliases: ["LSDB", "Link-State Database"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# Link State Database

## Definition

The **link-state database (LSDB)** is the collection of all **[[LSA]]s** received by an OSPF router — the router's complete map of the network topology *within its area*. SPF runs on the LSDB to compute routes.

## How It Works

- Each router originates LSAs describing its own links and receives flooded LSAs from neighbors.
- **All routers in the same [[OSPF Area]] must converge on an identical LSDB** — if they differ, routes will be inconsistent.
- Every new LSA (e.g., a link flap) is flooded and re-runs SPF only for the affected areas.
- `show ip ospf database` displays the LSDB; sequence numbers keep versions straight.

```text
LSDB = Σ of all LSAs seen by the router (per area)
SPF(Dijkstra) over LSDB → routing table prefix entries
```

## Exam Focus

- LSDB is **per-area**: routers in different areas hold different LSDBs (ABRs relay summary/external info instead — see [[ABR]], [[ASBR]]).
- A **mismatched LSDB** (blocked flooding, one-way link) means routing loops/blackholes — classic exam troubleshooting angle.
- Larger LSDB ≠ slower convergence necessarily, but *area boundaries* exist precisely to bound this database per router.

## Related Terms

- [[OSPF]], [[LSA]], [[OSPF Area]], [[ABR]], [[ASBR]], [[OSPF Neighbor States]]
- Level 10 notes: [[Level 10 - OSPF/06. LSA Types]], [[Level 10 - OSPF/07. SPF Algorithm]]