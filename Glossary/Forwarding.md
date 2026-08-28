---
tags: [CCNP, glossary, switching, networking]
aliases: ["L2 Forwarding", "Frame Forwarding"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Forwarding

## Definition

**Forwarding** at Layer 2 is choosing **which egress port** a received frame goes out — based on the **destination MAC + VLAN** lookup in the **[[CAM Table]]**. It completes the trio with [[MAC Learning]] (inbound) and [[Filtering]] (deliberate non-delivery).

## The Decision

```text
frame in (ingress port, VLAN)
   │ destination MAC in CAM?
   ├─ yes → forward ONLY to the matched port (same VLAN)
   ├─ no  → flood (unknown unicast)
   └─ broadcast/multicast → flood (or snooping-aware)
```

- Forwarding is **VLAN-constrained**: a frame never egresses a port that is not in the frame's VLAN (see [[VLAN]]).
- Switch forwarding ≠ router forwarding: switch = MAC/port lookup; router = longest-prefix IP lookup ([[CEF]]).

## Exam Focus

- **"Forwarding decisions are based on..."** → destination MAC (+ VLAN), never on source MAC.
- The pair "learn by source / forward by destination" is a guaranteed single-question.
- Forwarding only *within* the same VLAN — inter-VLAN requires a router ([[VLAN]] routing).

## Related Terms

- [[CAM Table]], [[MAC Learning]], [[Flooding]], [[Filtering]], [[VLAN]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/06. Forwarding]]