---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["Anycast", "Anycast Address"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# Anycast

## Definition

**Anycast** is an addressing model where **the same address is assigned to multiple devices**, and the network (routing table) delivers packets to the **nearest** one. IPv6 made anycast a first-class concept; IPv4 uses it too in practice (DNS root servers, CDNs) even without a dedicated block.

## How It Works

```text
2001:db8:aaa::53  ← configured on DNS servers in NY, LA, Frankfurt
routers advertise the /128 (or prefix) to the IGP
a query from Tokyo → routed to the TOPOLOGICALLY nearest advertiser

nearest ≠ fastest always — it's routing-metric nearest (usually good enough)
```

## Anycast Uses (exam favorites)

- **DNS**: root servers + public resolvers anycast → local nearest answer.
- **CDNs**: content replicated across PoPs, one anycast IP → nearest PoP.
- **FHRP-style**: IPv6 anycast can mimic a virtual gateway without HSRP state (each router owns the address; NDP handles it).

## Exam Focus

- **"One address, many devices, nearest wins"** is the definition to repeat.
- Difference from multicast: multicast = many receivers get *copies*; anycast = exactly **one** receiver (the nearest) gets it. Classic multiple-choice separation.
- With anycast, do NOT rely on a single device keeping state — sessions to a failed anycast node get re-routed.

## Related Terms

- [[IPv6]], [[IPv4 Multicast]], [[Neighbor Discovery]], [[DNS]]
- Level 06 notes: [[Level 06 - IPv6/05. Anycast]]