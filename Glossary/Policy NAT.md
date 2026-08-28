---
tags: [CCNP, glossary, nat]
aliases: ["Policy-Based NAT", "NAT by ACL", "Conditional NAT"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Policy NAT

## Definition

**Policy NAT** applies NAT **conditionally**, matching not just the source address but additional traffic characteristics — destination, protocol, ports — so different flows can be translated (or not) in different ways.

```text
Regular NAT:   Source matches          → Translate
Policy NAT:    Source + Destination + Protocol/Port match → Translate per policy
```

## How It Works

Selectivity is achieved with an **extended ACL**:

```cisco
! Only traffic from 10.0.0.0/24 TOWARD 198.51.100.0/24 is eligible
access-list 101 permit ip 10.0.0.0 0.0.0.255 198.51.100.0 0.0.0.255
ip nat inside source list 101 pool ISP-A overload
```

Or with a **route-map**:

```cisco
route-map NAT-POLICY permit 10
 match ip address 101

ip nat inside source route-map NAT-POLICY interface GigabitEthernet0/1 overload
```

A route-map used by NAT controls **NAT classification**, not routing.

## Common Use Cases

| Use case | Purpose |
| --- | --- |
| Multi-ISP | Different public pools per destination (ISP-A vs ISP-B) |
| Destination-specific NAT | Translate only flows to selected networks |
| Service-specific NAT | TCP/UDP port-based policies (e.g. only port 443) |
| Overlapping networks | Selective translation between colliding spaces |
| VPN traffic | Exclude specific traffic from NAT ("no NAT" policy) |

## Exam Focus

- **Policy NAT ≠ PBR.** Policy NAT decides *whether/how to translate*; PBR decides *where to forward*. Both can use route-maps — the purpose differs.
- Policy NAT ≠ [[Outside Source NAT]].
- A **broad NAT rule can swallow selective policies** — overlapping rules interact according to Cisco NAT processing; make conditions specific and verify with `show ip nat translations`.

## Related Terms

- [[NAT]], [[NAT ACL]], [[Outside Source NAT]], [[PAT]]
- Level 15 notes: [[Level 15 - NAT/04. Policy NAT]]