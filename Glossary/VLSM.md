---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["VLSM", "Variable Length Subnet Mask"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# VLSM

## Definition

**VLSM (Variable Length Subnet Masking)** uses **different prefix lengths inside one network** so each subnet gets exactly the size it needs (a /30 for a link, a /26 for a floor) — the address-efficient opposite of [[FLSM]]'s one-size-fits-all.

## Subnetting a /24 with VLSM

```text
waste with FLSM: 4 × /26 → 254 usable for 2 hosts per link (202 wasted)
VLSM /24:
  ┌─ 192.168.1.0/26   → 62 hosts    (LAN A)
  ├─ 192.168.1.64/27  → 30 hosts    (LAN B)
  ├─ 192.168.1.96/28  → 14 hosts    (LAN C)
  └─ 192.168.1.112/30 → 2 hosts     (router-router link)
  └─ 192.168.1.116/30 → 2 hosts     (2nd link)
  …remaining space for growth
```

## Exam Focus

- **"Which technique assigns different-length masks to maximize efficiency?"** → VLSM.
- VLSM requires a **classless protocol** — EIGRP and OSPF support it natively; RIPv1 does not (classful).
- Subnetting arithmetic: block size (`256 - mask octet`) gives the range; subnets fall on **multiples of the block**.

## Related Terms

- [[CIDR]], [[FLSM]], [[IPv4]], [[Summarization]]
- Level 05 notes: [[Level 05 - IPv4/12. VLSM]]