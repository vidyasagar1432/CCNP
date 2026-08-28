---
tags: [CCNP, glossary, switching, networking]
aliases: ["Cisco Express Forwarding", "CEF", "FIB", "Adjacency Table"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# CEF

## Definition

**Cisco Express Forwarding (CEF)** is Cisco's high-performance IP forwarding architecture: the control plane (routing/[[ARP]]) builds two **pre-computed data structures** — the **FIB** (longest-prefix-ready copy of the routing table) and the **adjacency table** (next-hop L2 rewrite info) — that the data plane uses to forward line-rate.

## The Two Tables

```text
routing table + ARP ──► FIB           (prefix → next hop)
                     └► adjacency table (next hop → L2 rewrite: MAC, egress)
  packet ──► FIB lookup (longest prefix) ──► adjacency (rewrite) ──► forward
```

- **FIB lookup is the data plane's job** — no per-packet route lookup or ARP delay.
- Adjacencies can be "incomplete" (ARP unresolved) — that's the classic "CEF adj incomplete" symptom.
- `ip cef` / `ip cef load-sharing` are the on/off knobs; per-flow load balancing since IOS 12.x.

## Exam Focus

- **"How does a router forward fast without consulting the routing table?"** → CEF: FIB + adjacency pre-built.
- "Adjacency incomplete" → next-hop ARP unresolved → host unreachable — a fast diagnostic.
- CEF is the *control-plane→data-plane* handoff example (see [[Control Plane]] / [[Data Plane]]).

## Related Terms

- [[Control Plane]], [[Data Plane]], [[ARP]], [[Routing Table]], [[Forwarding]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/13. CEF Basics]]