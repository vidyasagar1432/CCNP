---
tags: [CCNP, glossary, routing, networking]
aliases: ["Default Route", "Default Gateway", "0.0.0.0/0", "Quad Zero"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Routing Fundamentals
created: 2026-08-29
---

# Default Route

## Definition

A **default route** — `0.0.0.0/0` — is the **catch-all**: any destination with no more-specific match forwards there. It is the **router answering host's default gateway**, the **stub's way out**, and the **edge's path to the ISP**. Longest-prefix match makes it the *last* route consulted (prefix length 0 loses to everything).

## Where Defaults Appear

```text
host:     ip route default gateway 10.1.0.1        (gateway-of-last-resort)
router:   ip route 0.0.0.0 0.0.0.0 10.1.0.1        (static catch-all)
dynamic:  default-information originate            (OSPF injects default into area)
          redistribute static (the same static)    (EIGRP/BGP announce it)
```

## Exam Focus

- **Longest-match logic**: a packet for `10.1.1.5` matches `10.1.1.0/24` (24 bits) *before* `0.0.0.0/0` (0 bits) — the default is only a safety net. 
- "Which route type matches everything not more specifically known?" → default.
- The **default gateway of hosts** = their router's interface address (the [[Routing Table]]'s connected/static deal), not the default route itself — keep the two vocabularies straight in scenario questions.

## Related Terms

- [[Static Routing]], [[Floating Static]], [[Routing Table]], [[OSPF]]
- Level 09 notes: [[Level 09 - Routing Fundamentals/10. Default Route]]