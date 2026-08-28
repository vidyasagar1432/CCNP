---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Enterprise Network Architecture", "Campus Design", "Core Distribution Access"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Enterprise Network Architecture

## Definition

**Enterprise network architecture** organizes network devices into **functional modules** (campus, WAN, data center, branch) instead of one flat fabric — making the network **predictable, scalable, secure, and manageable**. The centerpiece is the hierarchical **core / distribution / access** model.

## The Campus Hierarchy

```text
CORE        (high-speed backbone, no policy — route fast)
  ▲
DISTRIBUTION (routing boundary, policy + [[VLAN]]/[[ACL]] enforcement)
  ▲
ACCESS       (user ports: [[VLAN]], [[PortFast]], [[DHCP Snooping]], 802.1X)
```

| Layer | Job | Failure isolation |
| --- | --- | --- |
| Access | Connect [[End Device|end devices]] | Small [[VLAN]]/port-level failures |
| Distribution | Aggregate, enforce policy | Aggregates one failure domain per building |
| Core | Move traffic between distribution blocks | Redundancy everywhere ([[EtherChannel]]) |

## Expanded Model (Cisco)

- **Campus, WAN, Data Center, Branch, Teleworker** modules — each with its own design rules.
- Pairing: two switches/routers per layer (**redundancy**) with [[First Hop Redundancy Protocol|FHRP]] at gateways.

## Exam Focus

- **Know which layer does what**: access = user ports; distribution = policy/VLAN routing; core = no policy, just speed.
- "Where does a design change belong for <scenario>?" answers usually map to core/distribution/access.
- Later levels (STP tuning, [[EtherChannel]], [[First Hop Redundancy Protocol|HSRP/VRRP/GLBP]]) all assume this hierarchy.

## Related Terms

- [[Network Design Principles]], [[LAN]], [[End Device]], [[VLAN]], [[First Hop Redundancy Protocol]]
- Level 00 notes: [[Level 00 - Networking Basics/06. Enterprise Network Architecture]]