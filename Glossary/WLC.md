---
tags: [CCNP, glossary, wireless, networking]
aliases: ["WLC", "Wireless LAN Controller", "Wireless Controller", "RRM", "AP Join"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# WLC

## Definition

The **WLC (Wireless LAN Controller)** is the **brain of the centralized WLAN**: it configures and monitors lightweight **APs** (via [[CAPWAP]]), runs **RRM (Radio Resource Management)** for automatic channel/power tuning, authenticates clients, and coordinates **[[Roaming]]/[[Mobility]]**. The AP→WLC split: **APs = radios + some forwarding; WLC = config, policy, security, RF intelligence**.

## The Split of Duties

```text
AP (lightweight): RF, beacons, some local switching (FlexConnect) — "thin"
WLC: config push, CAPWAP join, client auth (802.1X), RRM (channel/power),
     mobility anchoring, guest tunneling — "fat brain, thin arms"
AP boots → discovers WLC (DNS/option 43/broadcast) → joins via CAPWAP
```

## Exam Focus

- **"What does the WLC do?" → centralized config/security/RRM/mobility** — the role list; APs are radio-extensions.
- **AP discovery**: DHCP option 43, DNS, or local — "how does an AP find its WLC?" question.
- **RRM**: automatic channel + power assignment — the "what tunes RF automatically?" answer.
- **Controller redundancy**: primary/secondary/tertiary lists, AP failover — the HA scenario.

## Related Terms

- [[CAPWAP]], [[WLAN]], [[SSID]], [[Mobility]], [[Roaming]]
- Level 22 notes: [[Level 22 - Wireless/07. WLC]]