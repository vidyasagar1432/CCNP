---
tags: [CCNP, glossary, physical, networking, ethernet]
aliases: ["Auto Negotiation", "Speed Negotiation"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Auto-Negotiation

## Definition

**Auto-negotiation** lets two Ethernet devices agree on the **highest common speed and duplex** at link-up, via fast link pulses. It is on by default for copper ports — and the silence when it *fails* is where half of physical-layer troubleshooting starts.

## How It Works

```text
devices exchange base-page messages (speed capabilities + duplex caps)
→ both pick the best common mode:
    prefer higher speed; at equal speed prefer full duplex
```

- **When it fails:** one side manually hard-coded → the other side may fall back to half duplex → **[[Duplex|duplex mismatch]]**, late collisions, retransmissions.
- Fiber ports typically have fixed rates/optics (no negotiation on 10G LR/SR links).
- Best practice: **leave auto on both ends** for copper; hard-set only symmetrically.

## Exam Focus

- **"What do you recommend to fix a flapping/slow port?"** → confirm auto-negotiation on both ends; never hard-code only one side.
- If both ends are hard-coded to the *same* speed+duplex, the link works — mismatch is the killer.
- Auto-neg is L1/L2 — the exam frames it as a physical-layer troubleshooting step.

## Related Terms

- [[Duplex]], [[Ethernet]], [[Ethernet Standards]]
- Level 01 notes: [[Level 01 - Physical Layer/02. Ethernet/03. Speed]]