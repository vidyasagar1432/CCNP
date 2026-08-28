---
tags: [CCNP, glossary, stp, switching]
aliases: ["STP Timers", "Hello Timer", "Max Age", "Forward Delay"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# STP Timers

## Definition

**STP timers** pace how quickly the spanning tree detects changes and converges. Classic STP is deliberately slow; these three timers are the engine of that slowness.

## The Three Timers

| Timer | Default | Meaning |
| --- | --: | --- |
| Hello | 2 s | Interval between configuration BPDUs from the root |
| Max Age | 20 s | How long a switch waits without hearing the root before declaring the root dead |
| Forward Delay | 15 s | Time spent in [[STP Port States|Listening]] and in [[STP Port States|Learning]] |

Worst-case classic convergence ≈ **Max Age + 2 × Forward Delay = 50 s**.

## Rules and Constraints

- The **root** drives these values (root's timers win; every switch echoes them in BPDUs).
- `spanning-tree vlan X max-age / forward-time / hello-time` — adjust deliberately, they are diameter-dependent (recommended diameter ≤ 7).

## Exam Focus

- **Do not memorize timer values as universal** — they follow from the root and platform defaults; understand the 50 s classic worst case instead.
- [[RSTP]] keeps hello but **removes the need for the full forward-delay wait** on point-to-point links via Proposal/Agreement — that is the main reason RSTP converges in ~1–3 s.
- Topology changes trigger **TCN BPDUs** (see [[BPDU]]) that shorten MAC aging temporarily — timers play a role there too.

## Related Terms

- [[STP]], [[STP Port States]], [[BPDU]], [[RSTP]], [[Root Bridge]]
- Level 08 notes: [[Level 08 - STP/01. STP]], [[Level 08 - STP/02. RSTP]]