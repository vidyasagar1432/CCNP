---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["Public IP Address", "Global IP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# Public IP

## Definition

A **public (global) IP address** is uniquely routable across the Internet — no two devices worldwide can share the same one simultaneously. Public addresses are assigned by **IANA → RIRs (ARIN, RIPE, APNIC…) → ISPs → you**.

## How It Works

```text
public IP ──► globally unique, advertised across the Internet
private IP ──► reusable inside your network, NOT routable publicly ([[Private IP]])

shortage reality: IPv4 exhaustion → most enterprise edges use NAT
(see [[NAT]]) to map many private → few public addresses.
```

## Exam Focus

- **"Which addresses are routable on the Internet?"** → public; private/loopback/multicast are not.
- NAT exists *because* public IPv4 is scarce and private space is reusable.
- Expect "is this public or private?" identification questions — memorize the [[Private IP]] ranges to spot the difference fast.

## Related Terms

- [[Private IP]], [[IPv4]], [[NAT]], [[APIPA]]
- Level 05 notes: [[Level 05 - IPv4/05. Public IP]]