---
tags: [CCNP, glossary, qos, networking]
aliases: ["IntServ", "Integrated Services", "RSVP", "Resource Reservation Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# IntServ

## Definition

**IntServ (Integrated Services)** guarantees **per-flow, hard QoS end-to-end** by **reserving bandwidth before traffic flows** — via **RSVP** (Resource Reservation Protocol): each flow signals its needs, every router along the path admits/commits resources, and the flow gets a **guaranteed service** contract. Precise, but it **does not scale**: state per flow, signaling per flow. Rare in production; the exam contrast to [[DiffServ]].

## The Flow

```text
sender → RSVP PATH message (flow spec) → receivers → RSVP RESV back
each router: admission control → reserve queue + bandwidth for that flow
services: Guaranteed (hard bound) / Controlled Load (soft)
state = per-flow, everywhere → why it doesn't scale past small domains
```

## Exam Focus

- **"Which architecture reserves bandwidth per flow?" → IntServ/RSVP** — the definition; "hard QoS guarantee" keyword.
- **RSVP messages**: PATH (downstream) then RESV (upstream) — the signaling mechanism question.
- **Why not everywhere?** → scalability: per-flow state and signaling — "the limitation of IntServ" answer (they scale badly; DiffServ scales).
- IntServ-over-DiffServ hybrids exist (RSVP for voice call admission) — the nuance mention.

## Related Terms

- [[DiffServ]], [[LLQ]], [[RSVP]]
- Level 21 notes: [[Level 21 - QoS/08. IntServ]]