---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["IPv4 Multicast", "Multicast Address", "Class D"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# IPv4 Multicast

## Definition

**IPv4 multicast** sends one stream to a **group** of interested receivers via **Class D addresses (224.0.0.0/4)** — one-to-many, routable, and far more efficient than unicast copies or broadcast. Delivery is driven by group membership ([[IGMP]]) and group-based routing ([[PIM]]).

## Address Structure

| Range | Name | Scope |
| --- | --- | --- |
| 224.0.0.0/24 | Link-local | Every device on a link (e.g. 224.0.0.5 OSPF, 224.0.0.9 RIPv2, 224.0.0.10 EIGRP) |
| 224.0.1.0+ | Globally scoped | Routed groups across the network |
| 239.0.0.0/8 | Admin. scoped | Private/org-local range |

## Exam Focus

- **"Which multicast groups are never routed?"** → 224.0.0.0/24 (link-local) — no TTL propagation beyond the segment.
- L2 mapping: IPv4 multicast MAC = `01:00:5E:xx:xx:xx` (low 23 bits of the IP).
- Router protocols listening: OSPF `224.0.0.5/6`, EIGRP `224.0.0.10` — link-local hello groups.

## Related Terms

- [[IPv4]], [[IPv4 Classes]], [[IGMP]], [[PIM]]
- Level 05 notes: [[Level 05 - IPv4/10. Multicast]]