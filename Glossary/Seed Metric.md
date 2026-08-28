---
tags: [CCNP, glossary, routing, redistribution]
aliases: ["Seed Metric", "Default Metric", "Redistribution Metric"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Route Redistribution
created: 2026-08-29
---

# Seed Metric

## Definition

The **seed metric** is the cost a redistributed route starts with inside its **new protocol** — assigned by the [[Route Redistribution|redistributing]] router. Every protocol has its own default: OSPF external **20**, EIGRP **infinite (not advertised!)**, RIP **infinity (not advertised)** — which is why "I redistributed but nothing shows" is usually Seed Metric 101.

## Defaults That Bite

| Protocol | Default seed metric | Result if unset |
| --- | --- | --- |
| OSPF (external) | 20 | Advertised as E2 cost 20 (works) |
| EIGRP | Infinite (huge) | NOT advertised — "no route" symptom |
| RIP | Infinity (16) | NOT advertised |
| IS-IS | 0 (or unset) | 0 = default metric elsewhere |

```text
router eigrp 100
  redistribute ospf 100 metric 10000 100 255 1 1500
                     (bandwidth kbps, delay, reliability, load, MTU)
router ospf 100
  redistribute eigrp 100 subnets                (metric 20 default, E2)
  redistribute static subnets metric-type 1 metric 30
```

## Exam Focus

- **"Why don't redistributed EIGRP routes appear?" → missing seed metric** — EIGRP/RIP never advertise without one; OSPF has a usable default (20).
- The **`subnets` keyword** in OSPF: without it, only **classful** routes are redistributed — the second most-asked redistribute fact.
- Changing the seed metric = **`metric-type` + `metric`** on OSPF side; the EIGRP `metric` list order (BW delay reliability load MTU) is a recognition question.

## Related Terms

- [[Route Redistribution]], [[Route Tag]], [[Metrics]], [[OSPF]], [[EIGRP]]
- Level 13 notes: [[Level 13 - Route Redistribution/04. Seed Metrics]]