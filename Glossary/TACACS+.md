---
tags: [CCNP, glossary, security, identity]
aliases: ["TACACS+", "TACACS", "Terminal Access Controller Access-Control System"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# TACACS+

## Definition

**TACACS+** is Cisco's AAA protocol for **device administration** — **TCP 49**, and unlike [[RADIUS]] it **separates authentication, authorization, and accounting** into independent exchanges, **encrypts the entire payload**, and supports **per-command authorization** on IOS devices. The admin-login protocol of choice.

## TACACS+ vs RADIUS — the Comparison

| | TACACS+ | RADIUS |
| --- | --- | --- |
| Use | Device admin (CLI) | Network access (dot1x/VPN) |
| Transport | TCP 49 (reliable) | UDP 1812/1813 |
| AAA | Three separate exchanges | Combined (auth+acct) |
| Encryption | Full payload | Only password (RADIUS shared secret) |
| Command auth | Per-command possible | No |

```text
aaa new-model
aaa group server tacacs+ ISE
  server 10.1.99.20
tacacs server ISE key cisco123      ← ENCRYPTS the whole packet
```

## Exam Focus

- **"Which protocol fully encrypts device-admin AAA and allows per-command authorization?" → TACACS+** — the defining contrasts.
- **TCP 49** is the port fact; **per-command authorization** (`aaa authorization commands 15 …`) is the feature nobody else has.
- "Cisco device management should use X; network user access should use Y" — the pairing question answered TACACS+/RADIUS.
- TACACS+ shares the same "AAA" vocabulary: authentication/authorization/accounting each run as separate messages (the "separated services" line).

## Related Terms

- [[AAA]], [[RADIUS]], [[SSH]], [[LDAP]]
- Level 17 notes: [[Level 17 - Security/02. TACACS+]]