---
tags: [CCNP, glossary, stp, switching]
aliases: ["Path Cost", "STP Cost", "Root Path Cost"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# STP Path Cost

## Definition

**STP path cost** (root path cost) is the cumulative cost of the path from a switch back to the [[Root Bridge]], used to determine which port becomes the [[STP Port Roles|Root Port]]. Lower cost wins.

## Cost Reference (IEEE)

| Link speed | 802.1D cost | 802.1t / Cisco cost |
| --- | --: | --: |
| 10 Mbps | 100 | 100 |
| 100 Mbps | 19 | 19 |
| 1 Gbps | 4 | 4 |
| 10 Gbps | 2 | 2 |

Paths are summed:

```text
SW3 ──1G── SW2 ──100M── SW1(Root)
       4     +    19     = 23
```

## How It Is Used

1. Elect root (see [[Root Bridge]]).
2. Each switch advertises its own root path cost; switches add the local port cost.
3. **Lowest root path cost** selects the Root Port; per segment, lowest cost selects the Designated Port.

Manual override:

```cisco
interface GigabitEthernet0/1
 spanning-tree cost 10          ! per-port cost
 spanning-tree vlan 10 cost 10  ! per-VLAN cost
```

## Exam Focus

- Cost is **per-direction and per-port** — the cost a switch *receives* is added to its own port cost.
- Root's own cost = 0; its ports can all be designated (unless loop).
- Changing link speeds recomputes cost automatically — a common reason the "expected" root/port changes after an upgrade.

## Related Terms

- [[Root Bridge]], [[STP Port Roles]], [[Bridge ID]], [[STP]]
- Level 08 notes: [[Level 08 - STP/06. Root Bridge]], [[Level 08 - STP/07. Port Roles]]