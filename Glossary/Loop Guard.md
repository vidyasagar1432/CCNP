---
tags: [CCNP, glossary, stp, switching]
aliases: ["Loop Guard", "LoopGuard", "Unidirectional Link"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# Loop Guard

## Definition

**Loop Guard** protects STP from **unexpected [[BPDU]] loss on non-designated ports**. If a link fails unidirectionally (or BPDUs silently stop), a blocking/alternate port could wrongly transition to forwarding and create a **Layer-2 loop**. Loop Guard holds such ports in a **loop-inconsistent (blocking) state** instead.

## How It Works

```cisco
interface GigabitEthernet0/1
 spanning-tree guard loop
```

```text
Expected BPDUs stop arriving on a non-designated port
      ↓
Port → loop-inconsistent (blocking), not forwarding
      ↓
When BPDUs resume → port recovers to normal role/state
```

## What It Actually Detects

- **Unidirectional link failures** (fiber one strand down, faulty port)
- Any condition where traffic flows but BPDUs do not arrive

It differs from [[UDLD]] (which detects *physical* unidirectional links); Loop Guard works at the logical/BPDU level.

## Exam Focus

- Loop Guard is about **unexpected BPDU loss** — not about rogue switches (that is [[BPDU Guard]] / [[Root Guard]]).
- Configure it on **non-designated (alternate/backup) ports**, where a silent failure would hurt most.
- State shown in `show spanning-tree` is **loop-inconsistent** — that state is *not* the same as errdisable and recovers automatically.

## Related Terms

- [[BPDU]], [[STP Port Roles]], [[BPDU Guard]], [[Root Guard]], [[STP]]
- Level 08 notes: [[Level 08 - STP/13. Loop Guard]]