---
tags: [CCNP, glossary, stp, switching]
aliases: ["Root Port", "Designated Port", "Alternate Port", "Backup Port"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# STP Port Roles

## Definition

**STP port roles** describe the **function a port performs** in the spanning-tree topology — what the port is *for*, independent of its current forwarding state. Roles are decided by the tie-breaking sequence (lowest path cost → lowest sender bridge ID → lowest sender port ID).

## The Roles

| Role | Meaning | Typical location |
| --- | --- | --- |
| **Root Port** | Best path toward the root bridge | Every non-root switch has exactly one |
| **Designated Port** | Best port on a segment toward root; the only forwarding role permitted on a segment | One per LAN segment |
| **Alternate Port** | Backup path to the root via *another switch* (rejects the root port's role) | Non-root switch, redundant uplinks |
| **Backup Port** | Backup path toward the *same segment / same switch* | Two links to the same segment |

## Role Logic

```text
Decision per port:
1. Lowest root bridge ID        → determines the root
2. Lowest root path cost        → Root Port (forwarding)
3. Lowest sender bridge ID      → Designated Port (forwarding)
4. Lowest sender port ID        → final tie-break
Everything else → Alternate / Backup (blocking)
```

## Exam Focus

- **Do not confuse role with state.** A [[STP Port Roles|Root Port]] can be in a *blocking* state (classic STP) — role = logical function, state = current forwarding behavior (see [[STP Port States]]).
- RSTP keeps the same roles but adds rapid role transitions via Proposal/Agreement.
- Blocking is **not a role** — it is a *state*; the blocked port still holds a role like Alternate.

## Related Terms

- [[STP]], [[Root Bridge]], [[STP Port States]], [[STP Path Cost]], [[Bridge ID]], [[RSTP]]
- Level 08 notes: [[Level 08 - STP/07. Port Roles]]