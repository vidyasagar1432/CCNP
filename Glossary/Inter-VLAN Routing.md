---
tags: [CCNP, glossary, switching, routing]
aliases: ["Inter-VLAN Routing", "IVR", "Router on a Stick"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# Inter-VLAN Routing

## Definition

**Inter-VLAN routing** is the Layer-3 forwarding **between VLANs** (different subnets→different broadcast domains). A router (or L3 switch) is the mandatory in-between: VLANs never talk at L2 unless something routes them. Three classic implementations: **SVIs, router-on-a-stick, routed ports**.

## The Three Ways

| Method | Where routing lives | Good for |
| --- | --- | --- |
| **SVI** (Switch Virtual Interface) | L3 switch, one virtual interface per VLAN (`interface vlan 10`) | Campus/distribution, low latency, simple |
| [[Router-on-a-Stick]] | External router + trunk subinterfaces | Small/edge, upgrades without new hardware |
| Routed ports | Each access port = routed interface (`no switchport`) | Server/DC segments, L3 access |

```text
switch:  interface vlan 10 → ip address 10.1.10.1/24   (gateway for VLAN 10)
         interface vlan 20 → ip address 10.1.20.1/24   (gateway for VLAN 20)
         ip routing  ← the switch must route! (routing = not a switch VLAN default)
```

## Exam Focus

- **"Inter-VLAN traffic flows through what?" → a Layer-3 device** — the SVI/subinterface is a gateway, and `ip routing` is what turns a switch into the router.
- SVI vs subinterface: SVI scales (hardware), subinterface is limited by trunk bandwidth.
- **DHCP relay + inter-VLAN routing pair up**: hosts in VLAN 20 need `ip helper-address` to reach the DHCP server in VLAN 10 — a combined scenario question.

## Related Terms

- [[VLAN]], [[Router-on-a-Stick]], [[Subnet]], [[DHCP]]
- Level 07 notes: [[Level 07 - VLAN Technologies/10. Inter-VLAN Routing]]