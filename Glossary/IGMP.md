---
tags: [CCNP, glossary, multicast, networking]
aliases: ["IGMP", "Internet Group Management Protocol", "IGMPv3", "IGMP Snooping"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Multicast
created: 2026-08-29
---

# IGMP

## Definition

**IGMP (Internet Group Management Protocol)** is the **host-to-router** membership protocol: receivers tell the local router which **multicast groups** they want to join — the entry ticket to multicast delivery. Versions: **v1/v2** (any-source, leave messages), **v3** (source-specific joins → enables [[Source-Specific Multicast|SSM]]). Routers query, hosts report.

## Membership Lifecycle

```text
host joins 239.1.1.1 → sends IGMP Membership Report (224.0.0.22 v3)
router: queries periodically (general query), hosts answer with reports
host leaves (v2 leave) → router sends group-specific query → no reply = prune
snooping tie-in: switches listen to IGMP to prune ports ([[IGMP Snooping]])
```

## Exam Focus

- **"Which protocol manages receiver membership in multicast groups?" → IGMP** — hosts↔first-hop-router scope.
- **v3's superpower**: `(S,G)` joins — a host can request **specific sources**, which is what makes SSM work — the version question.
- IGMP vs [[PIM]]: IGMP = host↔router membership; PIM = router↔router delivery — the scope separation.
- Query vs report: who asks and who answers — the roles question.

## Related Terms

- [[IGMP Snooping]], [[PIM]], [[Source-Specific Multicast]], [[IPv4 Multicast]]
- Level 19 notes: [[Level 19 - Multicast/01. IGMP]]