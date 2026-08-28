---
tags: [CCNP, glossary, stp, switching]
aliases: ["Multiple Spanning Tree Protocol", "IEEE 802.1s", "MSTI", "CIST", "IST"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# MST

## Definition

**MST (Multiple Spanning Tree, 802.1s, now part of 802.1Q)** reduces STP scale by mapping **many VLANs to a small number of spanning-tree instances**, instead of one instance per VLAN ([[PVST+]]).

## Key Concepts

| Term | Meaning |
| --- | --- |
| MST instance (MSTI) | A spanning-tree instance carrying a set of VLANs |
| MST region | Group of switches sharing the same instance→VLAN mapping, revision, and name |
| IST / CIST | Common (Internal) Spanning Tree connecting regions as one classic STP tree |
| CIST root | The root of the whole MST/Multiple regions topology |

VLAN mapping is configured per region; switches agree on a mapping via their configuration, so **consistency matters**:

```text
Region A: VLANs 1-10 → instance 1, VLANs 11-20 → instance 2
```

## Why MST

- Scales better than PVST+ on large networks (fewer instances, fewer BPDUs).
- Retains rapid convergence because it uses **RSTP mechanisms**.
- Enables per-instance load balancing.

## Exam Focus

- **MST ≠ simply "PVST+ with less overhead."** It is a standards-based hierarchy (region → instance → CIST) with different inter-region behavior.
- **All switches in a region must agree** on name, revision, and VLAN mapping; a mismatch splits regions.
- MST is **not** "not having a root" — the CIST still has a root; instances use RSTP logic.

## Related Terms

- [[STP]], [[RSTP]], [[PVST+]], [[Root Bridge]]
- Level 08 notes: [[Level 08 - STP/05. MST]]