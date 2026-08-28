---
tags: [CCNP, glossary, switching, first-hop]
aliases: ["HSRP", "Hot Standby Router Protocol", "HSRP Group"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: First Hop Redundancy
created: 2026-08-29
---

# HSRP

## Definition

**HSRP (Hot Standby Router Protocol)** is Cisco's proprietary [[First Hop Redundancy Protocol|FHRP]]: two or more routers share a **virtual IP + virtual MAC**; one is **Active**, the others **Standby**. If Active dies, Standby takes over in seconds (hello 3 s, hold 10 s; subsecond with timers). Virtual MAC: `0000.0c07.acXX` (XX = group).

## The Essentials

```text
standby 10 ip 10.1.1.254          ← VIP (hosts' gateway)
standby 10 priority 120            ← higher wins Active
standby 10 preempt                  ← retake when priority returns
standby 10 track gigabitethernet0/1 ← uplink loss → priority −10 (see [[Object Tracking]])
standby 10 authentication md5 key-string XYZ
UDP 1985, multicast 224.0.0.2, group 0–255, VMAC 0000.0c07.acXX
```

## The States (recite)

INITIAL → **LEARN** (no VIP yet) → **LISTEN** (sees hellos) → SPEAK (announces) → STANDBY → **ACTIVE**. Elections: highest **priority**, tie-break by **highest IP**.

## Exam Focus

- **"Which FHRP is Cisco proprietary with virtual MAC 0000.0c07.acXX?" → HSRP** — the fingerprint questions.
- HSRP **v1 vs v2**: v2 supports groups > 255, IPv6, and uses `0000.0c9f.f000` MACs — ask-the-version trivia.
- **Preempt** is the word: without preempt, the original Active never returns after a failback.
- Timer scoring: 3 s/10 s default, 1 s/3 s or 200 ms/700 ms with timers — "fast convergence" answer is subsecond.

## Related Terms

- [[First Hop Redundancy Protocol]], [[VRRP]], [[GLBP]], [[Object Tracking]], [[Gratuitous ARP]]
- Level 14 notes: [[Level 14 - First Hop Redundancy/01. HSRP]]