---
tags: [CCNP, glossary, stp, switching]
aliases: ["BPDU Guard", "BPDUGuard"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# BPDU Guard

## Definition

**BPDU Guard** protects **edge/[[PortFast]] ports**: if the port receives any [[BPDU]], BPDU Guard **shuts the port down** (errdisable). A BPDU means a switch-like device appeared on what should be an end-host port — either miswiring or an attacker.

## How It Works

```cisco
! Per interface
interface GigabitEthernet0/1
 spanning-tree bpduguard enable

! Globally (only affects ports with portfast)
spanning-tree portfast bpduguard default
```

Upon receiving a BPDU:

```text
Port receives BPDU
      ↓
Port placed in errdisable
      ↓
Recovery: manual (shut/no shut) or auto (errdisable recovery)
```

## Why It Matters

- Prevents a rogue switch from hijacking the [[Root Bridge]] election or creating loops.
- In RSTP edge ports, receiving a BPDU would convert the port to a normal STP port — BPDU Guard prevents that surprise.

## Exam Focus

- **BPDU Guard ≠ BPDU Filter.** Guard *shuts down* on BPDU receipt; Filter *drops* BPDUs and never participates (see [[BPDU Filter]]).
- It is the classic pairing with PortFast: PortFast for speed, BPDU Guard for safety on the same edge port.
- Verify with `show errdisable detect` / `show interfaces status err-disabled`.

## Related Terms

- [[PortFast]], [[BPDU]], [[BPDU Filter]], [[Root Guard]], [[STP]]
- Level 08 notes: [[Level 08 - STP/11. BPDU Guard]]