---
tags: [CCNP, glossary, network-services, file-transfer]
aliases: ["FTP", "File Transfer Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# FTP

## Definition

**FTP (File Transfer Protocol)** transfers files with **two connections**: a **control channel (TCP 21)** and a **data channel (TCP 20 active / ephemeral passive)**. Authentication is **plaintext** — the classic hardening story. Enterprises use it (and its cousins) to ship **IOS images and configs** to/from devices.

## Active vs Passive

```text
ACTIVE:  client→server TCP 21 (control); server→client connects from 20 to client's ephemeral
PASSIVE: client says PASV; server opens an ephemeral port; client connects to it
         (required through NAT/firewalls — the modern default; NAT blocks active)
```

## Exam Focus

- **"Which protocol uses two TCP connections?" → FTP** — the distinguishing design fact.
- **Passive mode is the NAT/firewall answer** — "active mode fails through PAT" is the scenario.
- Plaintext username/password → prefer **[[HTTPS]]/SFTP/SCP** for secure copies — the security-comparison line.
- Device image management context: `copy ftp://… flash:` — the config-transfer workflow question.

## Related Terms

- [[TFTP]], [[HTTPS]], [[SSH]]
- Level 16 notes: [[Level 16 - Network Services/08. FTP]]