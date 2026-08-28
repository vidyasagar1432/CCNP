---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["End Host", "Host", "End Station"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# End Device

## Definition

An **end device** is where data is **generated or consumed** — the source or destination of communication. PCs, servers, phones, printers, IP cameras, and IoT sensors are end devices; they sit at the **edge** of the network.

## Role in the Network

```text
end device (source) ──► intermediary devices ──► end device (destination)
    origin / sink of traffic        transport              origin / sink
```

- End devices run applications and use protocols **end to end** (HTTP, DNS, DHCP) that transit devices mostly carry untouched.
- They typically have **one attached interface** (except servers with multiple NICs) and do **no forwarding of other people's traffic** (hosts forwarding = a security red flag).
- Identification: MAC + [[IPv4|IP]] address (needs a default gateway → [[First Hop Redundancy Protocol|FHRP]] themes later).

## Exam Focus

- **End device vs [[Intermediary Device]] is a core classification question** — "PCs, printers, servers = end; switches, routers, firewalls = intermediary."
- Which plane does an end device have? Only the **data plane** of its own traffic — it has no control/management plane for the *network* (contrast with [[Control Plane]]).
- ENCOR scenarios: rogue host forwarding, DHCP server placement — trace back to end-device roles.

## Related Terms

- [[Intermediary Device]], [[Client-Server]], [[LAN]]
- Level 00 notes: [[Level 00 - Networking Basics/05. Network Components]]