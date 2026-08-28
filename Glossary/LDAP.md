---
tags: [CCNP, glossary, network-services, identity]
aliases: ["LDAP", "Lightweight Directory Access Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# LDAP

## Definition

**LDAP (Lightweight Directory Access Protocol)** reads and searches a **directory** (users, groups, devices, policies) — **TCP 389** (636 with LDAPS). It's the query interface to the enterprise's identity store (Active Directory speaks it, OpenLDAP is the reference). Authentication (bind) can happen over LDAP — and that's where [[AAA]] and device login get involved.

## How It's Used

```text
structure: DN tree (dc=corp, dc=com → ou=Users → cn=jdoe)
operations: bind (auth), search, compare, modify
Cisco: radius/aaa servers can proxy to LDAP; devices may auth against LDAP
       via RADIUS/TACACS+ translation — LDAP itself is rarely the device dial-up
security: LDAP = plaintext; LDAPS (636) = TLS — always LDAPS for auth/bind
```

## Exam Focus

- **"Which protocol queries a directory of users/groups?" → LDAP** — the definition; port 389.
- **LDAP vs [[AAA]]**: LDAP is an identity/directory service; RADIUS/TACACS+ are the network-auth protocols (Centralized auth stacks on both) — the "which talks to the user database?" architecture question.
- LDAP injection (injection via untrusted search filters) and LDAPS — the security line.
- SAML/OAuth vs LDAP: modern federated identity uses directory + federation — a trend mention for the automation levels.

## Related Terms

- [[AAA]], [[SSH]], [[TACACS]]
- Level 16 notes: [[Level 16 - Network Services/17. LDAP]]