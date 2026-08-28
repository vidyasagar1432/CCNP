---
tags: [CCNP, glossary, mpls, networking]
aliases: ["MPLS VPN", "L3VPN", "Layer 3 VPN", "BGP MPLS VPN", "Any-to-Any VPN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# MPLS VPN

## Definition

**MPLS L3VPN** is the provider service that stitches **customer sites into one private IP network across an MPLS backbone** — any-to-any, no customer overlays. The recipe: **VRFs** isolate customers on the PE, **MP-BGP** carries VPNv4 routes (RD/RT), **labels** deliver packets site-to-site through label-only cores. The customer just peers with the PE and sees its own private network.

## The Three Planes

```text
control: MP-BGP VPNv4 between PEs (RD-unique routes + RT import/export)
data:    label stack — outer (path LSP) + inner (VPN label to the far PE/VRF)
edge:    PE attaches VRF to customer-facing interfaces; CEs peer with PEs
no MPLS needed at the customer site — the CE speaks plain routing
```

## Exam Focus

- **"How does a provider give overlapping, private, any-to-any connectivity at scale?" → MPLS L3VPN** — the match; contrast Layer 2 VPN (Ethernet) vs L3VPN (IP route exchange).
- **The label stack**: outer = transport LSP, inner = VPN label at egress → the "which label picks the VRF?" answer.
- **Who routes what**: CE↔PE = customer routing; MP-BGP between PEs; P routers carry nothing customer-specific — the plane roles.
- Troubleshooting: `show ip vrf`, `show ip bgp vpnv4 vrf X`, `ping vrf X` — the recognition set.

## Related Terms

- [[MPLS]], [[VRF]], [[MP-BGP]], [[MPLS Label]], [[FEC]]
- Level 20 notes: [[Level 20 - MPLS/09. MPLS VPN]]