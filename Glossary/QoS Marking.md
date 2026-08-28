---
tags: [CCNP, glossary, qos, networking]
aliases: ["QoS Marking", "Marking", "802.1p", "CoS", "IP Precedence"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# QoS Marking

## Definition

**Marking** **writes** a QoS value into the packet (or frame) so downstream devices share one view of the traffic's class — the "paint it once, trust it everywhere" model. Markers: **L2 802.1p CoS** (3 bits, in the trunk tag), **L3 IP precedence** (3 bits) / **[[DSCP]]** (6 bits, superset), **MPLS EXP**. Marking is done once at the [[Trust Boundary|trust boundary]]; everything downstream just classifies the mark.

## The Marking Ladder

```text
CoS (3 bits, L2) ─► IP precedence (3 bits, L3) ─► DSCP (6 bits, L3) ─► EXP (MPLS)
typical map: voice = CoS 5 / EF ; video = CoS 4 / AF41 ; data = CoS 0–3 / default-AF
highest fidelity survives: DSCP is the richest (64 values vs 8)
```

## Exam Focus

- **"Which QoS step writes DSCP/CoS?" → marking** vs classification (reads) — the pair question.
- **3-bit vs 6-bit**: CoS/IP-prec = 8 values; DSCP = 64 — the capacity question; DSCP preferred for its granularity.
- "Where to mark?" → as close to the source as possible, at the trust boundary — the design rule.
- Marking is a **trusted-domain** idea: remark/re-classify when crossing admin domains — security nuance.

## Related Terms

- [[QoS Classification]], [[DSCP]], [[Trust Boundary]], [[DiffServ]]
- Level 21 notes: [[Level 21 - QoS/02. Marking]], [[Level 21 - QoS/12. QoS Marking & Trust Boundaries]]