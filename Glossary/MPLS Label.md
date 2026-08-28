---
tags: [CCNP, glossary, mpls, networking]
aliases: ["MPLS Label", "Label", "Label Stack", "Penultimate Hop Popping", "PHP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# MPLS Label

## Definition

An **MPLS label** is a **20-bit shim header** inserted between the L2 and L3 headers, carrying the forwarding decisions: exactly **which label value** a packet carries determines per-hop behavior via the [[LFIB]]. A packet can carry a **label stack** (e.g. transport label + VPN label). Special values: **3 = PHP (penultimate hop popping)** — ask the penultimate router to pop before the egress.

## The Label Structure

| Field | Bits | Purpose |
| --- | --- | --- |
| Label | 20 | The forwarding value (16–1,048,575 usable) |
| EXP/TC | 3 | QoS / class of service |
| S | 1 | Bottom of stack flag |
| TTL | 8 | Time-to-live (loop protection) |

## Exam Focus

- **The four fields and their sizes** — the memory question; label value in the 20-bit field.
- **PHP (label 3)**: egress advertises implicit-null so the **penultimate** router pops — "who pops the label in PHP?" → the penultimate hop, not the egress — classic trick question.
- **Label stack**: outer = path, inner = service (VPN) — the two-label L3VPN structure.
- Scope: 0–15 reserved (explicit-null 0, implicit-null 3); labels are local per-hop, swapped hop to hop — the "labels are locally significant" fact.

## Related Terms

- [[MPLS]], [[LFIB]], [[FEC]], [[MPLS VPN]]
- Level 20 notes: [[Level 20 - MPLS/02. Labels]]