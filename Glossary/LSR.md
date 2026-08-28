---
tags: [CCNP, glossary, mpls, networking]
aliases: ["LSR", "Label Switch Router", "P Router", "Provider Router"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# LSR

## Definition

An **LSR (Label Switch Router)** sits in the **core of the MPLS domain** and forwards purely **by label**: incoming label → [[LFIB]] lookup → swap for the outgoing label → out. No IP longest-prefix lookups in the data path. Providers call it the **P router (Provider)** — it carries the label-switched paths for everyone else's traffic.

## The Core Loop

```text
in packet with label 101 → LFIB → out with label 217 on g0/1
decisions: swap (normal transit), pop (PHP labels / own labels), push (rare in core)
P routers run label distribution (LDP/RSVP-TE) but carry NO customer routes (in L3VPN)
```

## Exam Focus

- **"Which router only swaps labels?" → the LSR/P router** — the role definition; contrast [[LER]].
- **P router properties in VPNs**: no VRF, no customer routes — pure transport — the "what does a P router know?" question.
- LFIB is the LSR's forwarding table — every swap question really asks about the LFIB mechanics.
- Label distribution protocols: LDP (default for IGP routes) vs RSVP-TE (traffic engineering) — the signaling mention.

## Related Terms

- [[MPLS]], [[LER]], [[LFIB]], [[MPLS Label]], [[FEC]]
- Level 20 notes: [[Level 20 - MPLS/04. LSR]]