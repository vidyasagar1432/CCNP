---
tags: [CCNP, glossary, nat]
aliases: ["Application Level Gateway", "Application Layer Gateway", "ALG"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT ALG

## Definition

A **NAT ALG (Application-Level Gateway)** makes address translation work for protocols that carry IP addresses or ports **inside their payload** — where plain address rewriting would break the application because the embedded address stays untranslated.

## Problem It Solves

Some applications embed addressing information beyond the packet header:

- **FTP** — active mode embeds the client's IP in PORT commands; the server connects back to it
- **SIP** — signaling messages carry the media (RTP) address in SDP
- Protocols that advertise their "real" address that the peer then uses

Ordinary NAT rewrites headers only; the embedded address would still reveal the untranslated value, so the peer connects to the wrong address. The ALG rewrites the payload too.

## How It Works

```text
Application message carries 10.0.0.10:21 (embedded)
                 ↓  ALG inspects + rewrites payload
Application message carries 203.0.113.10:21
```

## Exam Focus

- **Do NOT assume every app failure behind NAT is an ALG problem.** IOS/PIX inspection behavior varies by platform, OS version, and design — verify NAT state, ports, and routing first.
- **Do NOT memorize "SIP/RTP requires ALG."** Modern platforms handle or mitigate this differently (STUN, NAT traversal, inspection policy).
- FTP active vs passive mode changes whether the control/data connection pattern creates a NAT problem.

## Related Terms

- [[NAT]], [[NAT Translation Table]], [[PAT]]
- Level 15 notes: [[Level 15 - NAT/06. Troubleshooting]]