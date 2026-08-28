---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["IPv4 Classes", "Class A", "Class B", "Class C", "Class D", "Class E"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# IPv4 Classes

## Definition

Classful addressing splits IPv4 by the **first octet** into classes with fixed network/host splits. Classes **A/B/C** were the original allocation units; **D** is multicast; **E** is reserved. Modern routing ([[CIDR]]) has made classes obsolete — but the ranges are still exam math.

## The Class Table

| Class | First octet | Default mask | Range |
| --- | --- | --- | --- |
| A | 0–127 | /8 | 0.0.0.0–127.255.255.255 |
| B | 128–191 | /16 | 128.0.0.0–191.255.255.255 |
| C | 192–223 | /24 | 192.0.0.0–223.255.255.255 |
| D (multicast) | 224–239 | — | 224.0.0.0–239.255.255.255 |
| E (reserved) | 240–255 | — | 240.0.0.0–255.255.255.255 |

## Exam Focus

- **First-octet classification is the fastest question in the exam** ("which class is 172.16.5.1?" → B).
- Class D = multicast (see [[IPv4 Multicast]]); **loopback 127/8 is inside A**.
- The trick line: "classful vs classless" — classful addressing is dead; every real network uses [[CIDR]].

## Related Terms

- [[IPv4]], [[CIDR]], [[Private IP]], [[IPv4 Multicast]], [[IPv4 Broadcast]]
- Level 05 notes: [[Level 05 - IPv4/04. Classes]]