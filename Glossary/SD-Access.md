---
tags: [CCNP, glossary, sdn, automation]
aliases: ["SD-Access", "Software-Defined Access", "SDA Fabric", "Fabric Mode"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# SD-Access

## Definition

**SD-Access** is Cisco's **intent-based campus fabric**: a **[[VXLAN]] overlay** carries data (16M VNIs — the VLAN problem solved), **[[LISP]]** is the control plane (EID→RLOC mapping), **ISE** provides policy/segmentation, and **[[DNA Center]]** orchestrates it all. Devices connect anywhere and get their identity/policy from the fabric — the campus equivalent of SD-WAN's overlay thinking.

## The Fabric Roles

```text
underlay: IP network (routing) — fabric doesn't care about the physical design
overlay: VXLAN (data) + LISP (control) — one logical campus fabric
edge nodes: access switches (identity/policy enforcement)
border nodes: connect fabric to legacy/DC/WAN (gateway)
control: LISP map server/resolver; policy via ISE groups (SGTs)
```

## Exam Focus

- **"What is SD-Access?" → campus fabric: VXLAN data + LISP control + DNA orchestration** — the three-tech recipe (the recurring exam combo).
- **VXLAN vs LISP roles in the fabric**: encapsulation vs identity/location mapping — the split question (see [[VXLAN]], [[LISP]]).
- **Fabric roles**: edge, border, control — "which node connects to the WAN?" → border — the role map.
- SD-Access vs traditional campus: VLAN-based vs VNI/group-based — the migration story.

## Related Terms

- [[VXLAN]], [[LISP]], [[DNA Center]], [[SDN]], [[VLAN]]
- Level 24 notes: [[Level 24 - SDN & Automation/03. SD-Access]]