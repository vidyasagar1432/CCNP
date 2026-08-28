---
tags: [CCNP, glossary, nat]
aliases: ["Inside Global"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Inside Global Address

## Definition

The **inside global address** is the address that *represents an inside host to the outside network* — in practice, the public address assigned by the NAT rule. It is the translated version of the [[Inside Local Address]].

## How It Works

- For outbound traffic: the NAT router rewrites the source from the inside local address to the inside global address.
- For inbound traffic: the router rewrites the destination from the inside global address back to the inside local address.

```text
Outbound:  src 10.0.0.10   ──►  src 203.0.113.10
Inbound:   dst 203.0.113.10 ──►  dst 10.0.0.10
```

## Where Inside Global Addresses Come From

| Type of NAT | Source of the inside global address |
| --- | --- |
| [[Static NAT]] | Fixed address in the config (`ip nat inside source static ...`) |
| [[Dynamic NAT]] | Allocated from a [[NAT Pool]] |
| [[PAT]] | The outside interface address or a [[NAT Pool]] with [[NAT Overload]] |

## Exam Focus

- One inside local address **can map to one inside global address at a time** in dynamic NAT; the address is only *borrowed*, not owned, by the host (see [[NAT Pool]] exhaustion).
- With PAT, many inside local addresses share **one** inside global address distinguished only by Layer-4 port — the fundamental [[PAT]] vs [[Dynamic NAT]] difference.
- In `show ip nat translations`, the inside global column shows what the outside world actually sees as the source.

## Related Terms

- [[Inside Local Address]], [[NAT Pool]], [[Static NAT]], [[Dynamic NAT]], [[PAT]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/01. Static NAT]], [[Level 15 - NAT/02. Dynamic NAT]]