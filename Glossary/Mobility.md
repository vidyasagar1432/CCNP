---
tags: [CCNP, glossary, wireless, networking]
aliases: ["Wireless Mobility", "Mobility Group", "Mobility Anchor", "Guest Anchor", "Inter-WLC Roaming"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# Mobility

## Definition

**Wireless mobility** is the WLC machinery that keeps a client's **session alive while moving across APs and even across WLCs**. WLCs join a **mobility group** (sharing mobility keys); when a client roams to another WLC, the **anchor WLC** holds the client's state and forwards traffic so the session (DHCP, auth, VPN) never breaks. Related concept: **guest anchoring** keeps guest traffic tunneled back to a designated anchor.

## How It Works

```text
client roams AP1(WLC1) → AP2(WLC2)
WLC2 finds the client's mobility info (Mobility Message Exchange) →
  WLC1 becomes anchor: it keeps the client's DHCP/security state
  traffic: client → WLC2 → WLC1 (anchor) → network (or local + anchor just tracks)
mobility group: WLCs that trust each other (shared secret, same group name)
```

## Exam Focus

- **"What keeps the session alive on inter-WLC roaming?" → mobility/anchor** — the definition; the anchor WLC = "home" of the session.
- **Mobility group**: WLCs mutually trusted (key exchange) — "how do WLCs know each other?" answer.
- **Guest anchoring**: guest traffic tunneled to a chosen anchor (often DMZ) — the security-mandated pattern.
- Layer 3 roaming vs Layer 2 roaming wrap into mobility design — the integration with [[Roaming]].

## Related Terms

- [[Roaming]], [[WLC]], [[CAPWAP]], [[DHCP]]
- Level 22 notes: [[Level 22 - Wireless/09. Mobility]]