---
tags: [CCNP, glossary, nat]
aliases: ["Network Address Translation"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT

## Definition

**Network Address Translation (NAT)** is the process of rewriting the source and/or destination IP address (and with PAT, Layer-4 port) of packets as they pass through a router, so the addresses seen on one side of the boundary differ from those on the other side.

## How It Works

A NAT device decides — based on **inside/outside interface roles** and a **NAT rule** — which packets to translate and how. Every active translation is recorded in the [[NAT Translation Table]].

```text
Inside host  ──►  NAT router  ──►  Outside network
10.0.0.10         203.0.113.10

        IP packet rewritten at the NAT boundary
```

NAT is **direction-aware**:

| Term | Meaning |
| --- | --- |
| Inside | The network the translation is "for" — normally the private side |
| Outside | The network the translated address represents — normally the public side |
| Local | An address as it appears on the *inside/private* side of the boundary |
| Global | An address as it appears on the *outside/public* side of the boundary |

These combine into the four address terms: [[Inside Local Address]], [[Inside Global Address]], [[Outside Local Address]], [[Outside Global Address]].

## Types

| Type | Mapping | Notes |
| --- | --- | --- |
| [[Static NAT]] | Fixed 1:1 | Predictable inbound access |
| [[Dynamic NAT]] | Temporary 1:1 | Allocated from a [[NAT Pool]] |
| [[PAT]] | Many:1 | Shares one global address via ports |
| [[Outside Source NAT]] | Outside host's address rewritten | Overlapping-space designs |

## Exam Focus

- NAT **changes addresses** — it does not repair routing and does not override security policy.
- NAT classification uses an [[NAT ACL]]; that ACL is **not** a security filter.
- The **inside/outside** and **local/global** axes are the single most-tested distinction in NAT.
- NAT64 ([[NAT64]]) is a *different* family: it translates between IPv6 and IPv4, not between RFC 1918 and public IPv4.

## Related Terms

- [[Static NAT]], [[Dynamic NAT]], [[PAT]], [[NAT Pool]], [[NAT Translation Table]], [[NAT ACL]], [[NAT64]]
- Level 15 notes: [[Level 15 - NAT/NAT Overview]]