---
tags: [CCNP, glossary, sdn, automation]
aliases: ["DNA Center", "Cisco DNA Center", "Intent-Based Networking", "IBN", "DNA-C"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# DNA Center

## Definition

**Cisco DNA Center** is the **SDN controller + management platform for the campus**: the heart of **intent-based networking (IBN)**. It automates **design, provisioning, assurance (telemetry/AI), and policy** across switches/APs, and orchestrates **[[SD-Access]]** fabrics (VXLAN/LISP/ISE). It is the campus analog of SD-WAN's vManage — one pane of glass, with REST APIs for everything.

## What It Does

```text
design: sites, network profiles, templates
provision: plug-and-play onboarding, Day-0/1 config at scale
policy: segmentation, group-based access (with ISE)
assurance: streaming telemetry, AI-driven health scores (wired+wireless)
APIs: REST northbound — "show me all devices / push this template"
```

## Exam Focus

- **"What is DNA Center?" → campus SDN controller + assurance platform; IBN** — the role/pairing (with SD-Access).
- **The four "intents"**: design / provision / policy / assurance — the pillar question.
- DNA Center vs **Prime**: legacy NMS vs intent-based automation — the generation contrast.
- **DNA vs SD-WAN planes**: campus DNA ↔ WAN vManage/vSmart — the ecosystem mapping.

## Related Terms

- [[SDN]], [[SD-Access]], [[VXLAN]], [[REST API]], [[Telemetry]]
- Level 24 notes: [[Level 24 - SDN & Automation/02. Cisco DNA Center]]