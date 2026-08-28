---
tags: [CCNP, glossary, network-services, mail]
aliases: ["IMAP", "Internet Message Access Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# IMAP

## Definition

**IMAP (Internet Message Access Protocol)** keeps mail **on the server, synced across devices** — **TCP 143** (993 with TLS). Clients see the server's folders/state (read, flagged, moved) — the "everything everywhere" mailbox model that replaced POP3 for multi-device users.

## IMAP Statefulness

```text
client logs in → server mailstore is THE source of truth
actions sync: mark-read, move, search — visible on every device
offline clients cache, then re-sync on reconnect
vs POP3: nothing is downloaded-away; server holds the copy
```

## Exam Focus

- **"Which protocol offers multi-device synchronized mail?" → IMAP** — the defining contrast against [[POP3]].
- Ports: 143 (plain) / 993 (TLS) — both POP3-SSL and IMAP-SSL use 993 is a classic trick (POP3S 995 actually — many sources; the exam-safe table is 110/143/995/993).
- Mail tri-angle: [[SMTP]] moves mail between servers/from clients; IMAP is the *read* protocol — "which retrieves?" never SMTP.

## Related Terms

- [[POP3]], [[SMTP]], [[DNS]]
- Level 16 notes: [[Level 16 - Network Services/16. IMAP]]