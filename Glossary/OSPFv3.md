---
tags: [CCNP, glossary, ospf, routing, ipv6]
aliases: ["OSPFv3", "OSPF for IPv6"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# OSPFv3

## Definition

**OSPFv3 (RFC 5340)** is OSPF for **IPv6** — same link-state mechanics, Dijkstra SPF, areas, and neighbor state machine as [[OSPF|OSPFv2]], but redesigned to run over IPv6 and to be **address-family independent**.

## Key Differences from OSPFv2

| Aspect | OSPFv2 | OSPFv3 |
| --- | --- | --- |
| Address family | IPv4 only | IPv6 (and IPv4 via `address-family ipv4`) |
| Adjacencies | Interface IPv4 addresses | **Link-local** addresses |
| Router ID | In the packet | Explicit (still required, IPv4-style) |
| Authentication | Field in packet | **IPsec** (AH/ESP) |
| LSA payloads | Carry IPv4 prefixes | Prefixes in separate, new LSA types |
| Network type / DR-BDR | Same | Same ([[DR BDR]] still exists) |

New LSA types in v3 handle IPv6 prefixes and link-local addressing, so the core router/network LSAs no longer embed addresses directly.

## How It Works

```cisco
interface GigabitEthernet0/0
 ipv6 address 2001:db8:10::1/64
interface GigabitEthernet0/0
 ipv6 ospf 1 area 0

router ospf 1
 router-id 1.1.1.1
```

## Exam Focus

- **OSPFv3 neighbors speak over link-local addresses** — interfaces need IPv6 enabled, not necessarily a global address on that link.
- **Router ID is still configured identically**, even though v3 is IPv6-native.
- v3 authentication = IPsec; MD5-in-header is v2-only (see [[OSPF Authentication]]).
- The SPF, areas, and election logic are the same — focus on *what changed*, not on relearning OSPF.

## Related Terms

- [[OSPF]], [[OSPF Area]], [[OSPF Router ID]], [[DR BDR]], [[OSPF Authentication]]
- Level 10 notes: [[Level 10 - OSPF/02. OSPFv3]]