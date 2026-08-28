---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["Route Summarization", "Summarization", "Summary Route", "Route Aggregation"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# Summarization

## Definition

**Route summarization** collapses **multiple contiguous prefixes into one shorter prefix** advertised upstream, so neighbors carry one route instead of many. The secret: find the common bits — the summary is the network and mask of the **lowest common prefix**.

## How to Summarize

```text
10.1.0.0/24, 10.1.1.0/24, 10.1.2.0/24, 10.1.3.0/24
  └─ all under /16? → too broad. Find bound:
  contiguous block of 4 → 10.1.0.0/22   (aligns on a /22 boundary)
```

```text
Rules of thumb:
  • the summary must start on a multiple of its block size
  • you cannot summarize non-contiguous ranges into one route
  • longer-summary = fewer routes = smaller tables
    (a "2^n networks of /X summarize into /X−n")
```

## Exam Focus

- **"Given four /24s, what is the best summary?"** → find the biggest mask that covers them exactly (aligns on a boundary) — classic math question.
- **Summarization hides failures** (a flap inside the block isn't seen upstream) — good for stability, a trap for troubleshooting.
- EIGRP/OSPF both support manual summarization; EIGRP auto-summarizes at classful boundaries by default (off in named mode).

## Related Terms

- [[CIDR]], [[Supernetting]], [[Route Aggregation]], [[VLSM]]
- Level 05 notes: [[Level 05 - IPv4/14. Summarization]]