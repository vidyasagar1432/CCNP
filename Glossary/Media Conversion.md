---
tags: [CCNP, glossary, physical, networking]
aliases: ["Media Converter", "Fiber to Copper Converter"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Physical Layer
created: 2026-08-29
---

# Media Conversion

## Definition

**Media conversion** changes the physical medium at the bit level — typically **fiber ↔ copper (RJ45)** or multimode ↔ single-mode — letting a single device sit on different media without changing its port type. Converters are transparent to frames (no L2/L3 changes).

## Use Cases

```text
switch (SFP copper) ── RJ45 ── converter ── fiber run ── converter ── RJ45 ── far switch
                                                        (or: SFP/GBIC direct fiber)
```

- Extend a link beyond 100 m of copper using existing fiber plant.
- Bridge MMF (short-reach optics) to SMF for longer spans.
- **Must run full duplex on both sides**; bad converters add latency and error sources.

## Exam Focus

- **Converters are transparent, but they still buffer** — they add minor latency and are failure points; prefer native fiber ports when possible.
- "Link up but flapping" on converted legs: check duplex auto-neg across the converter, then the optics (see [[Auto-Negotiation]], [[Transceiver]]).
- Frame size matters: verify the converter passes jumbo frames end-to-end (see [[MTU]]).

## Related Terms

- [[Transceiver]], [[Fiber]], [[UTP]], [[Duplex]]
- Level 01 notes: [[Level 01 - Physical Layer/06. Media Conversion]]