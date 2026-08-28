---
tags: [CCNP, glossary, wireless, networking]
aliases: ["CAPWAP", "Control And Provisioning of Wireless Access Points", "LWAPP", "AP Mode", "FlexConnect"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# CAPWAP

## Definition

**CAPWAP (Control And Provisioning of Wireless Access Points)** is the **standard tunnel between AP and [[WLC]]** (RFC 5415, replacing Cisco's LWAPP). It runs **two UDP tunnels**: **control** (port 5246 — config, stats, keepalives) and **data** (port 5247 — client traffic). Split by **AP mode**: **Local mode** = data tunneled to the WLC (central switching); **FlexConnect** = data switched locally at the AP (for branches).

## The Tunnels

```text
UDP 5246: control — AP↔WLC config, monitoring, keys (DTLS-encrypted by default)
UDP 5247: data — client frames, when the AP is in Local mode
modes: Local (centralized) | FlexConnect (local switching, WLC still owns config)
```

## Exam Focus

- **"Which protocol is the AP↔WLC tunnel?" → CAPWAP** — the definition; successor to LWAPP — the history fact.
- **Control vs data port**: 5246 vs 5247 — the port-pair question.
- **Local vs FlexConnect**: where does client traffic get switched? → WLC vs AP — the mode decision (branch = FlexConnect).
- CAPWAP control should be encrypted (DTLS) — the security mention.

## Related Terms

- [[WLC]], [[WLAN]], [[Mobility]]
- Level 22 notes: [[Level 22 - Wireless/08. CAPWAP]]