---
tags: [CCNP, glossary, cloud, networking]
aliases: ["IaaS", "Infrastructure as a Service", "Cloud Compute", "EC2"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# IaaS

## Definition

**IaaS (Infrastructure as a Service)** delivers **raw compute, storage, and networking** on demand: you rent **VMs (vCPU/vRAM), disks, and virtual networks (VPC)** and manage everything above — **OS, apps, data** (AWS EC2, Azure VM, GCP Compute). The provider handles the physical/hypervisor layer. More control than [[PaaS]]/[[SaaS]], more work — the "bare metal of the cloud".

## The IaaS Stack

```text
you: guest OS, patches, apps, data, security inside the VMs
provider: hypervisor hosts, storage, virtual networking (VPC/subnets)
virtual network: VPC, subnets, security groups, NAT, VPN/Direct Connect to on-prem
```

## Exam Focus

- **"Which model rents raw VMs/networks?" → IaaS** — the definition; "the customer patches the OS" — the responsibility line.
- **IaaS examples**: EC2, Azure VMs — the recognition.
- **IaaS vs PaaS vs SaaS**: infra vs platform vs app — the tier ladder (most to least control).
- Networking: VPCs, security groups, IPsec to on-prem, cloud routing — "how does the enterprise network reach IaaS?" answer.

## Related Terms

- [[PaaS]], [[SaaS]], [[Virtual Machine]], [[Public Cloud]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/13. IaaS]]