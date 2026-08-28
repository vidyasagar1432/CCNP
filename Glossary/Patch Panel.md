---
tags: [CCNP, glossary, physical, networking]
aliases: ["Patch Panel", "110 Block"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Patch Panel

## Definition

A **patch panel** is the passive termination point in a wiring closet where **horizontal cabling from wall jacks lands** — patch cords then jump from the panel to the switch ports. It makes adds/moves painless and keeps the structured cable plant untouched.

## How It Works

```text
wall jack ──(horizontal solid-core cable)──► patch panel port
switch port ◄──(patch cord, stranded)─────┘  front of panel
```

- The **solid horizontal run** is terminated once; only the short stranded patch cords change.
- Panels are organized per room/zone; label discipline is everything for troubleshooting.
- Copper panels (Keystone/RJ45) and fiber panels (LC/MPO cassettes) coexist.

## Exam Focus

- **Why panels exist**: protect the expensive horizontal cabling and enable rapid patching — a structured-cabling design question.
- Failure point: **loose/dirty patch-term connections** cause intermittent link flaps; reseating is step 1 of physical troubleshooting.
- The 100 m rule counts panel+patch + horizontal + wall jack (see [[UTP]]).

## Related Terms

- [[UTP]], [[Connectors]], [[Transceiver]]
- Level 01 notes: [[Level 01 - Physical Layer/05. Patch Panels]]