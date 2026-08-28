---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["Route Aggregation", "Aggregate Route", "Aggregate"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# Route Aggregation

## Definition

**Route aggregation** is the router-side act of **advertising one aggregate route instead of many specifics** (the forwarding outcome of summarization). Done at routing-protocol level, it shrinks routing tables, reduces protocol churn, and stabilizes the network — e.g. OSPF's `area range`, EIGRP's `summary-address`, and BGP's `aggregate-address`.

## Where Aggregation Happens

```text
OSPF:   area 1 range 10.1.0.0 255.255.252.0   (at the ABR)
EIGRP:  interface ... summary-address 10.1.0.0 255.255.252.0
BGP:    aggregate-address 10.1.0.0 255.255.252.0 [summary-only]
IS-IS:  summary-address 10.1.0.0/22 level-2
```

## Exam Focus

- **"Which component performs aggregation?"** → the boundary device: ABR/ASBR (OSPF), the summarizer (EIGRP), or the BGP speaker advertising the aggregate.
- Aggregates can advertise even when no specific is present (`summary-only` suppresses specifics entirely) — BGP nuance questions.
- Aggregation hides the *breakage* of the underlying specifics — good stability, bad troubleshooting surprise.

## Related Terms

- [[Summarization]], [[Supernetting]], [[CIDR]], [[BGP Aggregation]]
- Level 05 notes: [[Level 05 - IPv4/16. Route Aggregation]]