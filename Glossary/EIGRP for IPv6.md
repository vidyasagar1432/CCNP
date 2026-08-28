---
tags: [CCNP, glossary, eigrp, routing, ipv6]
aliases: ["EIGRP for IPv6"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# EIGRP for IPv6

## Definition

**EIGRP for IPv6** runs the same DUAL/RTP engine over IPv6. It is **not** a new protocol — the algorithm, metrics, and convergence behavior are identical; only the addressing and configuration scaffolding differ.

## IPv6 vs IPv4 Differences

| Aspect | EIGRP IPv4 | EIGRP IPv6 |
| --- | --- | --- |
| Hellos | 224.0.0.10 | **FF02::A** |
| Configuration | `router eigrp <as>` + `network` | `address-family ipv6` — **no `network`**; enable per-interface |
| Router ID | Auto-derived | **Must be configured** (or a `router-id`) |
| Adjacency | Interface IPv4 address | **Link-local** addresses |
| Classic CLI | Separate process | Named mode unifies both AFs |

```cisco
router eigrp CCNP-NET
 address-family ipv6 unicast autonomous-system 100
  af-interface GigabitEthernet0/0
  exit-af-interface
  topology base
interface GigabitEthernet0/0
 ipv6 eigrp CCNP-NET
```

## Exam Focus

- **EIGRP for IPv6 requires a configured router-id and manual interface activation** (no `network` statement) — the pair of traps exam writers love.
- Multicast address differs: FF02::A vs 224.0.0.10.
- Named mode handles both address families under one process (see [[Named Mode EIGRP]]).

## Related Terms

- [[EIGRP]], [[Named Mode EIGRP]], [[OSPFv3]] (the IPv6 twin of OSPF)
- Level 11 notes: [[Level 11 - EIGRP/06. IPv6]]