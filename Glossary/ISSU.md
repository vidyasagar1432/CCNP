---
tags: [CCNP, glossary, high-availability, networking]
aliases: ["ISSU", "In-Service Software Upgrade", "Hitless Upgrade"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: High Availability
created: 2026-08-29
---

# ISSU

## Definition

**ISSU (In-Service Software Upgrade)** upgrades IOS XE on a **dual-supervisor/RP** device **without a maintenance window**: it runs **[[SSO]]** state sync plus **[[NSF]]** so the standby takes over (with new software) while the active keeps serving, then roles flip back. Result: **zero-disruption software change** on the box.

## The ISSU Roll

```text
1. load new image on standby (RP keeps running old code)
2. SSO switchover → standby (new code) becomes active, state intact
3. old active reloads with new image → becomes standby → SSO again
services/features must be ISSU-compatible (check FW support)
```

## Exam Focus

- **"How do you upgrade without downtime?" → ISSU** — the definition; requirement: dual supervisors + SSO/NSF.
- **The two-switchover mechanism**: bring-up standby, flip, flip back — the process question.
- ISSU vs reload/NBD upgrade: downtime vs none — the O&M comparison.
- Compatibility caveat: some features halt ISSU (incompatible → full reload) — the planning caveat.

## Related Terms

- [[SSO]], [[NSF]], [[Redundant Supervisors]], [[Cisco IOS]]
- Level 27 notes: [[Level 27 - High Availability/06. ISSU]]