---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Peer-to-Peer", "P2P"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Peer-to-Peer

## Definition

**Peer-to-peer (P2P)** networking treats every node as an **equal peer**: each device can both request and provide services directly, with **no dedicated central server** and no central point of control.

## How It Works

```text
device A ◄──► device B
    equal peers: share files, print, chat directly

scaling limit: N devices → up to N×(N−1)/2 direct relations
```

| Trait | P2P | Client-Server |
| --- | --- | --- |
| Roles | Every node serves + requests | Centralized providers |
| Control | Distributed (harder to manage) | Central policy point |
| Best for | Small workgroups | Enterprise-scale services |

## Exam Focus

- **The role-symmetry is the exam point**: no server, any node can serve — vs [[Client-Server]] centralization.
- P2P scaling and security concerns (every peer is an attack surface) justify *not* using it in large enterprises.
- Microsoft "workgroup" vs "domain" maps directly to P2P vs client-server.

## Related Terms

- [[Client-Server]], [[End Device]], [[LAN]]
- Level 00 notes: [[Level 00 - Networking Basics/04. Peer-to-Peer]]