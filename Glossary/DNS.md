---
tags: [CCNP, glossary, network-services, networking]
aliases: ["DNS", "Domain Name System", "DNS Resolver", "A Record"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# DNS

## Definition

**DNS (Domain Name System)** maps **names ↔ IP addresses** (A/AAAA records), and much more (MX, CNAME, PTR). It's a **hierarchical, distributed database**: root → TLD → authoritative servers, with **resolvers caching** answers. UDP **53** (TCP 53 for large transfers/zone transfers).

## The Resolution Walk

```text
host → local resolver (stub) → recursive query … root → .com → example.com auth
answer flows back; resolver caches (TTL!) → next query is instant
records: A (v4), AAAA (v6), CNAME (alias), MX (mail), PTR (reverse), SRV (service)
```

## Security (exam-gold)

- **DNS poisoning** — corrupt an answer; **DNS tunneling** — exfil over queries; **DNSSEC** — signed answers (RRSIG/DS) stop forgery.
- **Anycast** DNS = the modern resolver design ([[Anycast]] tie-in, names like 8.8.8.8/1.1.1.1).
- Split-horizon / internal vs external views — the enterprise design question.

## Exam Focus

- **Ports: UDP 53 primary, TCP 53 for zones/overflow** — a near-guaranteed trivia point.
- **"Which record maps a name to IPv6?" → AAAA; "mail server?" → MX; "alias?" → CNAME.**
- Failure mode: correct IP but name wrong → DNS (not routing) — the troubleshooting "who do you check?" classic.
- `ip name-server` on routers; `ip domain lookup` gates resolution for admin commands.

## Related Terms

- [[Anycast]], [[HTTPS]], [[DHCP]]
- Level 16 notes: [[Level 16 - Network Services/04. DNS]]