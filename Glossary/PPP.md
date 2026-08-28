---
tags: [CCNP, glossary, wan, networking]
aliases: ["PPP", "Point-to-Point Protocol", "PAP", "CHAP", "LCP", "NCP", "MLPPP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# PPP

## Definition

**PPP (Point-to-Point Protocol)** is the classic point-to-point WAN protocol that took over from bare HDLC: it adds **authentication (PAP/CHAP)**, **multilink bonding (MLPPP)**, and structured **negotiation via LCP (link control) + NCP (network control, e.g. IPCP)**. Because it negotiates and authenticates, PPP is the right tool for **dialup, serial T1/E1 links, and as the payload of [[PPPoE]]**.

## How PPP Works

```text
phases: Dead → Establish (LCP: configure, auth options) → Authenticate
        (PAP: plaintext; CHAP: 3-way challenge/handshake) → Network (NCP/IPCP)
LCP options: magic number, MRU, authentication protocol
MLPPP: bundle multiple links into one logical pipe (load balancing)
```

## Exam Focus

- **"What does PPP add over HDLC?" → authentication + negotiation (LCP/NCP) + multilink** — the difference question; HDLC = no auth.
- **PAP vs CHAP**: PAP sends password in cleartext (one-way logins); CHAP uses a 3-way hash challenge — "which authenticates securely?" → CHAP — the classic pair.
- **LCP vs NCP roles**: LCP = link itself; NCP/IPCP = IP over it — the layer split.
- PPP framing/flag (01111110) + FCS — the trivia bits; and today PPP mostly survives inside [[PPPoE]].

## Related Terms

- [[PPPoE]], [[HDLC]], [[WAN]]
- Level 23 notes: [[Level 23 - Enterprise WAN/01. PPP]]