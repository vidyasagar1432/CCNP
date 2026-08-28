---
tags: [CCNP, glossary, nat]
aliases: ["Static Translation"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Static NAT

## Definition

**Static NAT** is a permanent, one-to-one mapping between an [[Inside Local Address]] and an [[Inside Global Address]], configured by hand and independent of traffic.

```text
Inside Local        Inside Global
10.0.0.10  ◄──────►  203.0.113.10
```

The mapping exists — and consumes the global address — even with **no active traffic**.

## How It Works

```cisco
ip nat inside source static 10.0.0.10 203.0.113.10

interface GigabitEthernet0/0
 ip nat inside
interface GigabitEthernet0/1
 ip nat outside
```

- Outbound: source `10.0.0.10` → `203.0.113.10`
- Inbound: destination `203.0.113.10` → `10.0.0.10`

## Key Characteristics

| Aspect | Behavior |
| --- | --- |
| Mapping | Fixed 1:1 |
| Creation | Configuration, not traffic |
| Pool | Not required |
| Inbound initiation | Predictable (a permanent mapping exists) |
| Port translation | No (unless "static PAT") |
| Timeout | No dynamic aging |

## Exam Focus

- **Static NAT ≠ automatically reachable.** Inbound connectivity still needs: a route to the inside host, reachability to the inside-global address, a valid return path, and ACL/firewall permitting the traffic.
- The static mapping exists even when idle — that is why it is the tool for **predictable inbound access**.
- `ip nat inside source static tcp 192.168.10.100 443 203.0.113.100 443` is **static PAT** (port-level static translation), used for inbound services.

## Related Terms

- [[Dynamic NAT]], [[PAT]], [[Inside Local Address]], [[Inside Global Address]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/01. Static NAT]], [[Level 15 - NAT/06. Troubleshooting]]