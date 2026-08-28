---
tags: [CCNP, glossary, eigrp, routing]
aliases: ["EIGRP Authentication"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: EIGRP
created: 2026-08-29
---

# EIGRP Authentication

## Definition

**EIGRP authentication** verifies that EIGRP packets (hello, update, query, reply) come from a neighbor that shares the configured key. Only **HMAC-MD5** (classic) and **HMAC-SHA-256** (named mode) are supported.

## How It Works

```text
Router (key chain "CCNP-KEYS": key 1 md5 ...)
    │  every packet carries a keyed MAC + key ID
    ▼
Neighbor validates with the same key ID
Mismatch → packets dropped → adjacency never forms / drops silently
```

- Keys are stored in **key chains**; multiple keys with lifetimes allow **rolling (graceful) key change**.
- Authentication protects against route injection/redirection attacks — not against traffic sniffing ([[OSPF Authentication]] is the same idea).
- Per-neighbor or per-address-family configuration (classic `ip authentication mode eigrp <as> md5`; named mode under `af-interface`).

## Exam Focus

- **Both sides need identical key + key-ID**; a mismatch produces silent drops — neighbors stay in "Pending"/down without errors.
- **Key-chain lifetimes** enable zero-downtime key rotation — a favorite scenario question.
- EIGRP MD5 is a MAC over the packet, unlike plaintext passwords.

## Related Terms

- [[EIGRP]], [[Named Mode EIGRP]], [[OSPF Authentication]] (contrast), [[OSPFv3]] (IPsec-only auth)
- Level 11 notes: [[Level 11 - EIGRP/08. Authentication]]