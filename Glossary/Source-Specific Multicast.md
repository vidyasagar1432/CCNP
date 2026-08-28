---
tags: [CCNP, glossary, multicast, routing]
aliases: ["Source-Specific Multicast", "SSM", "PIM SSM"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# Source-Specific Multicast

## Definition

**SSM (Source-Specific Multicast)** delivers **group traffic from ONE specified source**: receivers join **(S,G)** — "give me group G from source S" — rather than (*,G) any-source. Built on **IGMPv3** (hosts request sources) + **PIM-SSM** (no RP, no shared tree — direct source trees only). Result: simpler, more secure, more efficient than PIM-SM for known sources.

## The Model

```text
receiver knows source S (via directory/DNS) → IGMPv3 (S,G) join
first-hop router → PIM (S,G) join toward S → direct SPT, no RP at all!
whole 232.0.0.0/8 is the standard SSM range
benefits: no RP, no shared tree, no unwanted sources, easier to secure
```

## Exam Focus

- **"Which multicast model joins specific sources only?" → SSM** — the (S,G) versus (*,G) tell.
- **Dependencies**: IGMPv3 on hosts + PIM-SSM on routers — "what must be deployed for SSM?" answer.
- **232.0.0.0/8** = SSM range — the address-pool question (vs 239/8 administrative scope).
- Why choose SSM: known-source apps (IPTV, trading feeds) — no RP complexity, spoof-joins limited — the "when SSM?" design answer.

## Related Terms

- [[PIM]], [[PIM-SM]], [[IGMP]], [[Rendezvous Point]]
- Level 19 notes: [[Level 19 - Multicast/07. Source-Specific Multicast]]