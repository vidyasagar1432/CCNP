---
tags: [CCNP, glossary, switching, networking]
aliases: ["L2 Filtering", "Frame Filtering"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Filtering

## Definition

**Filtering** at Layer 2 means the switch **deliberately does not send a frame out a given port** — the complement of [[Forwarding]]. The classic case: a frame destined to a MAC learned on the **same ingress port** never echoes back out that port.

## Why Filtering Exists

```text
host A ── port 1 ── switch ── port 2 ── host B
frame A→B: CAM says B is on port 2 → forward to port 2, NOT port 1
frame A→A (same port): drop — no need to send it back out port 1
```

- A switch **never forwards a frame out the port it came in on** — the fundamental difference from a hub.
- Filtering also covers intentional drops: port shutdown, [[Port Security]] violations, storm control, ACLs applied at L2.

## Exam Focus

- **"Why doesn't the frame go back out the ingress port?"** → filtering — the switch's one-port-per-segment discipline.
- Filtering is what makes switches better than hubs: no echoes, no wasted bandwidth.
- Filtering + [[MAC Learning|learning]] + [[Forwarding|forwarding]] + [[Flooding|flooding]] = the four L2 primitives — expect them as a group in one question.

## Related Terms

- [[Forwarding]], [[Flooding]], [[CAM Table]], [[MAC Learning]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/07. Filtering]]