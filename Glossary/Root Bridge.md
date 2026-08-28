---
tags: [CCNP, glossary, stp, switching]
aliases: ["Root Switch", "Root Bridge Election"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# Root Bridge

## Definition

The **root bridge** is the single switch chosen as the reference point of the spanning tree — the "top" of the logical loop-free topology. All other switches compute their [[STP Path Cost|root path cost]] toward it, and every tree terminates at it.

## Election

Root election uses the [[Bridge ID]]:

```text
1. Lowest bridge priority
2. Lowest extended system ID (VLAN) if priorities equal
3. Lowest MAC address if still tied
```

Every switch announces its candidate root in its [[BPDU]]s; eventually all agree on one root per VLAN.

## Root Bridge Characteristics

- **All its ports can be [[STP Port Roles|Designated Ports]]** unless it has a physical loop back to itself (then one becomes backup/blocked).
- The root is the **only switch without a Root Port**.
- Elected by configuration, not by location — that is why placement is a design decision, and why [[Root Guard]] exists.

## Common Design Practice

- Choose the switch closest to the network core, ideally with the most aggregated traffic.
- `spanning-tree vlan X root primary` / `root secondary` sets priority without manual math.

## Exam Focus

- **Root bridge placement matters for path utilization** — poorly placed roots create long, inefficient paths and block useful links.
- **RSTP does not remove the root bridge** — it accelerates convergence around the same root.
- A switch *can* be root for one VLAN and non-root for another in per-VLAN STP ([[PVST+]]).

## Related Terms

- [[Bridge ID]], [[BPDU]], [[STP Port Roles]], [[STP Path Cost]], [[Root Guard]], [[STP]]
- Level 08 notes: [[Level 08 - STP/06. Root Bridge]]