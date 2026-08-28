---
tags: [CCNP, glossary, wireless, networking]
aliases: ["WPA2", "Wi-Fi Protected Access 2", "CCMP", "AES-CCMP", "PSK", "802.1X", "TKIP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# WPA2

## Definition

**WPA2** is the long-standing Wi-Fi security standard: **AES-CCMP** encrypts data (the **TKIP** of WPA1 is gone), and authentication is **802.1X** in enterprise mode or **PSK** (pre-shared key) for personal. WPA2-PSK's weakness: **brute-forceable passphrases** in the four-way handshake — the reason [[WPA3]] exists.

## The Stack

```text
encryption: AES-CCMP (counter mode + CBC-MAC) — the "what encrypts in WPA2?" answer
auth modes: personal (PSK ≥ 8 chars) vs enterprise (802.1X → RADIUS backend)
four-way handshake: PMK → PTK → GTK — where the PSK gets cracked
```

## Exam Focus

- **"Which cipher does WPA2 mandate?" → AES-CCMP** — the definitive answer (TKIP = legacy-only).
- **WPA2-Personal vs Enterprise**: PSK vs 802.1X/RADIUS — the mode-choice question (corporate = enterprise).
- **The four-way handshake** and PMK derivation from PSK — the attack-surface fact (offline dictionary).
- Weakness framing: PSK = shared password everyone knows — "what's the piggyback risk?" scenario.

## Related Terms

- [[WPA3]], [[AAA]], [[RADIUS]], [[802.1X]]
- Level 22 notes: [[Level 22 - Wireless/11. WPA2]]