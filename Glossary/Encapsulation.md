---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Encapsulation Process", "Header Addition"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSI & TCP/IP
created: 2026-08-29
---

# Encapsulation

## Definition

**Encapsulation** adds **headers (and trailers)** as data travels **down** the protocol stack: application → transport → network → link. Each layer wraps the previous layer's output in its own header — like nesting envelopes — so every hop can deliver it one level closer to the destination.

## The Stack of Headers

```text
application data
   ▼ add TCP/UDP     →   segment (sport/dport, seq, checksum)
   ▼ add IP          →   packet  (src/dst IP, TTL, proto)
   ▼ add Ethernet    →   frame   (src/dst MAC, EtherType, FCS)
   ▼ physical        →   bits
```

- **Source builds down; destination tears down (see [[Decapsulation]])**.
- Each header is addressed for its layer: MAC = next hop, IP = end-to-end, port = application.
- Overhead grows per hop until the [[MTU]] limit — tunneling adds yet more headers ([[MTU]] note).

## Exam Focus

- **"Which order do headers get added?"** → transport → network → link, always in that order.
- Know which PDU name applies at each step (see [[PDU]]): segment → packet → frame.
- Every intermediate router touches the **link + network** headers only; final host strips the rest.

## Related Terms

- [[Decapsulation]], [[PDU]], [[OSI Model]], [[TCP-IP Model]], [[MTU]]
- Level 03 notes: [[Level 03 - OSI & TCP IP/03. Encapsulation]]