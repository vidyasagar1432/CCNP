---
tags: [CCNP, glossary, switching, networking]
aliases: ["Proxy ARP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Proxy ARP

## Definition

**Proxy ARP** is a router behavior where the router **answers an ARP request on behalf of another device** reachable through it — so a host can reach off-subnet destinations **without a default gateway configured**.

## How It Works

```text
host A (10.1.1.1, no gateway) wants 10.1.2.1 (different subnet)
  A broadcasts "who has 10.1.2.1?"
  router (10.1.1.254) knows 10.1.2.1 via routing →
     replies "10.1.2.1 is at <router MAC>"
  A sends frames to the router's MAC → router routes them onward
```

- Classic workaround: diskless/dumb clients, devices with no gateway config.
- **Disabled by default on modern Cisco interfaces** — its absence breaks "no-gateway" trickery (and it degrades routing behavior if left on).

## Exam Focus

- **"Which feature lets a host without a default gateway reach other subnets?"** → proxy ARP.
- It answers **on behalf of another host**, unlike normal [[ARP]] (owner answers itself) — contrast question.
- Security note: proxy ARP can mask misconfigurations and disrupt modern multi-gateway designs (like FHRP); disabling is the modern best practice.

## Related Terms

- [[ARP]], [[Gratuitous ARP]], [[Default Gateway]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/12. Proxy ARP]]