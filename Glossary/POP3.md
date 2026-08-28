---
tags: [CCNP, glossary, network-services, mail]
aliases: ["POP3", "Post Office Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# POP3

## Definition

**POP3 (Post Office Protocol v3)** lets a mail client **download messages to the device** and (traditionally) remove them from the server — **TCP 110** (993 with TLS). It's the "offline mailbox" model: one device, simple, minimal server storage.

## POP3 vs IMAP — the Decision

| | POP3 | [[IMAP]] |
| --- | --- | --- |
| Model | Download & (usually) delete | Sync & keep on server |
| Multi-device | Poor (per-device mail) | Native (folders everywhere) |
| Server storage | Minimal | Central |
| Port | 110 / 993 (SSL) | 143 / 993 |

## Exam Focus

- **"Which protocol downloads mail to a single device and empties the server?" → POP3** — contrast with IMAP's keep-synced model.
- Ports: POP3 110/SSL 993 vs IMAP 143/SSL 993 vs [[SMTP]] 25/587 — build the four-port matrix.
- Mail path clarity: **SMTP sends, POP3/IMAP reads** — "which protocol retrieves mail?" is the stock question.

## Related Terms

- [[IMAP]], [[SMTP]], [[DNS]]
- Level 16 notes: [[Level 16 - Network Services/15. POP3]]