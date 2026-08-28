---
tags: [CCNP, glossary, troubleshooting, networking]
aliases: ["Troubleshooting", "Network Troubleshooting", "OSI Troubleshooting", "Divide and Conquer"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Troubleshooting
created: 2026-08-29
---

# Troubleshooting

## Definition

**Troubleshooting** is a **systematic method** for finding why the network misbehaves — not magic. The core approaches: **bottom-up** (start at Layer 1 — the physical link — and work up), **top-down** (start at the application), and **divide-and-conquer** (pick a middle layer, e.g. ping at L3, then narrow). Tools: **ping/traceroute**, `show` commands, **debuge**, logs ([[Syslog]]), captures ([[Wireshark]]), and measurements ([[IP SLA]]).

## The Method

```text
1. gather symptoms (what broke, what changed?) — change management is your friend
2. hypothesize (Layer 1? config? routing? policy?)
3. verify with tools: ping → traceroute → show ip interface/route → debugs — 
   bottom-up or top-down; document everything
4. fix, verify the fix, and note the root cause (not the symptom)
```

## Exam Focus

- **"Which troubleshooting approach starts at the OSI bottom?" → bottom-up** — the model questions (bottom-up vs top-down vs divide-and-conquer).
- **First questions**: "what changed?" + documentation — the professional answer over guesswork.
- **Tool scoping**: ping (L3 reachability), traceroute (path), `show` (state), debug (detail, carefully!) — the tool-match matrix.
- Root cause vs symptom: fixing the symptom = repeat incident — the closing principle.

## Related Terms

- [[OSI Model]], [[IP SLA]], [[Wireshark]], [[Syslog]], [[Syslog]]
- Level 29 notes: [[Level 29 - Troubleshooting/Troubleshooting Overview]]