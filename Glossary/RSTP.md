---
tags: [CCNP, glossary, stp, switching]
aliases: ["Rapid Spanning Tree Protocol", "IEEE 802.1w"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# RSTP

## Definition

**RSTP (Rapid Spanning Tree Protocol, IEEE 802.1w)** is the rapid-convergence evolution of classic STP (802.1D) — same loop-prevention goal, much faster convergence through new port states, explicit roles, and a Proposal/Agreement handshake on point-to-point links.

## Key Differences from Classic STP

| Aspect | Classic STP | RSTP |
| --- | --- | --- |
| Port states | 5 | 3 (Discarding, Learning, Forwarding) |
| Roles | Root, Designated, Blocked | Root, Designated, **Alternate, Backup** |
| BPDU timing | Root-sourced every 2 s | **Every switch sends every hello** |
| Convergence | ~50 s worst case | ~1–3 s on point-to-point links |
| Failure detection | Timers only | **3 missed hellos** |

## Rapid Role Transition

On a **point-to-point full-duplex** link, RSTP uses Proposal/Agreement:

```text
SW-A: Proposal  ──►  SW-B
SW-B: syncs its own ports, then Agreement ──►  SW-A
port forwards immediately (no forward-delay wait)
```

This is why **link type matters**: the handshake only runs on point-to-point links; shared/half-duplex links fall back to classic timing.

## Edge Ports

An **edge port** (Cisco: [[PortFast]]) connects to an end host, not another switch. RSTP forwards immediately; if a BPDU arrives on an edge port, it is treated as a normal STP port (or shut down by [[BPDU Guard]]).

## Exam Focus

- **RSTP does not eliminate the Root Bridge** or the election process — it accelerates *convergence*, not topology logic.
- **Alternate is a role, Backup is a different role** — do not use them interchangeably.
- "RSTP is always 1–3 s" is false — it depends on topology and link type.

## Related Terms

- [[STP]], [[STP Port Roles]], [[STP Port States]], [[STP Timers]], [[PortFast]], [[MST]], [[PVST+]]
- Level 08 notes: [[Level 08 - STP/02. RSTP]], [[Level 08 - STP/04. Rapid PVST+]]