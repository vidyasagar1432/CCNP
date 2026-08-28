---
tags: [CCNP, glossary, mpls, networking]
aliases: ["FEC", "Forwarding Equivalence Class", "FEC Assignment"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# FEC

## Definition

A **FEC (Forwarding Equivalence Class)** is the MPLS grouping rule: **all packets that should be forwarded the same way** (same destination prefix, same next hop, same service, same QoS) get **one label**. The [[LER]] classifies each incoming packet into a FEC at ingress — after that, the whole class is carried by a single label binding, and the core never re-asks.

## The Mapping

```text
FEC definition: e.g. "destination 10.1.0.0/16 via X"
binding: FEC ⇄ label 101 (advertised by downstream LSR via LDP)
effect: one FEC = one LSP; many packets, one label
granularity choices: per-prefix, per-VPN, per-service — coarser = fewer labels
```

## Exam Focus

- **"What determines the label a packet gets?" → its FEC** — the classification concept; "what IS a FEC?" → the equivalence-class definition.
- **One FEC = one LSP = one label** — the binding chain question.
- Ingress does FEC assignment once; core can't re-classify — "where does classification happen?" → LER only.
- Coarse vs fine FECs (destination-based vs per-service) — the design trade-off question.

## Related Terms

- [[MPLS]], [[MPLS Label]], [[LER]], [[MPLS VPN]]
- Level 20 notes: [[Level 20 - MPLS/06. FEC]]