---
tags: [CCNP, glossary, sdn, automation]
aliases: ["LISP", "Locator ID Separation Protocol", "EID", "RLOC", "Map Server", "Map Resolver"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# LISP

## Definition

**LISP (Locator/ID Separation Protocol)** splits a host's **identity (EID)** from its **location (RLOC)**: endpoints keep stable IDs while the network tracks where they live, via a **map server/map resolver** control plane. Mobility becomes a mapping update — the **control plane of [[SD-Access]]** (alongside [[VXLAN]] data plane). Packets are encapsulated to the RLOC that currently holds the EID.

## The Separation

```text
EID  = endpoint identifier (host/device address — stays stable)
RLOC = routing locator (topology address where the device currently is)
flow: packet to EID → query map (map-resolver/map-server) → get RLOC →
      encapsulate & deliver → LISP header between inner and outer IP
```

## Exam Focus

- **"What does LISP separate?" → EID (identity) from RLOC (location)** — the definition; the acronym mapping.
- **LISP's role in SD-Access**: control plane (VXLAN = data plane) — the roles pairing.
- **Map server / map resolver**: who stores vs who answers mappings — the control-plane components.
- Mobility without IP changes: host moves, mapping updates — the "how does roaming keep the IP?" answer.

## Related Terms

- [[SD-Access]], [[VXLAN]], [[DNA Center]], [[SDN]]
- Level 24 notes: [[Level 24 - SDN & Automation/05. LISP]]