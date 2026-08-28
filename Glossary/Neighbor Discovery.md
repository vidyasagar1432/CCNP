---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["Neighbor Discovery", "NDP", "Neighbor Discovery Protocol", "ICMPv6 NDP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# Neighbor Discovery

## Definition

**Neighbor Discovery (ND/NDP)** is IPv6's replacement for **ARP** — implemented with **ICMPv6** messages: **Neighbor Solicitation (NS)** / **Neighbor Advertisement (NA)** map IPv6 → MAC; **Router Solicitation (RS)** / **Router Advertisement (RA)** distributes prefixes and default routes. DAD uses NS too.

## NS/NA — the "ARP" Table

```text
want MAC for 2001:db8:1:2::10 →
  NS to its solicited-node multicast (no broadcast!)
  owner answers NA (unicast) with its MAC
host cache = NDP neighbor table  (IPv6 analog of ARP cache)
```

| Message | Purpose |
| --- | --- |
| NS / NA | Resolve L2 address; DAD probing |
| RS / RA | Find router, learn prefix + default route ([[SLAAC]]) |
| Redirect | Better next-hop hint |

## Exam Focus

- **"IPv6 hosts use what instead of ARP?" → NDP**, carried in **ICMPv6** (type 135/136 NS/NA, 133/134 RS/RA) — the one-liner they test.
- **DAD (Duplicate Address Detection)**: before using an address, a host NS-probes it — that's the security angle (NDP threats → ND inspection, RA guard).
- NDP neighbors have states just like OSPF: INCOMPLETE → REACHABLE → STALE → DELAY → PROBE — `show ipv6 neighbors` states.

## Related Terms

- [[ICMPv6]], [[IPv6]], [[ARP]], [[SLAAC]], [[Link Local]]
- Level 06 notes: [[Level 06 - IPv6/09. Neighbor Discovery]]