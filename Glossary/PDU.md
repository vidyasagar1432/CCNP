---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Protocol Data Unit", "Segment", "Packet", "Frame"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSI & TCP/IP
created: 2026-08-29
---

# PDU

## Definition

A **Protocol Data Unit (PDU)** is the unit of data at a given layer: that layer's **header (+trailer) plus the payload** from the layer above. Each layer has its own PDU name — the vocabulary of [[Encapsulation|encapsulation]].

## The PDU Names

| Layer | PDU name |
| --- | --- |
| Application | Data |
| Transport (TCP/UDP) | **Segment** |
| Network (IP) | **Packet** |
| Data Link (Ethernet) | **Frame** |
| Physical | Bits (symbols) |

```text
data → segment → packet → frame → bits
              (encapsulation down)
frame → packet → segment → data
              (decapsulation up)
```

## Exam Focus

- **Name-per-layer is a 1-point staple**: "what is an IP packet called at L2?" → frame.
- The same bytes change names as headers are added/removed — questions test *when* the name changes (at each layer boundary).
- Related "sdu" nuance (service data unit = payload) is a nice-to-know differentiator on edge questions.

## Related Terms

- [[Encapsulation]], [[Decapsulation]], [[OSI Model]], [[TCP-IP Model]]
- Level 03 notes: [[Level 03 - OSI & TCP IP/05. PDUs]]