---
tags: [CCNP, glossary, virtualization, cloud]
aliases: ["Container", "Containerization", "Container Runtime", "Namespaces", "Cgroups"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Container

## Definition

**Containers** package an **app + its dependencies** to run as **isolated but kernel-shared** workloads: no guest OS, no hypervisor layer — the host kernel is shared and **namespaces/cgroups** provide isolation and resource limits. They boot in **seconds**, are portable, and scale horizontally. The trade: **weaker isolation than VMs** (shared kernel) — the classic security debate.

## Container vs VM

| Aspect | VM | Container |
| --- | --- | --- |
| Kernel | Own guest OS kernel | Shared host kernel |
| Overhead | High (full OS) | Low (just the app stack) |
| Isolation | Strong | Moderate (kernel shared) |
| Boot | Minutes | Seconds |
| Units | vCPU/GB | CPU shares/memory limits |

## Exam Focus

- **"What's the key difference from VMs?" → shared kernel vs own guest OS** — the definitive contrast; boot speed and density follow.
- **Mechanisms**: namespaces (isolation) + cgroups (resource limits) — the Linux internals question.
- **Why containers for microservices?** → density, speed, CI/CD fit — the design answer.
- Networking: containers get virtual NICs/overlay nets (CNI in Kubernetes) — the network angle.

## Related Terms

- [[Virtual Machine]], [[Docker]], [[Kubernetes]], [[Hypervisor]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/03. Containers]]