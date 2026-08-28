---
tags: [CCNP, glossary, wireless, networking]
aliases: ["WPA3", "Wi-Fi Protected Access 3", "SAE", "Simultaneous Authentication of Equals", "OWE", "Forward Secrecy"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# WPA3

## Definition

**WPA3** fixes WPA2's cracks: **SAE (Simultaneous Authentication of Equals)** replaces the PSK four-way handshake — the password never transits in a crackable form (**forward secrecy**, resistant to **offline dictionary attacks**), **OWE** (Opportunistic Wireless Encryption) gives open networks real encryption, and **192-bit enterprise mode** adds stronger crypto. Same AES-CCMP/AES-GCMP underneath.

## What Changed

```text
WPA2-PSK  →  WPA3-SAE: Dragonfly handshake, each session unique, 
             no offline guess, forward secrecy
WPA2 open →  OWE (Wi-Fi "Enhanced Open"): encrypts without a password
enterprise →  WPA3-Enterprise 192-bit (CNSA suite)
```
Note: SAE **doesn't fix weak passwords** — it removes the offline-attack vector (online guessing still possible).

## Exam Focus

- **"What replaces PSK in WPA3?" → SAE** — the flagship answer; "why better?" → no offline dictionary, forward secrecy.
- **OWE**: "secured open network" — the guest/hotspot answer.
- **WPA3 backward compatibility**: transition mode with WPA2 devices — the mixed-deployment nuance.
- Same underlying cipher family (AES) — hardening is in the **handshake**, not the cipher — the "what actually changed?" clarity.

## Related Terms

- [[WPA2]], [[802.1X]], [[AAA]]
- Level 22 notes: [[Level 22 - Wireless/12. WPA3]]