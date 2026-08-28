---
tags: [CCNP, glossary, nat]
aliases: ["Port Address Translation", "NAT Overload", "overload"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# PAT

## Definition

**PAT (Port Address Translation)** — often called **NAT Overload** — lets **many inside hosts share a single inside-global address** by also translating the Layer-4 source port, so each flow is uniquely identified by *address + port*.

```text
10.0.0.10:50001  ──►  203.0.113.1:50001
10.0.0.11:50002  ──►  203.0.113.1:50002
10.0.0.12:50003  ──►  203.0.113.1:50003
```

## How It Works

The router builds a translation for each new flow. If the desired source port is already in use, IOS picks another:

```text
10.0.0.5:12345  ──►  203.0.113.1:23456
```

The requirement: the resulting translation must be **unique enough for the router to map return traffic** to the correct inside host.

Two configuration styles:

```cisco
! Interface PAT (uses the outside interface address)
ip nat inside source list 10 interface GigabitEthernet0/1 overload

! Pool PAT
ip nat inside source list 10 pool PUBLIC overload
```

## Key Characteristics

| Aspect | Behavior |
| --- | --- |
| Mapping | Many:1 |
| Ports translated | Yes (key difference from [[Dynamic NAT]]) |
| Pool | Optional (interface address can be used) |
| Scalability | Very high |
| Exhaustion | Possible — ports and platform resources are finite |

## Exam Focus

- **The `overload` keyword is what enables PAT behavior.** Without it, pool-based NAT stays 1:1 Dynamic NAT.
- PAT is **not** immune to exhaustion — port and translation resources can run out.
- Exam trap: NAT64 ([[NAT64]]) is *not* "PAT for IPv6." PAT is IPv4→IPv4; NAT64 is IPv6→IPv4.

## Related Terms

- [[NAT Overload]], [[Dynamic NAT]], [[Static NAT]], [[NAT Pool]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/03. PAT]], [[Level 15 - NAT/02. Dynamic NAT]]