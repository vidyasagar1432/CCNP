---
tags: [CCNP, glossary, physical, networking]
aliases: ["Shielded Twisted Pair", "ScTP", "F/UTP", "S/FTP", "STP Cabling"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Shielded Twisted Pair

## Definition

**Shielded Twisted Pair (STP / ScTP / F/UTP / S/FTP)** adds a **conductive shield** (foil or braid) around the twisted pairs or the whole bundle, rejecting external EMI and crosstalk in exchange for higher cost and stricter grounding requirements.

> Note: this term is cabling **STP** — do not confuse with Spanning Tree Protocol ([[STP]]).

## When to Use Copper Shielding

- Industrial / factory floors (motor noise, VFDs) where EMI is high.
- 10 Gbps runs over Cat6/6A at the longer end of reach.
- Cross-talk-heavy bundles and high-density IDF closets.

## Trade-offs vs [[UTP]]

| Factor | UTP | Shielded |
| --- | --- | --- |
| Cost | Low | Higher (cable + connectors + grounded panels) |
| EMI immunity | Moderate | High (needs proper ground!) |
| Bend/install | Easy | Stiffer, careful termination |

## Exam Focus

- **One endpoint per shielding type matters**: mixing shielded/unanchored segments can break grounding — a troubleshooting story.
- Alias game: F/UTP (foil over pairs), S/FTP (braid + foil) — the exam may ask what the letters mean.
- Otherwise expect the UTP vs shielded comparison (cost/reach/EMI).

## Related Terms

- [[UTP]], [[Ethernet]], [[Connectors]], [[Fiber]]
- Level 01 notes: [[Level 01 - Physical Layer/01. Cables/02. STP]]