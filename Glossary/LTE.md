---
tags: [CCNP, glossary, wan, networking]
aliases: ["LTE", "5G", "Cellular WAN", "Cellular Interface", "APN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# LTE

## Definition

**LTE/5G cellular** is a **wireless WAN transport**: a router with a **cellular/modem interface + SIM + APN** gets IP over the mobile network. Perfect as **primary WAN in rural areas**, as **backup/failover** at any site, or for **roaming/merchant sites**. It's quick to deploy, but re-introduces **RF variables**: coverage, contention, carrier NAT, and dynamic addressing.

## The Setup

```text
router: interface Cellular0/1/0 → dialer/SIM → APN (carrier profile) → IP
    (usually DHCP-like or static from carrier; often CGNAT'd)
use cases: failover (ip route with track), rural primary, temporary sites
Cisco SD-WAN: LTE as an underlay transport alongside MPLS/broadband
```

## Exam Focus

- **"Which WAN option needs SIM + APN?" → LTE** — the cellular specifics; "when choose it?" → rural, backup, pop-up sites — the scenario answers.
- **LTE as failover**: tracked static route / SD-WAN tie — the design pairing.
- **Carrier-grade NAT + dynamic IP** hurdles → VPN/NAT traversal needed — the troubleshooting angle.
- 5G/4G version questions are the freshness bit — "latest radios are 5G-ready" mention.

## Related Terms

- [[Broadband]], [[SD-WAN]], [[NAT]]
- Level 23 notes: [[Level 23 - Enterprise WAN/06. LTE]]