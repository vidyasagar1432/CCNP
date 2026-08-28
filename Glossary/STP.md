---
tags: [CCNP, glossary, stp, switching]
aliases: ["Spanning Tree Protocol", "IEEE 802.1D"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# STP

## Definition

**STP (Spanning Tree Protocol, IEEE 802.1D)** prevents **Layer-2 loops** in redundant switched networks by building a **loop-free logical topology** — it keeps physical redundancy but places selected redundant paths into a **non-forwarding state**.

## How It Works

1. Switches exchange **[[BPDU]]s** to elect a single [[Root Bridge]] from the entire switched topology.
2. Every non-root switch selects one [[STP Port Roles|Root Port]] (best path to root).
3. Every segment selects one [[STP Port Roles|Designated Port]].
4. Non-selected ports block — they listen for BPDUs but do not forward user frames.

```text
        (Root)
         SW1
      /        \
   SW2          SW3
   root port    designated
   /   \
SW4   SW5
blocked path stays non-forwarding
```

## Stability and Convergence

- Changes are reacted to slowly by design: [[STP Port States]] move through listening → learning → forwarding, timed by [[STP Timers]].
- Without STP, redundant loops cause **broadcast storms**, **MAC-table instability**, and **duplicate frames** — the classic L2 disaster scenarios.

## Cisco Variants

| Variant | Standard | One instance per VLAN? |
| --- | --- | --- |
| STP | 802.1D | No (or with [[PVST+]]) |
| [[RSTP]] | 802.1w | No (faster) |
| [[PVST+]] / Rapid PVST+ | Cisco per-VLAN | Yes |
| [[MST]] | 802.1s | Multiple VLANs → few instances |

## Exam Focus

- STP's job is **loop prevention**, not load balancing (that is a side effect of design and of protocols like MST).
- The **root bridge is not eliminated** by RSTP or MST — every STP variant still elects one.
- Know the decision order: **lowest Bridge ID → lowest root path cost → lowest sender bridge ID → lowest sender port ID**. (See [[Root Bridge]], [[STP Path Cost]], [[Bridge ID]].)

## Related Terms

- [[BPDU]], [[Root Bridge]], [[Bridge ID]], [[STP Port Roles]], [[STP Port States]], [[STP Timers]], [[RSTP]], [[MST]], [[PortFast]]
- Level 08 notes: [[Level 08 - STP/STP Overview]]