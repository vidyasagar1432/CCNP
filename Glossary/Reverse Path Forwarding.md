---
tags: [CCNP, glossary, multicast, routing]
aliases: ["Reverse Path Forwarding", "RPF", "RPF Check", "Unicast RPF", "uRPF"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# Reverse Path Forwarding

## Definition

**RPF (Reverse Path Forwarding)** is multicast's **loop- and spoof-prevention rule**: a multicast packet is accepted only if it arrived on the interface that the **unicast routing table** says leads **back to its source**. Fail the RPF check → drop. It's the "am I on the right path for THIS source?" test applied at every hop.

## RPF in Action

```text
unicast table: source 10.1.1.1 is via g0/0
multicast packet arrives:
  g0/0 → RPF pass → forward (and create/refresh (S,G) state)
  g0/1 → RPF fail → DROP (loop prevention + spoof-source defense)
variants: multicast RPF (per (S,G)) vs unicast RPF/uRPF (anti-spoof at edges)
```

## Exam Focus

- **"Which check prevents multicast loops by verifying the reverse path?" → RPF** — the mechanism definition.
- **"Why are multicast packets from a source silently dropped?" → RPF failure** — top troubleshooting answer (`show ip mroute` / `show ip rpf`).
- Asymmetric routing = RPF failures (the modern pain: ECMP/load-balancing) — the "what breaks RPF?" scenario.
- uRPF on the Internet edge = anti-spoofing; PIM-RPF on routers = forwarding sanity — the two-senses question.

## Related Terms

- [[PIM]], [[PIM-SM]], [[Multicast]], [[Routing Table]], [[ACL]]
- Level 19 notes: [[Level 19 - Multicast/08. Multicast Boundaries & RPF]]