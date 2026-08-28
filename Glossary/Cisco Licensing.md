---
tags: [CCNP, glossary, ios, networking]
aliases: ["Cisco Licensing", "Licensing", "License", "PAK", "Evaluation License", "Technology Package"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# Cisco Licensing

## Definition

**Licensing** gates **feature entitlements** on IOS XE: which technology packages a device may run. The **legacy model** used **PAK keys + product activation keys / license files** (EULA-based, per-box, manual); the modern model is **[[Smart Licensing]]** with usage reporting to a central portal. Packages on platforms: e.g. **network-advantage/network-essential** on Catalyst 9000, or **technology packages** (ipbase, security, data) on ISR routers.

## Legacy vs Smart

| Aspect | Classic licensing | Smart Licensing |
| --- | --- | --- |
| Entitlement | PAK → license file | Right-to-use via portal (CSSM) |
| Reporting | None (offline) | Usage reporting (consumption) |
| Moves/upgrades | Manual re-host | Automatic pool-based |
| Operations | Painful at scale | Central, portal-based |

## Exam Focus

- **"What does licensing control on IOS XE?" → feature entitlements/technology packages** — the definition.
- **PAK file → activate → license file** — the legacy flow; "what replaced PAKs?" → Smart Licensing — the transition question.
- **Package names**: network-advantage vs network-essentials; IP Base/Security/Data services on ISRs — the recognition.
- Evaluation licenses: 90-day trial right-to-use — the "try before license" fact.

## Related Terms

- [[Smart Licensing]], [[IOS XE]], [[Cisco IOS]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/03. Licensing]]