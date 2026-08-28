---
tags: [CCNP, glossary, fundamentals, networking, topologies]
aliases: ["Three-Tier Architecture", "Core Distribution Access", "Hierarchical Network"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Topologies
created: 2026-08-29
---

# Three-Tier

## Definition

The **three-tier (hierarchical) model** layers the LAN as **Core → Distribution → Access**, Cisco's classic campus framework. Each tier has a distinct job — which is exactly what makes the design predictable and scalable (see [[Enterprise Network Architecture]]).

## The Layers

```text
CORE         |  high-speed backbone: route fast, NO policy
  ▲          |
DISTRIBUTION |  routing boundary: policy, [[VLAN]] routing, [[ACL]]s, summarization
  ▲          |
ACCESS       |  user ports: [[VLAN]] membership, [[PortFast]], security (802.1X, DHCP snooping)
```

| Layer | Priority | Failure isolation |
| --- | --- | --- |
| Access | Connect + secure users | Port/VLAN scope |
| Distribution | Aggregate + enforce | Per-building block |
| Core | Move traffic (speed only) | Redundancy everywhere ([[EtherChannel]], FHRP) |

## Exam Focus

- **Layer function mapping is guaranteed exam material** — "policy enforcement lives at which layer?" → distribution.
- Compare to **[[Collapsed Core|two-tier]]** (small sites merge core+distribution) and **[[Spine-Leaf]]** (data center flattens it further).
- Design questions reward citing *why* (bounded failure domains, hierarchy) over raw memorization.

## Related Terms

- [[Enterprise Network Architecture]], [[Collapsed Core]], [[Spine-Leaf]], [[Network Design Principles]], [[Enterprise Campus]]
- Level 02 notes: [[Level 02 - Network Topologies/08. Three-Tier]]