---
tags: [CCNP, glossary, qos, networking]
aliases: ["MQC", "Modular QoS CLI", "Class Map", "Policy Map", "Service Policy"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# MQC

## Definition

**MQC (Modular QoS CLI)** is Cisco's standard way to build QoS: three building blocks composed on any interface —

1. **class-map** — **match** traffic ([[QoS Classification]]),
2. **policy-map** — the **actions** per class (mark, police, shape, queue, WRED — see [[Policing]]/[[Shaping]]/[[Queuing]]/[[WRED]]),
3. **service-policy** — **attach** it to an interface (in or out).

Everything modern QoS config on IOS is MQC — recognizing the pattern answers half the config questions.

## The Pattern

```text
class-map match-any VOICE
  match ip dscp ef
!
policy-map EDGE
  class VOICE
    priority 128          (LLQ)
  class DEFAULT
    bandwidth percent 25  (CBWFQ)
    random-detect dscp-based  (WRED)
!
interface GigabitEthernet0/0
  service-policy output EDGE
```

## Exam Focus

- **"What are the three MQC components?" → class-map / policy-map / service-policy** — the structure question; "attach to interface" = service-policy.
- Match (class-map) vs action (policy-map) vs attach (service-policy) — mapping each statement type to its block.
- `match any` vs `match all`/`match-any` semantics — the class-matching subtlety.
- Config questions love "which command applies the policy?" → `service-policy input|output`.

## Related Terms

- [[QoS Classification]], [[Policing]], [[Shaping]], [[Queuing]], [[WRED]], [[CBWFQ]], [[LLQ]]
- Level 21 notes: [[Level 21 - QoS/09. Modular QoS CLI]]