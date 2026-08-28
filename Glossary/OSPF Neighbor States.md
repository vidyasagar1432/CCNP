---
tags: [CCNP, glossary, ospf, routing]
aliases: ["OSPF Neighbor States", "2-Way", "ExStart", "Exchange", "Loading", "Full State"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# OSPF Neighbor States

## Definition

The **OSPF neighbor state machine** describes the lifecycle of a neighbor relationship, from first detection to full adjacency. Knowing the states — and which ones are normal vs stuck — is essential for troubleshooting.

## The States

| State | Meaning | Reachable via |
| --- | --- | --- |
| Down | No hellos received | — |
| Init | Hello received, not yet bidirectional | Hello |
| 2-Way | Both routers see each other — **DR/BDR election happens here** | Hello |
| ExStart | Negotiating master/slave + initial DBD sequence | DBD packets |
| Exchange | Exchanging database descriptions (DBD) | DBD |
| Loading | Requesting/sending missing LSAs | LSR/LSU/LSAck |
| Full | Adjacency complete; LSDBs in sync | All |

On point-to-point links, routers go **2-Way → Full**; on multi-access, they stop at **2-Way** with non-DR neighbors (adjacency only with the [[DR BDR]]).

## Common Stuck States

| Stuck at | Typical cause |
| --- | --- |
| Init / ExStart | Mismatched MTU, filtering multicast 224.0.0.5/6 |
| Exchange | Mismatched network type / MTU / RID duplicate |
| 2-Way | Expected if neither is DR/BDR on multi-access |

## Exam Focus

- **Full = adjacency formed**; 2-Way is normal only for non-DR neighbors on broadcast segments.
- Neighbors **must agree on area, hello/dead timers, network type, authentication, and subnet** to move past Init/2-Way.
- Read `show ip ospf neighbor` — a column showing a permanent/ExStart state almost always means MTU mismatch.

## Related Terms

- [[OSPF]], [[DR BDR]], [[OSPF Router ID]], [[Link State Database]]
- Level 10 notes: [[Level 10 - OSPF/04. Neighbor States]]