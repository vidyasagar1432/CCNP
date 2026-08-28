---
tags: [CCNP, glossary, security, switching]
aliases: ["Storm Control", "Broadcast Storm", "Multicast Storm", "Unicast Storm"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# Storm Control

## Definition

**Storm control** caps the rate of **broadcast, multicast, or unknown-unicast** traffic per port (as a % of bandwidth or pps) and **drops the excess** — protecting the network from **packet storms**: loops, misbehaving devices, or attack floods that would otherwise eat all switch CPU/bandwidth (a broadcast storm is the classic STP-loss symptom).

## The Behavior

```text
interface gi0/1
  storm-control broadcast level 10        ← cap broadcast at 10% of BW
  storm-control multicast level 20
  storm-control unicast level pps 500
  storm-control action shutdown | trap    ← drop vs. errdisable+notify
```

| Storm type | Typical cause |
| --- | --- |
| Broadcast | STP failure/loop, rogue device flooding |
| Unknown-unicast | CAM flood attack |
| Multicast | Buggy stream/group churn |

## Exam Focus

- **"Which feature limits broadcast/multicast floods per port?" → storm control** — with the level/action keywords as config recognition.
- **STP-link**: broadcast storms are what break networks when STP fails — "after a loop, what saved the rest of the switch?" → storm control (and how it differs from BPDU guard).
- Levels are **% of link bandwidth** (or pps) — the "how is the threshold expressed?" trivia.
- Versus [[Port Security]]: storm control is traffic-rate protection; port security is identity protection — keep the two families straight.

## Related Terms

- [[Broadcast Domain]], [[STP]], [[Port Security]], [[CoPP]]
- Level 17 notes: [[Level 17 - Security/08. Storm Control]]