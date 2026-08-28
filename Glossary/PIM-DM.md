---
tags: [CCNP, glossary, multicast, routing]
aliases: ["PIM Dense Mode", "PIM-DM", "Flood and Prune"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# PIM-DM

## Definition

**PIM Dense Mode (PIM-DM)** uses the **flood-and-prune** model: on a new source, traffic is flooded to every router; branches **without receivers send prunes**, and only the receiving tree stays active. Simple, zero-config (no RP), but wasteful on sparse WANs — the "dense" fit is LAN-ish, receiver-rich networks.

## The Behavior

```text
source (S,G) starts → flood everywhere (like a broadcast)
leaf without receivers → PIM prune message upstream (state: PRUNED)
prune timeout → re-flood (refresh mechanism; state aging)
best when receivers are everywhere; worst where one source → few receivers
```

## Exam Focus

- **"Which PIM mode floods first and prunes later?" → dense mode** — the mechanism definition.
- **"What is PIM-DM's advantage?" → no RP, no joins — simple**; "its cost?" → bandwidth waste on sparse links — the trade-off pair.
- Dense = implicit join (default on), sparse = explicit join — the philosophical difference sentence.
- Modern practice: almost nothing runs dense on WANs — sparse + SSM dominate; "why?" is the forwarding-efficiency answer.

## Related Terms

- [[PIM]], [[PIM-SM]], [[Rendezvous Point]], [[Reverse Path Forwarding]]
- Level 19 notes: [[Level 19 - Multicast/02. PIM Dense]]