---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["IPv4 Broadcast", "Directed Broadcast", "Limited Broadcast", "255.255.255.255"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# IPv4 Broadcast

## Definition

An **IPv4 broadcast** is a packet addressed to **all hosts on a network**: either **limited** (`255.255.255.255`, this subnet only) or **directed** (all-ones host bits of a subnet, e.g. `10.1.1.255/24` — routable to that subnet). Routers forward directed broadcasts only if configured (`ip directed-broadcast`).

## Broadcast Types

```text
limited 255.255.255.255  → never forwarded by any router
directed 10.1.1.255/24   → routers may forward if enabled (default: off)
how hosts see it: L2 destination FF:FF:FF:FF:FF:FF ([[Broadcast Domain|broadcast]])
```

⚠️ Directed broadcasts are a classic **smurf-amplification attack** vector — that's why they're **disabled by default** on Cisco interfaces.

## Exam Focus

- **"Which address reaches every host in the subnet?"** → subnet broadcast = network's host bits all 1.
- Routers **do not forward limited broadcasts**; the [[Broadcast Domain]] boundary lives at L3.
- Directed broadcast vs multicast confusion: multicast is [[IPv4 Multicast|224/4, group-based, routable]] — a DIFFERENT mechanism.

## Related Terms

- [[IPv4]], [[Broadcast Domain]], [[IPv4 Multicast]]
- Level 05 notes: [[Level 05 - IPv4/09. Broadcast]]