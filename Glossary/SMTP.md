---
tags: [CCNP, glossary, network-services, mail]
aliases: ["SMTP", "Simple Mail Transfer Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# SMTP

## Definition

**SMTP (Simple Mail Transfer Protocol)** delivers email **between mail servers and from clients' submission** — **TCP 25** (server-to-server, classic) and **587** (submission, often with STARTTLS). It's push-based: servers **hand off** messages hop to hop until the destination server's mailbox. Mail clients *read* via [[POP3]]/[[IMAP]].

## The Flow

```text
MUA (Outlook) ── SMTP 587/STARTTLS ──► MSA/MTA
MTA ── SMTP 25 ── MX chain (spooling, retries backoff) ──► destination MTA → mailbox
reading side: client uses POP3/IMAP (NOT SMTP)
```

## Exam Focus

- **"Which protocol moves mail BETWEEN servers?" → SMTP** — vs POP3/IMAP = client *retrieval* — the constant distinction question.
- **Ports**: 25 (relay), 587 (submission), 465 (SMTPS) — plus [[DNS]] **MX records** pick the destination server (the DNS-email link).
- Email security vocabulary: SPF/DKIM/DMARC authenticate senders; STARTTLS encrypts the hop — the modern hardening line.
- Cisco angle: **email alerting** from devices/security appliances (SMTP as an alert channel).

## Related Terms

- [[POP3]], [[IMAP]], [[DNS]]
- Level 16 notes: [[Level 16 - Network Services/14. SMTP]]