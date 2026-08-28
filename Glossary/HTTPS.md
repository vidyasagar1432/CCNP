---
tags: [CCNP, glossary, network-services, web, security]
aliases: ["HTTPS", "HTTP Secure", "TLS", "SSL"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# HTTPS

## Definition

**HTTPS (HTTP Secure)** is HTTP encrypted with **TLS** — **TCP 443**. It protects confidentiality (content), integrity, and authenticity (server certificate verified against a [[DNS|DNS]]-resolved name). In network practice: secure web UI, RESTCONF/NETCONF transports, and the traffic you must NOT decrypt blindly.

## The Handshake in One Line

```text
client hello (ciphers) ⇄ server hello + certificate + key exchange
→ session keys → all subsequent HTTP inside TLS records
(trust = the certificate chain: leaf → CA → trusted root)
```

## Exam Focus

- **"Port 443 + TLS = ?" → HTTPS** — versus plain HTTP 80; the upgrade question.
- **PKI basics**: certificates, CAs, validity — expired device cert = broken management UI ([[NTP]] matters again for cert times!).
- Cisco: `ip http secure-server`, `crypto pki` for the device's own cert — the management-plane hardening set.
- TLS pinning/inspection: proxies that MITM HTTPS need installed trust anchors — the "why does interception break clients?" scenario.

## Related Terms

- [[HTTP]], [[SSH]], [[NTP]], [[Certificate]]
- Level 16 notes: [[Level 16 - Network Services/11. HTTPS]]