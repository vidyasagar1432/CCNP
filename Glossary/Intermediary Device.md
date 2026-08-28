---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Intermediary Device", "Network Device", "Intermediate Device"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Intermediary Device

## Definition

An **intermediary device** sits **between end devices** and is tasked with **moving and shaping data**: switches forward frames, routers forward packets, firewalls filter, and wireless APs bridge radio to wire. They are the infrastructure of the network.

## The Main Roles

| Device | Layer | Job |
| --- | --- | --- |
| Switch | 2 ([[LAN]]) | Forwards frames by MAC ([[VLAN]] segmentation) |
| Router | 3 | Forwards packets by IP, runs routing protocols |
| Firewall | 3–4+ | Policy enforcement, NAT, intrusion defense |
| AP / WLC | 2/3 | 802.11 bridging and management ([[WLAN]]) |
| Load balancer | 4–7 | Distributes app traffic |

## How They Think: Planes

Intermediary devices run on three planes (see [[Data Plane]], [[Control Plane]], [[Management Plane]]):

- **Data plane** — fast-path forwarding (ASIC/hardware).
- **Control plane** — routing/[[STP]]/ARP protocols (CPU).
- **Management plane** — SSH/SNMP/NETCONF access.

## Exam Focus

- **The end-vs-intermediary split** is a classification staple: "which devices are intermediaries?" → switches, routers, firewalls, APs.
- Envision *where* a device sits: intermediaries *do* forward others' traffic; [[End Device|end devices]] do not.
- Plane questions target intermediary devices specifically (SDN/[[NETCONF]]/telemetry pre-reqs).

## Related Terms

- [[End Device]], [[Data Plane]], [[Control Plane]], [[Management Plane]], [[LAN]]
- Level 00 notes: [[Level 00 - Networking Basics/05. Network Components]]