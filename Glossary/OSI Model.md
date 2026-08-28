---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["OSI Reference Model", "Seven-Layer Model", "OSI Layers"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSI & TCP/IP
created: 2026-08-29
---

# OSI Model

## Definition

The **OSI reference model (ISO/IEC 7498)** describes networking in **seven layers**, each with a distinct function. It is the **vocabulary** for troubleshooting and protocol discussion — not the protocol stack actually used (that is [[TCP/IP Model|TCP/IP]]).

## The Seven Layers

| # | Layer | Mission | Example protocols/units |
| --- | --- | --- | --- |
| 7 | Application | User services | HTTP, DNS, DHCP |
| 6 | Presentation | Encoding/encryption | TLS, codecs |
| 5 | Session | Dialog control | NetBIOS, RPC |
| 4 | Transport | End-to-end delivery | TCP, UDP (segment) |
| 3 | Network | Path selection/IP | IP, ICMP (packet) |
| 2 | Data Link | Hop-to-hop framing | Ethernet, 802.11 (frame) |
| 1 | Physical | Bits on the wire | UTP, fiber (bits) |

Mnemonic ladder: **A-P-S-T-N-D-P** (All People Seem To Need Data Processing) — and the reverse **P-D-N-T-S-P-A** for troubleshooting from the bottom up.

## Exam Focus

- **Layer mapping questions** ("which layer does routing / framing / sessions?") are free points — anchor them to the ladder.
- **Encapsulation order** follows the ladder (see [[Encapsulation]]).
- Troubleshooting follows the model **bottom-up** (phys → link → net → transport) — the classic "layer 1 first" answer.

## Related Terms

- [[TCP/IP Model]], [[Encapsulation]], [[Decapsulation]], [[PDU]], [[Ethernet]]
- Level 03 notes: [[Level 03 - OSI & TCP IP/01. OSI Model]]