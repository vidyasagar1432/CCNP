---
tags: [CCNP, glossary, wan, networking]
aliases: ["vManage", "SD-WAN Management Plane", "vManage NMS"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# vManage

## Definition

**vManage** is the **management plane** of Cisco [[SD-WAN]]: the central **NMS dashboard + API** where you **onboard devices, push templates (device/feature/VPN), monitor health, and run analytics** across the whole fabric. It talks to every controller and edge, aggregates their state (alerts, tunnels, apps) — and is the operator's single pane of glass.

## The Management View

```text
vManage tasks: device onboarding (ZK/connect), template deployment,
  software upgrades (image mgmt), monitoring dashboards,
  REST API / integration with DNA-C, NetFlow-ish app visibility
redundancy: vManage cluster (up to N nodes) — the fabric's book of record
```

## Exam Focus

- **"Which SD-WAN component is the UI/management plane?" → vManage** — the role definition; some questions map it vs [[vSmart]]/[[vBond]].
- **Templates**: feature templates + device templates (composite) — the config-model question.
- vManage is where **policies get authored** (centralized policy) before vSmart distributes them — the policy-authoring link to [[vSmart]].
- vManage cluster = HA for the dashboard + API — the redundancy mention.

## Related Terms

- [[SD-WAN]], [[vSmart]], [[vBond]], [[WAN Edge]]
- Level 23 notes: [[Level 23 - Enterprise WAN/08. vManage]]