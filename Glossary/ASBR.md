---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Autonomous System Boundary Router", "ASBR"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# ASBR

## Definition

An **Autonomous System Boundary Router (ASBR)** is any OSPF router that **redistributes routes from outside OSPF** into the OSPF domain (other routing protocols, static routes, connected networks). It originates **Type-5 AS-External LSAs** (or Type-7 in an NSSA).

## How It Works

```text
EIGRP / static / BGP
        │ redistribution
        ▼
      ASBR ──► Type 5 LSA (external route) ──► flooded AS-wide
```

- External routes arrive in the routing table as **E1 / E2** (external type 1/2): E2 keeps the redistributed metric and ignores internal path cost; E1 adds internal cost to the external metric.
- Routers find the ASBR via **Type-4 ASBR-Summary LSAs** (created by the ABR in other areas).

## Exam Focus

- **ASBR is defined by *redistribution*, not by being at a network edge in general.** A router with a static route redistributed into OSPF is an ASBR.
- **Shell trap:** stub areas block type 5 — so external routes do not reach a stub area; this is why [[NSSA]] exists for stub-like areas that still need *some* external import (Type 7).
- E1 vs E2: E2 is default; both can coexist for the same prefix from different paths.

## Related Terms

- [[OSPF]], [[LSA]], [[ABR]], [[OSPF Area]], [[NSSA]]
- Level 10 notes: [[Level 10 - OSPF/08. Areas]], [[Level 10 - OSPF/06. LSA Types]]