---
tags: [CCNP, glossary, stp, switching]
aliases: ["Root Guard", "RootGuard"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# Root Guard

## Definition

**Root Guard** protects the **intended [[Root Bridge]] placement**. It is enabled on ports where the switch must stay **Designated**; if a **superior BPDU** (claiming to be closer to a better root) arrives on such a port, the port is put into the **root-inconsistent state** (blocking) instead of accepting the new root.

## How It Works

```cisco
interface GigabitEthernet0/1
 spanning-tree guard root
```

```text
Superior BPDU received on Root-Guard port
      ↓
Port → root-inconsistent (blocking)
      ↓
If superior BPDUs stop → port returns to normal (designated/forwarding)
```

## Where It Belongs

- On ports toward **access-layer / edge switches** where a rogue or misconfigured switch must never overtake the root.
- **Not** on ports toward the intended root — that would block legitimate superior BPDUs.
- Often combined with PortFast-style edge protection but fundamentally different from [[BPDU Guard]].

## Root Guard vs BPDU Guard

| Feature | Root Guard | BPDU Guard |
| --- | --- | --- |
| Trigger | *Superior* BPDU claiming a better root | *Any* BPDU |
| Reaction | Port → root-inconsistent (blocking) | Port → errdisable |
| Scope | Specific to root election | Any STP participation |
| Auto-recovery | Yes, when superior BPDUs cease | No, unless errdisable recovery |

## Exam Focus

- **Root Guard does not shut the port; it blocks it** until the offending superior BPDUs stop.
- Place it to protect root *placement*, not as a general BPDU filter.

## Related Terms

- [[Root Bridge]], [[BPDU]], [[BPDU Guard]], [[STP]]
- Level 08 notes: [[Level 08 - STP/12. Root Guard]]