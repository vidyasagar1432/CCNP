---
tags: [CCNP, glossary, virtualization, cloud]
aliases: ["Virtual Machine", "VM", "Guest OS", "Computing Virtualization"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Virtual Machine

## Definition

A **VM** is a **software-emulated computer**: a full **guest OS** running on **virtualized hardware** (vCPU, vRAM, vNIC, vDisk) provided by a **hypervisor**. VMs deliver **strong isolation** and hardware flexibility at the cost of overhead (a whole OS per workload). In networking: VMs are what cloud IaaS rents you (EC2, Azure VMs) and what network virtual appliances (vEdge, virtual IOS-XE) run on.

## Structure

```text
host hardware → hypervisor (Type 1/2) → VMs (each: full guest OS + virtual devices)
VM = guest OS + virtual CPU/RAM/NIC/disk; moves between hosts (vMotion/live migration)
vs container: VM = heavy kernel per workload; container = shared host kernel
```

## Exam Focus

- **"What is a VM?" → full virtualized computer with guest OS** — the definition; key properties: isolation, portability, snapshot.
- **VM vs container**: each VM carries its own kernel/OS (heavy); containers share the host kernel (light) — the contrast question.
- **Cloud tie-in**: IaaS = "rent VMs"; the "what are you actually renting?" answer.
- Networking angle: virtual NICs, virtual switches (vSwitch/DVS), VM mobility — the "what changes in the network when VMs move?" scenario.

## Related Terms

- [[Hypervisor]], [[Container]], [[IaaS]], [[Public Cloud]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/01. Virtual Machines]]