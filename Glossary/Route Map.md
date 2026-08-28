---
tags: [CCNP, glossary, bgp, routing, policy]
aliases: ["Route Map", "Route-Map", "route-map"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Policies
created: 2026-08-29
---

# Route Map

## Definition

A **route map** is the general-purpose policy engine of the Cisco CLI: an ordered list of **match/set blocks** used for BGP attribute manipulation, redistribution filtering, [[Policy-Based Routing|PBR]], NAT, and more.

## Structure

```text
route-map NAME permit|deny SEQUENCE
  match ...      ← condition(s)
  set ...        ← action(s)

evaluation: like an ACL — first matching sequence wins; implicit deny at end
permit + no match → fall-through to next sequence (ACL-style)
```

```cisco
route-map SET-HIGH permit 10
 match ip address prefix-list IMPORTANT
 set local-preference 200
route-map SET-HIGH permit 20      ! everything else passes unchanged
```

## Uses

| Context | Command |
| --- | --- |
| BGP neighbor policy | `neighbor X route-map NAME in/out` |
| Redistribution filtering | `redistribute ospf 1 route-map NAME` |
| PBR | `ip policy route-map NAME` (see [[Policy-Based Routing]]) |
| NAT | `ip nat inside source ... route-map NAME` |
| Conditional advertising | `neighbor X advertise-map ...` |

## Exam Focus

- **permit + set** is the "allow and modify" pattern; **deny** stops the policy (implicit deny at the end affects filtering).
- Route-maps do not *short-circuit* like ACLs: a matched permit can still fall through to later sequences when nothing was set (compare "no match → next" behavior).
- **Match tools in BGP contexts:** prefix lists ([[Prefix List]]), communities, AS-path ACLs — each prefers an appropriate tool.

## Related Terms

- [[BGP]], [[Prefix List]], [[Communities]], [[Policy-Based Routing]], [[Local Preference]], [[MED]]
- Level 12 notes: [[Level 12 - BGP/13. Route Maps]]