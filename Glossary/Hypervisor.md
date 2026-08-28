---
tags: [CCNP, glossary, virtualization, cloud]
aliases: ["Hypervisor", "VMM", "Virtual Machine Monitor", "Type 1", "Type 2", "ESXi", "KVM"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Hypervisor

## Definition

A **hypervisor (VMM)** is the software that **creates and runs [[Virtual Machine|VMs]]** by abstracting hardware and multiplexing it between guests. **Type 1 (bare-metal)** runs directly on hardware — the datacenter standard (**ESXi, KVM, Hyper-V, Xen**). **Type 2 (hosted)** runs as an app on an OS (VirtualBox, VMware Workstation) — labs and desktops.

## Type 1 vs Type 2

| Type | Runs on | Examples | Use |
| --- | --- | --- | --- |
| Type 1 | Bare hardware | ESXi, KVM, Hyper-V | Production DC/cloud |
| Type 2 | Host OS | VirtualBox, Workstation, Parallels | Dev/lab/desktop |

## Exam Focus

- **"What runs VMs?" → hypervisor** — the definition; Type 1 = bare-metal (production), Type 2 = hosted — the type question.
- **Examples per type**: ESXi/KVM = Type 1; VirtualBox = Type 2 — the recognition.
- **Why Type 1 in the cloud?** → fewer layers, better performance/isolation — the choice rationale.
- Virtual networking: hypervisor ships virtual switches (vSwitch) for VM↔VM traffic — the "where do VMs connect?" answer.

## Related Terms

- [[Virtual Machine]], [[Container]], [[IaaS]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/02. Hypervisors]]