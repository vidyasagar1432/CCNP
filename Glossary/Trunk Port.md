---
tags: [CCNP, glossary, switching, vlan]
aliases: ["Trunk Port", "Trunking", "Trunk"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# Trunk Port

## Definition

A **trunk port** carries **multiple VLANs** between switches (or to a router) by **802.1Q-tagging** each frame with its VLAN ID. It is how ONE link carries ALL your VLANs — the backbone of multi-switch VLAN design.

## How It Works

```text
switch A ── trunk (tagged) ── switch B
frame leaves A: [VLAN 10 tag] ── 802.1Q header inserted
switches use the tag to forward; the tag is removed at the final access port
(unless the frame was in the native VLAN — left untagged, see [[Native VLAN]])
```

| Command | Effect |
| --- | --- |
| `switchport mode trunk` | Hard-set trunking |
| `switchport trunk allowed vlan 10,20` | Only these VLANs cross (pruning = security) |
| `switchport trunk native vlan 99` | Untagged VLAN on the trunk |

## Exam Focus

- **Tag format details**: 802.1Q adds a 4-byte tag — **TPID 0x8100**, 12-bit **VLAN ID (0–4095)**; priority (PCP) bits feed [[QoS]].
- **Native VLAN mismatch** = the classic troubleshooting trap: traffic silently mis-frames between mismatched native VLANs — "frames appear in the wrong VLAN" symptom.
- Trunks need: allowed-list discipline (VLAN hopping protection) + never carry VLAN 1 if avoidable (native/default attacks).

## Related Terms

- [[VLAN]], [[Access Port]], [[802.1Q]], [[Native VLAN]], [[DTP]], [[QinQ]]
- Level 07 notes: [[Level 07 - VLAN Technologies/05. Trunk Port]]