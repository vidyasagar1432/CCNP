---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Decapsulation Process", "Header Stripping"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSI & TCP/IP
created: 2026-08-29
---

# Decapsulation

## Definition

**Decapsulation** is the receiving side of [[Encapsulation]]: **bottom-up**, each layer **strips and validates its own header/trailer**, then hands the remaining payload to the layer above — until the application receives the original data.

## How It Works

```text
bits
   ▼ Ethernet header checked, FCS verified → frame → payload →
   ▼ IP header checked (TTL, protocol)     → packet → payload →
   ▼ TCP/UDP header checked (ports)        → segment → payload →
application data
```

- **Validation matters**: bad FCS → frame dropped at L2; bad checksum/TTL → packet dropped at L3; wrong port → segment dropped at L4.
- Routers perform **partial decapsulation** (link + network headers) and re-encapsulate — only the endpoints do the full strip.

## Exam Focus

- **"What does the receiving host do first?"** → strip the L2 frame, then L3, then L4 — bottom-up order.
- The FCS/checksum responsibilities per layer are classic "who checks what" questions.
- Pair with encapsulation: source pushes down, destination peels up — the two are mirror images.

## Related Terms

- [[Encapsulation]], [[PDU]], [[OSI Model]], [[TCP-IP Model]]
- Level 03 notes: [[Level 03 - OSI & TCP IP/04. Decapsulation]]