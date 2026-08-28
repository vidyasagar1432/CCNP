---
tags: [CCNP, glossary, switching, first-hop]
aliases: ["Object Tracking", "Track Object", "IP SLA Tracking", "track list"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: First Hop Redundancy
created: 2026-08-29
---

# Object Tracking

## Definition

**Object tracking** monitors a condition (interface up/down, IP reachability via [[IP SLA]], route in table) and lets **other features react** to it — the classic pairing being **[[First Hop Redundancy Protocol|FHRP]] priority**: track the uplink; when it fails, decrement priority so the **standby router takes over**. It fixes the "active router lost its uplink but is still the gateway" failure mode.

## The Pattern

```text
track 10 interface gigabitethernet0/1 line-protocol
track 20 ip sla 1 reachability            ← probes an upstream target
track 30 ip route 10.2.0.0/16 reachability

standby 10 track 10 decrement 20          ← HSRP: priority −20 when track 10 goes down
  (GLBP: weight-based — track lowers the forwarder weight instead)
```

| Tracked object | Answers "is…" |
| --- | --- |
| Interface line-protocol | This link physically up? |
| IP SLA reachability | The far end still reachable? |
| IP route reachability | This prefix still in the RIB? |

## Exam Focus

- **"How does HSRP know the WAN uplink failed?" → object tracking** (paired with IP SLA for non-adjacent targets) — the conceptual definition.
- **Priority decrement vs weight decrement**: HSRP/VRRP lower priority; GLBP lowers weight — protocol-specific reaction.
- Tracked-object states: UP/DOWN (+ "any/not") — `show track` is the diagnostic; thresholds (weight threshold) for GLBP.

## Related Terms

- [[First Hop Redundancy Protocol]], [[HSRP]], [[VRRP]], [[GLBP]], [[IP SLA]]
- Level 14 notes: [[Level 14 - First Hop Redundancy/04. Object Tracking]]