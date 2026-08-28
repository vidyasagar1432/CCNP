---
tags: [CCNP, glossary, switching, vlan]
aliases: ["Native VLAN", "Untagged VLAN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# Native VLAN

## Definition

The **native VLAN** is the VLAN on a **[[Trunk Port]] that is sent UNTAGGED** — frames belonging to it cross the trunk without a 802.1Q tag. It exists for compatibility with gear that doesn't understand tags. **Default: VLAN 1** — and that default is a security liability.

## The Rules

```text
trunk native vlan 99  ← everything for VLAN 99 goes out plain (no tag)
inbound untagged frames on a trunk → assigned to the native VLAN
native VLAN MUST match on both ends
   mismatch → frames silently go into the other switch's native VLAN
             (the "wrong VLAN" symptom, MAC-table weirdness, CDP/VTP talking over)
```

## Exam Focus

- **"Which VLAN is untagged on a trunk?" → native VLAN** — the one fact that makes or breaks trunk questions.
- **Native VLAN mismatch** is one of the most repeated symptoms in switch troubleshooting scenarios — verify with `show interfaces trunk`.
- Security: hosts in the native VLAN can **double-tag** (VLAN hopping) by putting an 802.1Q header in the payload — mitigation: change native VLAN off 1, disable DTP, prune the list.

## Related Terms

- [[Trunk Port]], [[VLAN]], [[802.1Q]], [[Access Port]], [[DTP]]
- Level 07 notes: [[Level 07 - VLAN Technologies/06. Native VLAN]]