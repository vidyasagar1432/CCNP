---
tags: [CCNP, glossary, cloud, networking]
aliases: ["Hybrid Cloud", "Hybrid Cloud Model"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Hybrid Cloud

## Definition

A **hybrid cloud** combines **[[Private Cloud|on-premises]] and [[Public Cloud|public cloud]]** into one operating model: **shared networking, security, and management** between both, so workloads can **burst** (overflow to public), **backup**, or **replicate** across the boundary. The network is the glue: **VPN/IPsec, Direct Connect/ExpressRoute, SD-WAN** stitching campus → DC → cloud.

## The Boundary

```text
on-prem (private) ⇄ (IPsec VPN / private link / SD-WAN) ⇄ public cloud (VPC)
uses: cloud burst, DR/business continuity, dev in cloud + prod on-prem
common pitfalls: IP overlap, security parity, latency, data gravity
```

## Exam Focus

- **"What is hybrid cloud?" → private + public used together** — the definition; the connectivity question follows ("how do they connect?" → VPN/private link).
- **Why hybrid?** → burst capacity, DR, compliance split — the use-case answer.
- **IP overlap** between on-prem and cloud VPCs is the top networking failure — the design gotcha.
- SD-WAN to cloud (Direct Internet Access / cloud gateways) — the modern tie-in ([[SD-WAN]]).

## Related Terms

- [[Public Cloud]], [[Private Cloud]], [[SD-WAN]], [[IPsec]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/10. Hybrid Cloud]]