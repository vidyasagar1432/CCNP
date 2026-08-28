---
tags: [CCNP, glossary, nat, ipv6]
aliases: ["IPv6 to IPv4 Translation", "Stateful NAT64"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT64

## Definition

**NAT64** lets **IPv6-only clients reach IPv4-only servers** by translating traffic between the two address families. It is the modern IPv6↔IPv4 transition/translation mechanism (replacing the deprecated NAT-PT).

```text
IPv6 client  ──►  NAT64 translator  ──►  IPv4 server
2001:db8:10::10      │                   198.51.100.10
                IPv6 ▼
                198.51.100.10   (IPv4 side)
```

## How It Works

The classic deployment combines:

| Component | Role |
| --- | --- |
| IPv6-only client | Initiates traffic; has no IPv4 stack |
| [[DNS64]] | Synthesizes an AAAA record for the IPv4 server |
| NAT64 translator | Rewrites IPv6 packets to IPv4 and back |
| IPv4-only server | Unaware it is being reached via translation |

The client talks to a synthesized IPv6 destination built on the **NAT64 Well-Known Prefix** `64:ff9b::/96` with the IPv4 address in the last 32 bits:

```text
192.0.2.10   ──►   64:ff9b::c000:020a
```

## Stateful vs Stateless

| Feature | Stateful NAT64 | Stateless NAT64 |
| --- | --- | --- |
| Translation state | Maintained (per-flow) | Algorithmic, no per-flow state |
| Address sharing | Many IPv6 → smaller IPv4 pool | Generally 1:1 mapping |
| Port translation | Common for address sharing | No |

## Exam Focus

- **Primary direction is IPv6 → IPv4.** It does *not* automatically provide inbound IPv4-initiated access to IPv6 hosts.
- NAT64 ≠ PAT: PAT is IPv4→IPv4; NAT64 is IPv6→IPv4.
- **Routing still required on both sides**: IPv6 route to `64:ff9b::/96` toward the translator, and IPv4 reachability from it.
- Classic exam trap: **DNS64 is not NAT64** — DNS64 only changes DNS answers; NAT64 translates packets.
- Related architecture: **464XLAT** (CLAT on the client side + PLAT/NAT64 provider-side) for IPv4 apps over IPv6-only mobile networks.
- NAT64 syntax is platform/IOS XE release-specific — verify per platform.

## Related Terms

- [[DNS64]], [[NAT]], [[PAT]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/05. NAT64]], [[Level 06 - IPv6/IPv6 Overview]]