---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["Private IP Address", "RFC 1918", "Private Addressing"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# Private IP

## Definition

**Private (RFC 1918) addresses** are reserved ranges that anyone may reuse inside their own networks — they are **never routed on the public Internet**. Their purpose: give every internal device a stable address while conserving global space.

## The Three Ranges (memorize)

| Range | CIDR | Typical use |
| --- | --- | --- |
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | Large orgs / DCs |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | Enterprise (note: only 172.16–31!) |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | SMB / home |

## Exam Focus

- **Spot-the-trap**: "172.32.x.x is private" → NO: RFC 1918 stops at **172.31.255.255**.
- Private space appears on almost every internal interface; the Internet edge translates it via **[[NAT]]** (PAT in practice).
- Duplicate private ranges across sites collide when VPNs connect them without NAT — a real-world design scenario.

## Related Terms

- [[Public IP]], [[IPv4]], [[NAT]], [[APIPA]]
- Level 05 notes: [[Level 05 - IPv4/06. Private IP]]