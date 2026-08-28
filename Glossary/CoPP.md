---
tags: [CCNP, glossary, security, control-plane]
aliases: ["CoPP", "Control Plane Policing"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# CoPP

## Definition

**CoPP (Control Plane Policing)** protects the **router's CPU** (the [[Control Plane]]) by applying **QoS policies to traffic destined to the control plane** — protocols get exactly the resources they need (BGP/OSPF/SSH preserved) while floods of garbage are dropped before they starve the CPU. It's the "keep the router's brain alive under attack" tool.

## The Pattern

```text
class-map CONTROL: match protocol bgp / ospf / ssh / snmp …
class-map ATTACK:  match access-group DENY_LIST …
policy-map CP-POLICY
  class CONTROL:  police 128000 conform transmit exceed drop
  class ATTACK:   drop
control-plane
  service-policy input CP-POLICY
(verify: show policy-map control-plane)
```

## Exam Focus

- **"Which tool polices traffic sent to the router's CPU?" → CoPP** — the definition; `control-plane` interface = the recognition point.
- **Why it matters**: CPU exhaustion from floods breaks routing protocols and management (the availability attack) — "what gets affected in a melee?" → routing/management.
- CoPP = [[QoS]]'s policing applied at the control plane — the conceptual bridge to [[QoS]].
- **Be careful**: don't police legitimate BGP/OSPF to death — the "what belongs in the protect class?" design question.

## Related Terms

- [[Control Plane]], [[QoS]], [[ACL]], [[Management Plane]]
- Level 17 notes: [[Level 17 - Security/09. CoPP]]