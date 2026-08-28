---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Network Design Principles", "Design Fundamentals"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Network Design Principles

## Definition

**Design principles** are the *why* behind topology choices: **hierarchical, modular, resilient, scalable, secure** — designs should bound failure domains, avoid single points of failure, and leave room to grow without redesign.

## The Core Principles

| Principle | Meaning | Example practice |
| --- | --- | --- |
| **Hierarchy** | Layers with distinct jobs | [[Enterprise Network Architecture|Core/Distribution/Access]] |
| **Modularity** | Self-contained building blocks | Campus / WAN / DC modules |
| **Redundancy** | No single point of failure | Dual core, [[EtherChannel]], [[First Hop Redundancy Protocol|FHRP]] |
| **Failure-domain bounding** | Small units of impact | VLANs, [[STP]] tuning, isolation ACLs |
| **Scalability** | Growth without redesign | Summarization, [[BGP Aggregation|aggregation]] |
| **Security** | Defense in depth | 802.1X, [[ACL]]s, segmentation |

## How to Apply (Exam Story)

- **"Why two core switches?"** → redundancy + failure-domain bounding.
- **"Why separate VLANs?"** → limit broadcast domain, security, and failure blast radius.
- Design answers should always cite **which principle** the change serves — the exam rewards principled reasoning over memorized configs.

## Exam Focus

- Questions ask you to *justify* architecture — map every design decision to a principle (redundancy most often).
- Know the classic **3-layer design vs flat design** trade-off and where each is appropriate.
- The later levels (STP, FHRP, [[EtherChannel]], QoL) exist because of these principles.

## Related Terms

- [[Enterprise Network Architecture]], [[LAN]], [[EtherChannel]], [[First Hop Redundancy Protocol]]
- Level 00 notes: [[Level 00 - Networking Basics/07. Network Design Principles]]