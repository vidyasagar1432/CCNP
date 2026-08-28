---
tags: [CCNP, glossary, bgp, routing, policy]
aliases: ["Policy-Based Routing", "PBR"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Policies
created: 2026-08-29
---

# Policy-Based Routing

## Definition

**Policy-based routing (PBR)** forwards packets based on **policy criteria** — source address, protocol, DSCP, length, interface — instead of the destination-based routing table. It lets you route "interesting" traffic differently from everything else.

## How It Works

```text
route-map PBR permit 10
 match ip address 101        ! interesting traffic (acl 101)
 set ip next-hop 10.0.0.2    ! send it a specific way
 set ip precedence 5         ! and mark it

interface GigabitEthernet0/0
 ip policy route-map PBR     ! applied inbound
```

- Applied **inbound on an interface**.
- Matching uses ACLs / prefix lists / route-maps (see [[Route Map]], [[Prefix List]]).
- **set ip next-hop**, `set ip default next-hop`, `set interface`, marking (QoS) are the main actions.

## Exam Focus

- **PBR is not BGP policy** — it is *forwarding* policy (layer 3), applied before the routing table lookup for matched traffic.
- The route-map must be **permitted**; if no match, normal destination routing applies (default behavior).
- **`ip policy route-map` on the interface** is the trigger; the same route-map could filter/attribute-manipulate in BGP (see [[Route Map]]).
- ENCOR ties PBR to QoS marking and traffic engineering scenarios.

## Related Terms

- [[Route Map]], [[Prefix List]], [[BGP]]
- Level 12 notes: [[Level 12 - BGP/11. Policy Routing]]