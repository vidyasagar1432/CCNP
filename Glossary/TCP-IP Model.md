---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["TCP/IP Model", "Internet Model", "DoD Model", "Internet Protocol Suite"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSI & TCP/IP
created: 2026-08-29
---

# TCP/IP Model

## Definition

The **TCP/IP model** describes the protocol stack actually used on the Internet. It has **four layers** (some texts say five) that map onto the OSI seven and reflect how real protocols ([[IPv4]], [[IPv6]], TCP, UDP, HTTP) structure communication.

## Four-Layer Map

| TCP/IP layer | OSI equivalents | Core protocols |
| --- | --- | --- |
| Application | 7+6+5 | HTTP, DNS, DHCP, TLS |
| Transport | 4 | TCP, UDP |
| Internet | 3 | IP, ICMP, routing protocols |
| Network Access (Link) | 2+1 | Ethernet, Wi-Fi, PPP |

## Exam Focus

- **The mapping question** ("which OSI layers collapse into the TCP/IP application layer?") is guaranteed — remember 7+6+5 → Application.
- The **Internet layer = OSI Network (3)**; the **Link layer spans 2+1**.
- The "Internet" in the name means inter-networking (routing between networks), not "the World Wide Web."

## Related Terms

- [[OSI Model]], [[Encapsulation]], [[PDU]], [[IPv4]], [[IPv6]]
- Level 03 notes: [[Level 03 - OSI & TCP IP/02. TCP IP Model]]