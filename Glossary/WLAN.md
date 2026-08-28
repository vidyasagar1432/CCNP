---
tags: [CCNP, glossary, wireless, networking]
aliases: ["WLAN", "Wireless LAN", "Wi-Fi", "BSS", "Basic Service Set"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# WLAN

## Definition

A **WLAN (Wireless LAN)** is the "last 100 meters" made wireless: clients associate over **RF** to an **AP (access point)** instead of plugging into a switch port. The atomic unit is the **BSS (Basic Service Set)** — one AP radio + its clients, identified by [[BSSID]] and advertised under an [[SSID]]. WLANs ride on the [[802.11]] standard family and can be **autonomous** (standalone AP) or **centralized** (APs managed by a [[WLC]]).

## The Structure

```text
BSS = AP radio + associated clients (the cell)
SSID = the name humans choose / see
ESS = extended service set: several APs, one SSID = roaming domain
frames travel: client ↔ AP (data), AP ↔ WLC (CAPWAP), then into the wired LAN
```

## Exam Focus

- **"What is the fundamental component of a WLAN?" → BSS** — the atomic unit; BSSID = its identity, SSID = its name — the tri-set question.
- **Autonomous vs controller-based**: standalone (fat) AP vs lightweight AP + [[WLC]] — the deployment model choice.
- WLAN = the L1/L2 wireless domain; it must **hand off to the wired infrastructure** — the integration boundary question.
- Exam "BSS/ESS/IBSS": IBSS = ad-hoc (no AP) — the variant not to forget.

## Related Terms

- [[802.11]], [[SSID]], [[BSSID]], [[WLC]], [[CAPWAP]]
- Level 22 notes: [[Level 22 - Wireless/01. WLAN]]