---
tags: [CCNP, glossary, switching, vlan]
aliases: ["QinQ", "QQinQ", "802.1Q-in-802.1Q", "VLAN Stacking"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# QinQ

## Definition

**QinQ (802.1Q-in-802.1Q, VLAN stacking)** wraps a customer's **inner 802.1Q tag** inside a **service-provider outer tag** — the provider carries thousands of customers over one trunk while customers keep their own VLAN IDs. It's the classic **carrier Ethernet / Metro-E** handoff mechanism.

## Double Tagging

```text
customer: [VLAN 100 tag] ──► provider edge adds [outer S-tag, e.g. VLAN 2000]
wire:  [S-tag 2000][C-tag 100][payload]        (stacked)

tunneling classification:
  port mode:  the whole port becomes a single tunnel (all traffic)
  selective:  per-VLAN mapping (only certain customer VLANs tunneled)
```

## Exam Focus

- **"Which technology carries customer 802.1Q inside a provider tag?" → QinQ** — the VLAN-stacking definition.
- **QinQ ≠ double-tagging attack**: the *attack* (VLAN hopping) injects a forged inner tag hoping the switch processes only the outer — QinQ is the legitimate stacking implementation.
- Inner tag lives inside the payload; the provider switch sees only the outer S-tag, so MAC learning is per-S-tag ('MAC-in-MAC' has its own variant — know the difference).

## Related Terms

- [[802.1Q]], [[VLAN]], [[Native VLAN]], [[Trunk Port]]
- Level 07 notes: [[Level 07 - VLAN Technologies/09. QinQ]]