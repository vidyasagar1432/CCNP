---
tags: [CCNP, glossary, routing, networking]
aliases: ["FIB", "Forwarding Information Base"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# FIB

## Definition

The **FIB (Forwarding Information Base)** is the **data-plane, forwarding-optimized copy of the routing table** — built by [[CEF]] from the [[RIB]] with next hops already resolved into L2 rewrites. Packets are switched against the FIB, not against the RIB: longest-prefix **FIB lookup → adjacency rewrite → forward**, at line rate.

## FIB vs RIB

| | RIB (routing table) | FIB |
| --- | --- | --- |
| Owner | Control plane (routing protocols, statics) | Data plane (CEF) |
| Question it answers | "What do I know?" | "What do I send and out which MAC?" |
| Built by | Protocols + AD + metric logic | CEF copying + resolving the RIB |
| Lookups | Best path selection | Per-packet forwarding |

```text
routing protocols ─► RIB ─► CEF ─► FIB + adjacency table ─► data plane
```

## Exam Focus

- **"Which structure does the data plane forward against?" → FIB**, not the RIB — get the separation right in any architectural question.
- **FIB must be in sync without being consulted**: `clear ip cef` fixes stale FIBs after table changes — know the refresh command.
- CEF terms overlap: "the FIB" is half of CEF; "adjacency table" is the other half ([[CEF]]).

## Related Terms

- [[CEF]], [[RIB]], [[Routing Table]], [[Recursive Lookup]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/05. FIB]]