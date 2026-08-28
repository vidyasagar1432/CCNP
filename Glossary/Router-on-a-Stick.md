---
tags: [CCNP, glossary, switching, routing]
aliases: ["Router-on-a-Stick", "ROAS", "Router on a Stick", "Subinterfaces"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# Router-on-a-Stick

## Definition

**Router-on-a-Stick (ROAS)** does [[Inter-VLAN Routing]] with ONE physical router link: the link is a **trunk to a switch**, and each **802.1Q subinterface** on the router owns one VLAN's gateway. `encapsulation dot1q <vlan>` ties each subinterface to a tag.

## The Config Pattern

```text
interface g0/0.10
  encapsulation dot1q 10        ← VLAN 10 = tag 10
  ip address 10.1.10.1 255.255.255.0
interface g0/0.20
  encapsulation dot1q 20
  ip address 10.1.20.1 255.255.255.0
  (native VLAN variant: encapsulation dot1q 20 native — untagged)

switch side:  port is a trunk carrying VLANs 10,20
```

## The Bottleneck Reality

- **ALL inter-VLAN traffic crosses ONE link** → single point of contention; subinterfaces share the trunk's bandwidth.
- Fixes: L3 etherchannel (adds links), or move routing to the switch (SVIs) — ROAS is a stepping-stone design, not a scale design.

## Exam Focus

- **"Router with subinterfaces routing VLANs over one trunk" → router-on-a-stick** — the exact definition.
- `encapsulation dot1q <vlan-id>` is the command that makes a subinterface a VLAN gateway; **mismatched native = silence** symptom (native rule applies on the router too).
- CDP/DTP trivia: subinterface native defaults to VLAN 1 unless `.10 native` — expect the "which subinterface tags native" question.

## Related Terms

- [[Inter-VLAN Routing]], [[Trunk Port]], [[802.1Q]], [[Native VLAN]], [[VLAN]]
- Level 07 notes: [[Level 07 - VLAN Technologies/11. Router-on-a-Stick]]