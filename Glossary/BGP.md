---
tags: [CCNP, glossary, bgp, routing]
aliases: ["Border Gateway Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# BGP

## Definition

**BGP (Border Gateway Protocol)** is the **path-vector** routing protocol of the Internet: it exchanges **prefixes with path attributes** between autonomous systems (ASes) and lets operators implement rich **policy** on who advertises what to whom.

## Key Facts

| Aspect | Value |
| --- | --- |
| Type | Path-vector (attributes per path, not per link) |
| Transport | **TCP port 179** (reliable, no replica of RTP/OSPF flooding) |
| Neighbors | Manually configured peers, eBGP vs iBGP |
| Updates | Incremental (full table first, then changes only) |
| Provision | Hold timer default 180 s; keepalive 60 s |
| Metric | No metric — **attributes + best-path selection** decide |

It is an **EGP** (exterior) protocol by design: designed to carry policy with thousands of routes, sacrificing the fast-convergence guarantees of an IGP like [[OSPF]] or [[EIGRP]].

## Example

An enterprise with two ISPs receives the full Internet table via **[[eBGP]]** from both; BGP picks the best path per prefix using attributes (see [[BGP Path Selection]]) and manipulates them ([[Local Preference]], [[MED]], [[Communities]]) for control.

## Exam Focus

- **BGP neighbors must be configured explicitly** (no multicast discovery like IGPs).
- **iBGP ≠ eBGP:** same protocol, different rules (TTL, next-hop, loop prevention — see [[eBGP]] / [[iBGP]]).
- BGP is policy-driven: **trade speed of convergence for control** — expect "which attribute..." questions.

## Related Terms

- [[eBGP]], [[iBGP]], [[BGP Path Selection]], [[AS Path]], [[Local Preference]], [[MED]], [[Communities]], [[Route Reflector]], [[Confederation]], [[BGP Aggregation]]
- Level 12 notes: [[Level 12 - BGP/BGP Overview]]