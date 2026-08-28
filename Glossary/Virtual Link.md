---
tags: [CCNP, glossary, ospf, routing]
aliases: ["Virtual Link", "OSPF Virtual Link"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# Virtual Link

## Definition

An **OSPF virtual link** is a logical, point-to-point adjacency that connects a disconnected area to the backbone — or repairs a non-contiguous Area 0 — by tunneling OSPF traffic through a **transit area**.

## How It Works

```text
        transit area (e.g. Area 1)
   ABR-A ─────────────────────── ABR-B
   (Area 1 hop)                  (Area 1 hop)
         │ virtual link           │
   Area 2 sees Area 0 through the virtual link
```

Requirements:

- The virtual link is configured on **two ABRs** (transit area must be the same).
- It is **not a real interface** — it is a logical adjacency; OSPF packets flow through the transit area as ordinary Area-1 traffic.
- The virtual link appears as a **point-to-point** link in SPF (`show ip ospf virtual-links`).

## When to Use (and Avoid)

| Situation | Virtual link? |
| --- | --- |
| Area 2 has no physical path to Area 0 | Yes (via a transit area) |
| Backbone (Area 0) split in two | Yes (repairs contiguity) |
| Any ordinary area design | No — prefer fixing physical design |

## Exam Focus

- Virtual links are **last-resort design tools**, not a normal architecture; a broken backbone "must" be repaired properly.
- **Stub areas and NSSAs cannot be transit areas** for virtual links, and virtual links cannot transit a stub.
- The endpoints must know each other's [[OSPF Router ID]] — reaching them via intra-area routes only.

## Related Terms

- [[OSPF Area]], [[ABR]], [[OSPF Router ID]], [[OSPF]]
- Level 10 notes: [[Level 10 - OSPF/12. Virtual Links]]