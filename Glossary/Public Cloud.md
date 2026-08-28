---
tags: [CCNP, glossary, cloud, networking]
aliases: ["Public Cloud", "AWS", "Azure", "GCP", "Cloud Provider"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Public Cloud

## Definition

A **public cloud** is **shared, on-demand infrastructure** operated by a provider (**AWS, Azure, GCP**) and consumed as **[[IaaS]]/[[PaaS]]/[[SaaS]]**. You rent capacity with **elasticity**, global scale, and pay-per-use — no capex, no facility. The trade: **shared responsibility** (provider secures the cloud; you secure what you run in it) and the network must reach it (Internet/VPN/Direct Connect).

## The Public Cloud Deal

```text
provider: global regions + AZs, virtual networks (VPC), managed services
you: rent VMs (IaaS), platforms (PaaS), or apps (SaaS) at meter pricing
network: connect via Internet VPN (IPsec) or private links (DX/ExpressRoute)
shared responsibility: provider = physical/hypervisor; you = OS/apps/network policy
```

## Exam Focus

- **"What is public cloud?" → shared multi-tenant provider infrastructure** — vs [[Private Cloud]] (dedicated) — the contrast.
- **Shared responsibility model**: who secures what — the classic exam table.
- **Connecting to it**: site-to-site VPN, Direct Connect/ExpressRoute (private) — the WAN question.
- **Elasticity + OpEx** vs private cloud capex — the economics phrase.

## Related Terms

- [[Private Cloud]], [[Hybrid Cloud]], [[IaaS]], [[PaaS]], [[SaaS]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/08. Public Cloud]]