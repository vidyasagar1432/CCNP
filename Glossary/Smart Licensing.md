---
tags: [CCNP, glossary, ios, networking]
aliases: ["Smart Licensing", "CSSM", "Smart Licensing Using Policy", "SLP", "Usage Reporting"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# Smart Licensing

## Definition

**Smart Licensing** replaces PAK-based keys with a **central portal — CSSM (Cisco Software Central)** — that manages entitlements across all devices. Devices **report usage** to CSSM (directly or via an on-prem **Smart License Manager (SSM)**), and **Smart Licensing Using Policy (SLP)** even grants **right-to-use** — devices can run features and report later, simplifying procurement and compliance. Also the model behind classic **licenses** going forward.

## The Flow

```text
devices → (direct / smart transport) → CSSM portal: license pools, usage reports
SLP: right-to-use evaluation → enforcement deferred, reporting mandatory
on-prem: Smart Software Manager (SSM) for air-gapped/closed networks
moves & upgrades: no re-host — entitlement follows the portal account
```

## Exam Focus

- **"Which licensing model reports usage to a portal?" → Smart Licensing (CSSM)** — vs classic PAK — the definition; "what is CSSM?" → the portal.
- **SLP (Smart Licensing Using Policy)**: right-to-use, report-don't-enforce-fiercely — the modern nuance.
- **On-prem option**: Smart Software Manager for isolated environments — the deployment question.
- Migration: traditional license → smart license conversion — the transition scenario.

## Related Terms

- [[Cisco Licensing]], [[IOS XE]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/04. Smart Licensing]]