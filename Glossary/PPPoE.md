---
tags: [CCNP, glossary, wan, networking]
aliases: ["PPPoE", "PPP over Ethernet", "PADI", "PADO", "PADR", "PADS"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# PPPoE

## Definition

**PPPoE (PPP over Ethernet)** carries a [[PPP]] session **inside Ethernet frames** — the standard for **DSL/broadband** access (note 05). A 4-step **discovery** (PADI → PADO → PADR → PADS) finds the access concentrator and creates a session ID, then normal **LCP/CHAP/IPCP** run inside — giving broadband the same authentication and IP assignment PPP offers on serial links.

## The Discovery Dance

```text
PADI  — client shouts "any DSLAM/BRAS out there?"
PADO  — server offers a session
PADR  — client requests one
PADS  — server grants it (session ID!)
then: LCP → (CHAP auth) → IPCP → IP over the session
```

## Exam Focus

- **"How does DSL hand out session + auth?" → PPPoE discovery then PPP inside** — the mechanism; the four PAD messages in order.
- **Why PPPoE on broadband?** → carrier-friendly AAA + IP assignment + session accounting — the "why not DHCP?" answer (both exist: PPPoE vs IPoE).
- **MTU/MTU discovery pain**: PPPoE → MRU 1492 → the classic fragmentation/MSS-clamping issue — the troubleshooting scenario.
- Session terminates at the **BRAS/BNG** (access concentrator) — the device fact.

## Related Terms

- [[PPP]], [[Broadband]], [[DHCP]], [[CHAP]]
- Level 23 notes: [[Level 23 - Enterprise WAN/02. PPPoE]]