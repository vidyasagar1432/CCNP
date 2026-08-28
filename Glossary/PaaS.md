---
tags: [CCNP, glossary, cloud, networking]
aliases: ["PaaS", "Platform as a Service", "Serverless", "FaaS"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# PaaS

## Definition

**PaaS (Platform as a Service)** provides a **managed platform** — runtime, databases, middleware — so developers **deploy code without managing servers/OS/infra** (e.g. AWS Elastic Beanstalk, Azure App Service, Heroku; **serverless/FaaS** like Lambda is the extreme). The provider handles **infra + platform**; you own **code and data**. It sits between [[IaaS]] (raw) and [[SaaS]] (finished apps).

## The Tier Position

| Tier | What you get | You manage |
| --- | --- | --- |
| IaaS | VMs/networks | OS, runtime, app, data |
| PaaS | App platform | App code, data |
| SaaS | Complete app | Users, business data only |

## Exam Focus

- **"Which model provisions platforms not servers?" → PaaS** — the definition; "no OS patching for developers" — the benefit.
- **PaaS vs IaaS**: platform vs raw infra — the tier question; PaaS vs SaaS: platform vs finished app.
- **Serverless/FaaS**: code runs on demand, zero persistent infra — the modern mention (Lambda).
- Network angle: PaaS endpoints over HTTPS, no IP management by you — the ops difference.

## Related Terms

- [[IaaS]], [[SaaS]], [[Public Cloud]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/12. PaaS]]