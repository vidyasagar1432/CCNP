---
tags: [CCNP, glossary, wireless, networking]
aliases: ["BSSID", "Basic Service Set Identifier", "BSS", "ESS"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# BSSID

## Definition

The **BSSID** is the **MAC address of an AP's radio** — the hardware identity that actually makes a wireless cell work. Each **BSS** = one radio + its clients; the **BSSID** names that cell to the 802.11 machinery. **ESS (Extended Service Set)** = several BSSes sharing an [[SSID]], which is what enables [[Roaming]]. BSSID = who you really talk to; SSID = the pretty name.

## The Identity Stack

```text
SSID  = "CORP" — what users pick
BSSID = 00:1a:2b:3c:4d:5e — the radio they associate with
one radio can carry multiple BSSIDs if it hosts multiple SSIDs (per-SSID cells)
frames are addressed TO the BSSID; the SSID is just carried in management frames
```

## Exam Focus

- **"Which identifier is the AP radio's MAC?" → BSSID** — vs SSID (name) — the naming question.
- **BSS vs ESS**: one cell vs many cells, one SSID — the scale definitions.
- **Multiple BSSIDs per radio**: one per SSID per radio — the "how many BSSIDs on an AP broadcasting 3 SSIDs?" scenario.
- "BSSID as destination" — 802.11 data frames go to the BSSID — the frame-addressing fact.

## Related Terms

- [[SSID]], [[WLAN]], [[Roaming]], [[802.11]]
- Level 22 notes: [[Level 22 - Wireless/04. BSSID]]