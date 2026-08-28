---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["Named Mode EIGRP", "Named EIGRP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# Named Mode EIGRP

## Definition

**Named-mode EIGRP** is the modern EIGRP configuration model: one **named process** unifies IPv4 and IPv6 under a single router (config) tree, with **per-address-family and per-interface (af-interface) settings**. It replaces the classic `router eigrp <as>` + interface commands.

## Structure

```cisco
router eigrp CCNP-NET            ! named process
 address-family ipv4 unicast autonomous-system 100
  topology base
  af-interface GigabitEthernet0/0
   bandwidth-percent 80
   hello-interval 5
  exit-af-interface
  network 10.0.0.0
 address-family ipv6 unicast autonomous-system 100
  af-interface GigabitEthernet0/0
   summary-address ...
```

## Benefits

- Same configuration tree for IPv4 **and** IPv6 (single AS number).
- Consistent `af-interface` control: hello timers, authentication, stub, next-hop-self in one place.
- Modern exams and CCNP labs expect named mode over the legacy classic syntax.

## Exam Focus

- **Named mode = configuration model, not a protocol change** — DUAL/RTP/metrics are identical.
- Key commands: `router eigrp <name>`, `address-family ipv4 unicast autonomous-system <as>`, `af-interface`.
- Authentication and stub settings can live under the AF or per af-interface.

## Related Terms

- [[EIGRP]], [[EIGRP for IPv6]], [[EIGRP Authentication]], [[EIGRP Stub]]
- Level 11 notes: [[Level 11 - EIGRP/05. Named Mode]]