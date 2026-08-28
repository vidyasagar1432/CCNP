---
tags: [CCNP, glossary, high-availability, networking]
aliases: ["Redundant Supervisors", "Dual Supervisor", "Supervisor Redundancy", "RPR", "RPR Plus"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: High Availability
created: 2026-08-29
---

# Redundant Supervisors

## Definition

**Redundant supervisors** give a chassis switch a **standby supervisor** in the second slot so a supervisor failure doesn't take down the box. The **redundancy mode** decides how much state the standby keeps — **RPR** (no state; standby boots/config loads, switchover = brief re-convergence) vs **RPR+** (startup-config + boot state) vs **[[SSO]] + [[NSF]]** (full state sync, lossless). SSO/NSF is the production choice.

## The Modes

| Mode | Standby state | Switchover impact |
| --- | --- | --- |
| RPR | None (cold) | Reload + re-learn (minutes) |
| RPR+ | Config + boot | Faster, still re-converges |
| SSO(+NSF) | Full control-plane state | No forwarding interruption |

## Exam Focus

- **"What protects a chassis from supervisor failure?" → redundant supervisors** — the definition; active/standby pairing.
- **The mode ladder**: RPR → RPR+ → SSO — "which is stateful?" → SSO; "which is cold?" → RPR — the matrix question.
- **Why SSO is the standard**: state sync = no flap — the design answer; NSF rides on top for routing.
- Requirement: dual supervisors = chassis devices (4500/6500/9500) — the platform context.

## Related Terms

- [[SSO]], [[NSF]], [[High Availability]], [[ISSU]]
- Level 27 notes: [[Level 27 - High Availability/03. Redundant Supervisors]]