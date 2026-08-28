---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Router ID", "OSPF Router Identifier"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# OSPF Router ID

## Definition

The **OSPF Router ID (RID)** is a 32-bit number that uniquely identifies a router in the OSPF domain. It is *not* an address that must exist in routing tables — it is an identifier used in neighbor sessions, LSAs, and election processes.

## Selection Order

1. **Configured** value — `router-id 1.1.1.1` (highest priority)
2. Highest IP of any **loopback** interface
3. Highest active **physical** interface IP

```cisco
router ospf 1
 router-id 1.1.1.1
```

## Key Facts

- The RID is chosen at OSPF startup; changing `router-id` requires a **manual restart** (`clear ip ospf process`) to take effect.
- Two routers with the **same RID** cannot form a valid adjacency — a classic exam-trap scenario (`show ip ospf neighbor` shows stuck ExStart/Exchange).
- The RID is carried in Type-1 Router LSAs and used for [[DR BDR]] election.

## Exam Focus

- **Loopbacks are preferred** in the default selection, so production configs almost always hard-code `router-id`.
- RID **does not have to be a routable address** and does not have to participate in OSPF.
- On RID change, OSPF tears down and rebuilds adjacencies — expect an outage.

## Related Terms

- [[OSPF]], [[OSPF Neighbor States]], [[DR BDR]]
- Level 10 notes: [[Level 10 - OSPF/03. Router ID]]