---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["CIDR", "Classless Inter-Domain Routing", "VLSM notation", "Prefix Length"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# CIDR

## Definition

**CIDR (Classless Inter-Domain Routing)** replaced classful addressing by expressing any address as **IP/prefix-length** (`/n`, 0–32). It decouples subnet boundaries from class octets — enabling **any-size networks, [[VLSM]],** and **route summarization** (just add the /n to aggregate).

## Why /n is the Whole Game

```text
/24 = 255.255.255.0  → 256 addresses, 254 usable
/30 = 255.255.255.252 → exactly 2 usable (point-to-point links)
/32 = host route        (loopback, default route 0.0.0.0/0 = "/0")
prefix length = number of 1-bits in the mask (left to right)
```

| Prefix | Block size | Usable |
| --- | --- | --- |
| /24 | 256 | 254 |
| /25 | 128 | 126 |
| /26 | 64 | 62 |
| /27 | 32 | 30 |
| /28 | 16 | 14 |
| /30 | 4 | 2 |

## Exam Focus

- **Converting /n ↔ dotted mask is core speed math** — know the /8–/30 block sizes cold.
- **"What is the CIDR notation for 255.255.255.240?"** → /28 (block 16). Instant-answer questions.
- Classless means routing no longer assumes class boundaries — **longest-prefix match (LPM)** decides instead.

## Related Terms

- [[IPv4]], [[VLSM]], [[FLSM]], [[Summarization]], [[Supernetting]]
- Level 05 notes: [[Level 05 - IPv4/11. CIDR]]