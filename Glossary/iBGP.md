---
tags: [CCNP, glossary, bgp, routing]
aliases: ["Internal BGP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# iBGP

## Definition

**iBGP (Internal BGP)** peer sessions run **between routers in the same AS**. Its job is to carry the BGP routes from border to border *without* redistributing them into the IGP.

## The iBGP Rules

- **Split horizon:** a route learned from an iBGP peer is **never re-advertised to another iBGP peer** → a full mesh of sessions is required (or [[Route Reflector]] / [[Confederation]]).
- **Next hop is preserved** from the eBGP path: the eBGP next hop must be reachable via IGP, or the iBGP speaker sets `next-hop-self`.
- **AS_PATH is not modified** by iBGP hops — it only grows at eBGP boundaries ([[AS Path]]).

```text
AS 65001:  R1 ─iBGP─ R2 ─iBGP─ R3
                ▲
                │ (no re-advertising between iBGP peers)
   full mesh, or route reflector, or confederation needed
```

## Exam Focus

- **Full mesh is mandatory by default** — the #1 iBGP exam item is recognizing the hierarchy of fixes: full mesh → reflectors → confederations.
- **Next-hop-self** is the standard fix when the eBGP next hop is not in the IGP.
- BGP routes stay out of the IGP — iBGP is a **transport for policy**, not for topology.

## Related Terms

- [[BGP]], [[eBGP]], [[Route Reflector]], [[Confederation]], [[BGP Path Selection]]
- Level 12 notes: [[Level 12 - BGP/02. iBGP]]