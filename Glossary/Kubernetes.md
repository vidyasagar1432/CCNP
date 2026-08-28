---
tags: [CCNP, glossary, virtualization, cloud]
aliases: ["Kubernetes", "K8s", "Pod", "Node", "Cluster", "Orchestrator"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Kubernetes

## Definition

**Kubernetes (K8s)** is the **container orchestrator**: it **schedules, scales, heals, and networks** container workloads across a **cluster** of **nodes**. Core objects: **pods** (smallest unit — one+ containers sharing an IP), **deployments** (desired state), **services** (stable network entry), **namespaces**. For network engineers: K8s brings **CNI plugins (Calico, Flannel, Cilium)** and an overlay-scale networking model.

## The Cluster Shape

```text
control plane: API server, scheduler, etcd (the "brain" nodes)
worker nodes: kubelet + container runtime (Docker/containerd) run pods
pod = containers + shared network namespace (one IP per pod)
service = stable VIP/DNS in front of pods (selector → endpoints)
```

## Exam Focus

- **"What orchestrates containers?" → Kubernetes** — the definition; "what is a pod?" → the atomic scheduling unit.
- **Control plane vs worker nodes**: API/scheduler/etcd vs kubelet+runtime — the role split.
- **K8s networking**: pod IPs, service VIPs, CNI — "how do components talk?" the network angle (overlays, e.g. Calico/Flannel).
- Desired state: deployments reconcile actual→desired (self-healing) — the "what happens if a pod dies?" answer.

## Related Terms

- [[Container]], [[Docker]], [[Public Cloud]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/05. Kubernetes Basics]]