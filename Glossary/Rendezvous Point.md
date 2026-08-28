---
tags: [CCNP, glossary, multicast, routing]
aliases: ["Rendezvous Point", "RP", "Multicast RP", "BSR", "Auto-RP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# Rendezvous Point

## Definition

The **RP (Rendezvous Point)** is the meeting place of [[PIM-SM]]: a designated router that **anchors the shared (*,G) tree** — sources register into it, receivers join toward it, and the tree is *built from the RP outward*. RP selection: **static** (manual), **Auto-RP** (Cisco), or **BSR** (PIM bootstrap router, RFC). A failed/misconfigured RP = multicast blackout.

## RP in Action

```text
receiver → (*,G) join toward the RP
source → registers (register/register-stop) through the RP
after SPT switchover the RP fades out of the fast path (but still anchors joins!)
RP discovery: static (ip pim rp-address <ip> <acl>)
              Auto-RP (mapping agent) / BSR (bootstrap messages, 224.0.0.13)
best practice: RP on a loopback, redundant (anycast RP / MSDP for multiple RPs)
```

## Exam Focus

- **"What device anchors the shared tree in sparse mode?" → the RP** — the definition; *any* multicast source/receiver path question routes through it initially.
- **RP election methods**: static vs Auto-RP vs BSR — with BSR being the standard-approach answer ("which is RFC/standard?" → BSR).
- **Anycast-RP/MSDP**: two RPs sharing the same loopback IP — the "how do you scale/redundancy RP?" answer.
- Failure symptom: "receivers can't get streams, unicast is fine, RP is down" — the troubleshooting scenario.

## Related Terms

- [[PIM-SM]], [[PIM]], [[Loopback Address]], [[Multicast]]
- Level 19 notes: [[Level 19 - Multicast/04. Rendezvous Point]]