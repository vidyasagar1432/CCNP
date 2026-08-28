---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["EIGRP Stub", "Stub Router EIGRP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# EIGRP Stub

## Definition

An **EIGRP stub router** advertises only a restricted route set and — crucially — **never forwards queries** beyond itself. Stub sizing is the standard design protection against wide **diffusing computations** (see [[DUAL]]).

## What It Does

- The stub tells neighbors "I am a stub": they stop sending **queries** to it for remote destinations.
- Route types controlled by keywords: `connected`, `static`, `summary`, `redistributed`, `receive-only` (learn nothing).
- Default stub mode on Cisco announces connected + summary (unless restricted).

```cisco
router eigrp CCNP-NET
 address-family ipv4
  topology base
  stub connected static
```

## Why It Matters

In a hub-and-spoke design, spokes should never be asked to answer queries about the rest of the network — they have no transit paths. Stub keeps recomputation **local to the hub side**, preventing [[DUAL|SIA]] and convergence storms.

## Exam Focus

- **Stub routers are query sinks** — they do not propagate queries and they do not learn routes from neighbors (only advertise their own set).
- `receive-only` means the router advertises nothing at all.
- A well-formed exam topology: DMVPN/hub-spoke with spokes configured as stubs is the "design fix" answer.

## Related Terms

- [[EIGRP]], [[DUAL]], [[Feasible Successor]]
- Level 11 notes: [[Level 11 - EIGRP/07. Stub]]