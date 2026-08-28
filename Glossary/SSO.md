---
tags: [CCNP, glossary, high-availability, networking]
aliases: ["SSO", "Stateful Switchover", "Stateful Failover", "Dual Supervisor"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: High Availability
created: 2026-08-29
---

# SSO

## Definition

**SSO (Stateful Switchover)** keeps **control-plane state synchronized** between the **active and standby supervisors/route processors**: hardware, software state (adjacencies, sessions, config) — so a **switchover causes no forwarding interruption**. It's the engine underneath **[[NSF]]** and **[[ISSU]]** on dual-supervisor chassis.

## How It Works

```text
active RP/SUP: runs the network; standby tracks its state (bulk sync + incremental)
failure → switchover: standby takes over WITH state (no re-learning, no flap)
what's synced: CEF/RIB, L2/L3 adjacencies, HSRP, QoS, ACL state
compared to RPR (no state): RPR = reboot + re-learn; SSO = instant, stateful
```

## Exam Focus

- **"What makes a supervisor failover lossless?" → SSO (stateful switchover)** — the definition; "state kept: CEF/adjacencies/protocols" — the sync answer.
- **SSO vs RPR**: state (SSO) vs no-state (RPR — full re-initialization) — the switchover-mode question.
- **The pair**: SSO = hardware/control plane; [[NSF]] = routing protocols keep forwarding — the combination question.
- **What's NOT synced**: in-flight data-plane inflight packets, netflow caches — the nuance ("what resets?").

## Related Terms

- [[NSF]], [[ISSU]], [[Redundant Supervisors]], [[High Availability]]
- Level 27 notes: [[Level 27 - High Availability/01. SSO]]