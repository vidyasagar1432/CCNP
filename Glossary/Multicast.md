---
tags: [CCNP, glossary, multicast, networking]
aliases: ["Multicast", "IP Multicast", "Multicast Group"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# Multicast

## Definition

**Multicast** is **one-to-many** delivery: a source sends **one stream to a group address**, and the network replicates it **only along paths with receivers**. It beats unicast (N copies), broadcast (everyone gets it), and scales for IPTV, market data, and conferencing — at the price of **state, membership management, and protocol complexity** (IGMP/PIM).

## The Model at a Glance

```text
source S ──► one packet to group G
receivers: join G (IGMP — host side)
routers: build tree to G (PIM — router side), replicate at branch points
switches: prune ports (IGMP snooping)
addresses: IPv4 224.0.0.0/4 (Class D), IPv6 ff00::/8
```

| vs | Unicast | Broadcast | Multicast |
| --- | --- | --- | --- |
| Receivers | One | All | Subscribed group only |
| Efficiency | Poor for many | Wastes bandwidth | Optimal |
| Delivery state | None | None | Group trees (S,G) |

## Exam Focus

- **Multicast needs three planes**: hosts (IGMP), routers (PIM/MRP), switches (snooping) — "list the multicast protocols" questions split along those lines.
- The **RPF** rule guarantees loop-free trees — the forward sanity check.
- Scope: link-local groups (224.0.0.0/24) never route; admin-scoped 239/8 = org-internal; SSM 232/8 = source-specific — the address-scope table.

## Related Terms

- [[IPv4 Multicast]], [[IGMP]], [[PIM]], [[IGMP Snooping]], [[Reverse Path Forwarding]], [[Source-Specific Multicast]]
- Level 19 notes: [[Level 19 - Multicast/Multicast Overview]]