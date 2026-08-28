---
tags: [CCNP, glossary, bgp, routing]
aliases: ["BGP Route Reflector", "Route-Reflector Client"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# Route Reflector

## Definition

A **route reflector (RR)** is the standard solution to the iBGP full-mesh problem: a hub router that **re-advertises iBGP-learned routes** to its **clients** (and other non-clients), so N routers need only N sessions to the RR instead of N×(N−1)/2 with each other.

## Roles and Rules

```text
clients ── iBGP ──► route reflector ## hub
                      │  re-advertises (breaks split horizon)
                      │
      to other clients / non-clients / external peers

RR three-way rule (hub-and-spoke hierarchy):
 1. From a client → reflect to all clients and non-clients
 2. From a non-client → reflect to clients only
 3. From eBGP → propagate normally
```

- Clients peer **only** with the RR (plus eBGP); the RR cluster needs a **cluster ID** when redundant RRs are used (loop prevention for reflected paths).
- **ORIGINATOR_ID** prevents loops when a route is reflected back.

## Exam Focus

- **RR is iBGP-only**: it does not change eBGP rules.
- **Cluster ID mismatch**: two RRs reflecting into each other need distinct cluster IDs to avoid route loops.
- A common design: RRs in the core, clients at the edge; the RR's own policy still applies — RR is not a "super router."

## Related Terms

- [[iBGP]], [[BGP]], [[Confederation]] (the alternative), [[BGP Path Selection]]
- Level 12 notes: [[Level 12 - BGP/08. Route Reflector]]