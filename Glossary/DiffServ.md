---
tags: [CCNP, glossary, qos, networking]
aliases: ["DiffServ", "Differentiated Services", "Per-Hop Behavior", "PHB", "DSCP-based QoS"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# DiffServ

## Definition

**DiffServ (Differentiated Services)** is the scalable QoS architecture: each packet **carries its own class** in the **DSCP** field, and every router applies the class's **PHB (per-hop behavior)** locally — no signaling, no per-flow state, no end-to-end reservations. The contrast: [[IntServ]] reserves per flow; DiffServ trusts the **marking + trust boundary** model. This is what enterprise QoS actually runs.

## The DiffServ Model

```text
edge: classify + mark DSCP once (trust boundary — see [[Trust Boundary]])
core: per-hop behavior only (EF = strict priority, AF = assured forwarding, CS = class selector)
no reservation, no signaling — the marking IS the contract
43 DSCP values in use; 64 possible; PHBs: EF, AFxy (4 classes × 3 drops), CS0–7
```

## Exam Focus

- **"Which QoS architecture marks packets and treats them per-hop?" → DiffServ** — the definition; vs IntServ's RSVP reservations — the architecture choice question.
- **PHB = per hop behavior**; DSCP selects it — “what determines behavior at each router?” → DSCP→PHB.
- **Why DiffServ scales**: no state per flow, no signaling — the enterprise default justification.
- The [[DSCP]] values (EF/AF/CS) are DiffServ's vocabulary — the exam's favorite table.

## Related Terms

- [[DSCP]], [[IntServ]], [[QoS Marking]], [[Trust Boundary]], [[QoS Classification]]
- Level 21 notes: [[Level 21 - QoS/07. DiffServ]]