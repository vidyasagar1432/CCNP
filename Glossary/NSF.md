---
tags: [CCNP, glossary, high-availability, networking]
aliases: ["NSF", "Nonstop Forwarding", "NSF Awareness", "Graceful Restart"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: High Availability
created: 2026-08-29
---

# NSF

## Definition

**NSF (Nonstop Forwarding)** keeps **traffic forwarding during control-plane recovery**: when the route processor restarts (supervisor switchover), the **data plane keeps forwarding** ([[CEF]] stays hot) while routing protocols **re-converge without flapping neighbors**. Peers that cooperate — **NSF awareness/graceful restart** — withhold route-down announcements and accept the restarting router back seamlessly.

## The NSF Dance

```text
RP switchover → control plane down, data plane keeps CEF-based forwarding
routing: peer routers (NSF-aware/graceful restart capable) don't declare
  the neighbor dead → no mass route flapping while the new RP re-learns
protocols: OSPF (RFC 3623 grace LSA), EIGRP (GR), BGP (GR capability)
```

## Exam Focus

- **"What keeps forwarding while the control plane restarts?" → NSF** — the definition; data plane (CEF) ≠ control plane (RP).
- **NSF alone vs SSO**: SSO = state sync (switchover), NSF = keep-forwarding-during-recovery — the complementary pair.
- **NSF with graceful restart peers**: "why don't neighbors drop routes?" → the GR handshake — the design question.
- What breaks without NSF-aware peers? → neighbors declare routes down → forwarding gap — the failure mode.

## Related Terms

- [[SSO]], [[CEF]], [[Redundant Supervisors]], [[ISSU]], [[OSPF]], [[BGP]]
- Level 27 notes: [[Level 27 - High Availability/02. NSF]]