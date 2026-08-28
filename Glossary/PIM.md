---
tags: [CCNP, glossary, multicast, routing]
aliases: ["PIM", "Protocol Independent Multicast", "Multicast Routing", "PIM Sparse Mode"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# PIM

## Definition

**PIM (Protocol Independent Multicast)** is the router-to-router **multicast routing protocol** — "protocol independent" because it builds the multicast tree using **whatever unicast routing table exists** (OSPF/EIGRP/static — the RPF check). Flavors: **dense ([[PIM-DM]])**, **sparse ([[PIM-SM]] + RP)**, and **bidirectional/SSM**. PIM does **not** run its own topology database — it borrows the IGP's.

## How PIM Thinks

```text
multicast tree built from source (S) to receivers (G):
  (S,G) shortest-path tree — per-source, or (*,G) shared tree via RP
reception rule: RPF check — packets accepted only if they arrive on the
  interface the unicast table says leads to the source ([[Reverse Path Forwarding|RPF]])
PIM neighbors: hello protocol (224.0.0.13) → DR election on LANs ([[PIM DR]])
```

## Exam Focus

- **"Which protocol routes multicast between routers?" → PIM** vs IGMP's host edge — the scope answer.
- **"Why 'protocol independent'?" → it relies on the unicast RIB** (and RPF) — the naming question.
- **Dense vs Sparse** is THE PIM choice: dense = flood-and-prune (small/broadcast-friendly), sparse = explicit joins via [[Rendezvous Point|RP]] (most networks) — the architecture scenario.
- PIM hello = 224.0.0.13, group-based — the recognition fact.

## Related Terms

- [[PIM-DM]], [[PIM-SM]], [[Rendezvous Point]], [[Reverse Path Forwarding]], [[IGMP]], [[Source-Specific Multicast]]
- Level 19 notes: [[Level 19 - Multicast/05. Multicast Routing]]