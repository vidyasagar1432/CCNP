---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Client-Server Model", "Client Server Architecture"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Client-Server

## Definition

The **client-server model** centralizes services on dedicated **servers** that **clients request work from**. Servers provide (web, mail, DNS, DHCP, files, databases); clients consume — a clear role separation that makes services manageable, secure, and scalable.

## How It Works

```text
client ── request ──► server
client ◄── response ── server

- server: waits for connections, one-to-many, higher-duty hardware
- client: initiates the transaction, usually one-to-one with the service
```

| Trait | Server | Client |
| --- | --- | --- |
| Role | Provide service | Request service |
| Relationship | One service, many clients | One user-centric endpoint at a time |
| Typical state | Rarely reboots, hardened | Commodity device |

## Exam Focus

- **Client–server vs [[Peer-to-Peer]]** distinctions: centralized vs decentralized, one-to-many vs equal roles, where the "service" lives.
- The exam tests *why* enterprises choose client-server: centralized policy, backup, security, and naming/DHCP all at the server.
- Everything DNS, DHCP, AAA, and NTP in later levels is an application of this model.

## Related Terms

- [[Peer-to-Peer]], [[End Device]], [[LAN]], [[Enterprise Network Architecture]]
- Level 00 notes: [[Level 00 - Networking Basics/03. Client-Server]]