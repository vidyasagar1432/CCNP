---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["FLSM", "Fixed Length Subnet Mask"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# FLSM

## Definition

**FLSM (Fixed Length Subnet Masking)** gives **every subnet the same prefix length** — simple and predictable, but wasteful when subnet needs vary (a /26 sized for a 60-host LAN also serves your 2-host links, wasting 60 addresses per link).

## The Trade-off

| | FLSM | [[VLSM]] |
| --- | --- | --- |
| Mask | One length for all | Varies per subnet |
| Simplicity | Higher | Lower |
| Address efficiency | Lower | Higher |
| Protocol req. | Works even classful | Needs classless (OSPF/EIGRP) |

```text
/24 split into 4 equal /26 subnets            → FLSM
same /24 split into /26, /27, /28, /30, /30   → VLSM
```

## Exam Focus

- **"Which method uses the same mask everywhere?"** → FLSM — the exact counterpart question to VLSM's.
- Historical: FLSM is what classful routing mandates; [[CIDR]]/VLSM removed that constraint.
- Expect a "how many /28s fit in a /24?" count → **2^(24−28) = 16** — halving per bit.

## Related Terms

- [[VLSM]], [[CIDR]], [[IPv4]]
- Level 05 notes: [[Level 05 - IPv4/13. FLSM]]