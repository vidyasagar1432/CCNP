---
tags: [CCNP, glossary, mpls, networking]
aliases: ["LFIB", "Label Forwarding Information Base", "Incoming Label Map", "ILM"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# LFIB

## Definition

The **LFIB (Label Forwarding Information Base)** is the MPLS-forwarding table on an [[LSR|LSR]] — the label-to-label engine: **in label → out label + out interface**. Built from label bindings learned via LDP/RSVP + the [[FIB]] (which maps FECs to next hops), the LFIB is what makes core forwarding a pure lookup, no IP decision.

## The LFIB Row

```text
IN label ├─► OUT label   OUT interface   (and typically the outgoing LSP)
101      │   217             g0/1
    actions: SWAP (transit) | POP (PHP) | POP+PUSH (egress into another label)
    miss = drop — there is no IP fallback in the data path
```

## Exam Focus

- **"Which table drives MPLS forwarding?" → LFIB** — vs [[FIB]] (IP forwarding) and [[RIB]] (routes) — the three-table question.
- **LFIB entry anatomy**: in-label/out-label/out-interface — "what's in an LFIB entry?" answer.
- **No LFIB match = drop** — no packet gets unlabeled unless PHP said so — the strictness fact.
- LFIB vs ILM naming: ILM tags the binding; LFIB holds the forwarding result — trivia-level distinction.

## Related Terms

- [[MPLS]], [[FEC]], [[FIB]], [[RIB]], [[LSR]], [[LER]]
- Level 20 notes: [[Level 20 - MPLS/05. LFIB]]