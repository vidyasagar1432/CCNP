---
tags: [CCNP, glossary, physical, networking, ethernet]
aliases: ["Full Duplex", "Half Duplex", "Duplex Mismatch"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Duplex

## Definition

**Duplex** describes whether a link transmits and receives **simultaneously (full duplex)** or one direction at a time (**half duplex**). Modern Ethernet is full duplex on dedicated switch ports; half duplex survives only on legacy hubs/some wireless.

## Full vs Half

| | Half duplex | Full duplex |
| --- | --- | --- |
| Send/receive | One at a time | Simultaneous |
| Collisions | Possible (CSMA/CD) | **None** (separate Tx/Rx pairs) |
| Effective speed | ≤ half the line rate | Full line rate |
| Where | Legacy hubs, 10/100 only | All modern switched links |

## Duplex Mismatch — the Failure Mode

```text
one side full, other half → the half side thinks collisions happened
                        → late collisions + FCS errors + retries → slow link
```

- Cause: manual config vs failed [[Ethernet]] auto-negotiation.
- Show: "input errors / late collisions" on the half side; intermittent TCP slowness.

## Exam Focus

- **Full duplex require both ends to agree — mismatch is a top-10 physical troubleshooting story**.
- Half-duplex devices must run CSMA/CD; full duplex disables it.
- Switch-to-switch and switch-to-host are full duplex by default today; hubs were the half-duplex exception.

## Related Terms

- [[Ethernet]], [[Auto-Negotiation]], [[Ethernet Standards]]
- Level 01 notes: [[Level 01 - Physical Layer/02. Ethernet/02. Duplex]]