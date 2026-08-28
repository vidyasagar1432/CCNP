---
tags: [CCNP, glossary, sdn, automation]
aliases: ["VXLAN", "Virtual Extensible LAN", "VNI", "VTEP", "UDP 4789"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# VXLAN

## Definition

**VXLAN** is an **overlay data-plane** technology: it wraps L2 frames in a **UDP (4789)** packet (outer: IP/UDP/VXLAN header) that rides any L3 underlay. Its **VNI (VXLAN Network Identifier, 24-bit)** replaces the 12-bit VLAN → **16 million segments** instead of 4094, and L2 domains stretch across routed cores / DCs — the foundation of **[[SD-Access]]** and data-center fabrics.

## The Encapsulation

```text
[host MAC frame] → VXLAN header (VNI 24-bit) → UDP 4789 → IP → L2/L3 underlay
VTEP (tunnel endpoint) = the device that encapsulates/decapsulates
control: BGP-EVPN or multicast — how VTEPs learn each other's hosts
```

## Exam Focus

- **"Which protocol encapsulates L2 in UDP?" → VXLAN** — with port **4789** and VNI — the fact triple.
- **"Why VXLAN?" → VLAN limit (4094) + L2 over L3** — the 16M VNI answer (24-bit).
- **VTEP**: the encapsulation endpoint — "what device does the VXLAN wrapping?" answer.
- VXLAN = data plane of SD-Access; [[LISP]] = its control plane — the pairing question.

## Related Terms

- [[SD-Access]], [[LISP]], [[VLAN]], [[UDP]], [[Telemetry]]
- Level 24 notes: [[Level 24 - SDN & Automation/04. VXLAN]]