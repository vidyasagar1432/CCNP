---
tags: [CCNP, glossary, virtualization, cloud]
aliases: ["Docker", "Dockerfile", "Docker Image", "Docker Registry", "Docker Compose"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Virtualization & Cloud
created: 2026-08-29
---

# Docker

## Definition

**Docker** is the most common **container runtime/platform**: you write a **Dockerfile** (build recipe) → **build an image** (immutable snapshot) → share it via a **registry** (Docker Hub) → **run containers** anywhere Docker exists. It popularized containers with an easy CLI and tooling (Compose for multi-container stacks).

## The Pipeline

```text
Dockerfile (FROM base, COPY, RUN, EXPOSE, CMD) → docker build → image
image (layered, immutable) → registry (pull/push) → docker run → container
state: containers are ephemeral — data lives in volumes/mounts
```

## Exam Focus

- **"What is Docker?" → container runtime + image/build/registry tooling** — the definition; it packages, not virtualizes.
- **Image vs container**: blueprint vs running instance — the state question (containers ephemeral, volumes for data).
- **Dockerfile basics**: FROM (base image), RUN, COPY, CMD — the recognition.
- Docker vs Kubernetes: Docker = runtime per host; K8s = orchestration across hosts — the scale contrast ([[Kubernetes]]).

## Related Terms

- [[Container]], [[Kubernetes]]
- Level 25 notes: [[Level 25 - Virtualization & Cloud/04. Docker]]