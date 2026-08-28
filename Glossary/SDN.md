---
tags: [CCNP, glossary, sdn, automation]
aliases: ["SDN", "Software-Defined Networking", "Controller", "Northbound API", "Southbound Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# SDN

## Definition

**SDN (Software-Defined Networking)** **separates the control plane from the data plane**: the brain moves to a **central controller** (e.g. [[DNA Center]]), while switches/routers keep only the forwarding plane. The controller talks to apps via **northbound APIs** (REST) and to devices via **southbound protocols** — **NETCONF/RESTCONF**, OpenFlow, SNMP. Result: network behavior becomes software — programmable, automated, policy-driven.

## The Three Planes

```text
APPLICATION layer — apps ask the network (Northbound API: REST/JSON)
CONTROL layer    — the controller: topology, policy, intent (the brain)
INFRASTRUCTURE   — devices forward (Southbound: NETCONF, OpenFlow, etc.)
```

## Exam Focus

- **"What does SDN separate?" → control plane from data plane** — the definition; centralization in a controller.
- **Northbound vs Southbound**: toward apps (REST) vs toward devices (NETCONF/RESTCONF) — the direction question.
- **SDN vs traditional**: box-local decision vs controller-derived policy — the paradigm contrast.
- Cisco's flavors: DNA Center (campus), SD-WAN vSmart (WAN) — "which product embodies SDN for campus?" answer.

## Related Terms

- [[DNA Center]], [[SD-Access]], [[REST API]], [[NETCONF]], [[RESTCONF]], [[Cisco IOS]]
- Level 24 notes: [[Level 24 - SDN & Automation/01. SDN]]