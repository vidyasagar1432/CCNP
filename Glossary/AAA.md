---
tags: [CCNP, glossary, security, identity]
aliases: ["AAA", "Authentication Authorization Accounting"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# AAA

## Definition

**AAA** is the security framework for access control, standing for:
- **Authentication** — *who* (identity: local, **[[TACACS+]]**/[[RADIUS]], certs)
- **Authorization** — *what they may do* (permission levels, command sets)
- **Accounting** — *what they did* (logs: logins, commands, sessions)

It's the backbone of enterprise device and network access: login, enable, dot1x, VPNs, and per-command control all ride on AAA.

## The Stack

```text
aaa new-model                       ← activates AAA on IOS
aaa authentication login default group tacacs+ local
aaa authorization exec default group tacacs+
aaa accounting exec default start-stop group tacacs+
fallback chains: group server → local → none   (resilience when the server dies)
```

## Exam Focus

- **"Which framework covers identify, permit, and audit?" → AAA** — the three-part definition is the whole question.
- **AAA ≠ an app**: it's the model; TACACS+/RADIUS are the transports — pair them per use case (device admin → TACACS+, network access → RADIUS).
- **Local fallback** (`local`) is the design answer for server-outage resilience — "which keyword keeps login working when AAA server is down?"
- Accounting = the logs — audit/compliance scenario questions point to `aaa accounting`.

## Related Terms

- [[TACACS+]], [[RADIUS]], [[SSH]], [[LDAP]], [[Port Security]]
- Level 17 notes: [[Level 17 - Security/01. AAA]]