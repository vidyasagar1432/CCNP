---
tags: [CCNP, glossary, high-availability, networking]
aliases: ["High Availability", "HA", "Redundancy Design", "Five Nines", "Availability"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: High Availability
created: 2026-08-29
---

# High Availability

## Definition

**High Availability** is the discipline of **layering redundancy at every level** — power, **link ([[EtherChannel]])**, **device ([[Redundant Supervisors]], stacking)**, **gateway ([[First Hop Redundancy Protocol|FHRP]])**, **path (routing)** — to reach a business **availability target** (e.g. **99.999% / five nines ≈ 5 min/year down**). Good HA design matches mechanism choice to the failure modes you can actually afford.

## The Layering

```text
device   → dual supervisors (SSO/NSF), stacking/VSS
link     → EtherChannel/LAG (multiple physical, one logical)
gateway  → HSRP/VRRP/GLBP virtual gateways
path     → routing redundancy (ECMP, backup routes, SD-WAN)
power    → redundant PSUs/UPS; plus ISSU for software
```

## Exam Focus

- **"What does HA mean in network terms?" → redundancy layered across failure domains** — the scope; "five nines ≈ how much downtime?" → ~26 s/month or 5 m/year — the math question.
- **Match failure to mechanism**: link fail → EtherChannel; supervisor fail → SSO; gateway fail → FHRP — the mapping question.
- **Design principle**: redundancy where the failure hurts; avoid single points (SPOF) — the "what's the single point?" scenario.
- HA ≠ backup only: it needs **fast detection + failed-state isolation** — the operational truth.

## Related Terms

- [[First Hop Redundancy Protocol]], [[SSO]], [[NSF]], [[EtherChannel]], [[Redundant Supervisors]], [[ISSU]], [[Virtual Switching System]]
- Level 27 notes: [[Level 27 - High Availability/08. Redundancy Design & Best Practices]]