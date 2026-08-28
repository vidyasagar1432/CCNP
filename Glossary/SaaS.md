---
tags: [CCNP, glossary, cloud, networking]
aliases: ["SaaS", "Software as a Service", "Cloud Application"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# SaaS

## Definition

**SaaS (Software as a Service)** delivers **complete applications over the internet** — **no install, no server management**: the provider runs everything (apps, OS, infra, updates). Examples: **Office 365, Salesforce, Webex, Google Workspace**. The customer is just a user; the shared-responsibility line sits at the app level. For the network: SaaS traffic flows to provider edges — QoS/video (Webex) and direct-to-cloud routing matter.

## The Service Tiers

| Tier | You manage | Provider manages |
| --- | --- | --- |
| On-prem | Everything | Nothing |
| IaaS | OS + app + data | Hypervisor + infra |
| PaaS | Code + data | Runtime + platform |
| SaaS | Just users/data | Everything else |

## Exam Focus

- **"Which model gives you a finished app?" → SaaS** — the definition; the least control, least work.
- **SaaS examples**: O365, Salesforce, Webex — the recognition (Webex = the Cisco link).
- **Shared responsibility**: at SaaS you manage only users and data — the boundary question.
- Network angle: optimizing **SaaS delivery** (SD-WAN direct internet, cloud on-ramps) — the "why bypass the DC for SaaS?" answer.

## Related Terms

- [[PaaS]], [[IaaS]], [[Public Cloud]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/11. SaaS]]