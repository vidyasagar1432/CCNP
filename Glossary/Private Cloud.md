---
tags: [CCNP, glossary, cloud, networking]
aliases: ["Private Cloud", "On-Premises Cloud", "VMware Cloud", "OpenStack"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Private Cloud

## Definition

A **private cloud** delivers **cloud-like capabilities** — **self-service, elasticity, metering** — on **dedicated, on-premises** infrastructure (typically **VMware, OpenStack, or Nutanix**). You keep **full control and isolation**, but you also own the **capex and operational burden**. It's the "cloud without the provider" — built to satisfy compliance, latency, or sovereignty needs.

## The Private Cloud Deal

```text
self-service portal + API (vCenter/OpenStack Horizon)
shared pools: compute/storage from your own clusters; tenants via VMs-containers
metering/showback; automation (VM templates, IaC)
why: regulatory data, predictable workloads, sunk DC investment
```

## Exam Focus

- **"What is private cloud?" → dedicated cloud-like infrastructure you operate** — vs public (someone else's) — the ownership question.
- **Why choose it?** → compliance/data sovereignty/latency; why not? → capex/scale limits — the trade-off answer.
- Tech: vSphere, OpenStack, KVM+automation — the stack recognition.
- Private vs on-prem legacy: self-service + elasticity are what make it "cloud" — the definitional nuance.

## Related Terms

- [[Public Cloud]], [[Hybrid Cloud]], [[Hypervisor]], [[IaaS]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/09. Private Cloud]]