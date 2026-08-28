---
tags: [CCNP, glossary, wireless, networking]
aliases: ["RF", "Radio Frequency", "RSSI", "SNR", "Signal to Noise Ratio", "Attenuation", "dBm", "dBi"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# RF

## Definition

**RF (radio frequency)** physics decides whether Wi-Fi actually works: **signal strength (RSSI, in dBm)**, **signal-to-noise ratio (SNR, in dB)**, **attenuation** (walls, distance), **interference** (non-Wi-Fi noise), **multipath**, and **antenna gain (dBi)**. Design questions are RF questions: **-67 dBm** = "good" for data; **-65 dBm or better** = voice grade.

## The Numbers That Matter

```text
RSSI: -50 dBm excellent | -67 dBm good | -75 dBm marginal | -85 dBm unusable
SNR:  >25 dB great | 20–25 good | <10 bad (noise floor wins)
dBm = absolute power (mW ratio), dBi = antenna gain, dB = relative change
3 dB ≈ double/half power — the quick mental math
```

## Exam Focus

- **The dBm thresholds**: -67 good data, -65 voice — the design-limit question.
- **RSSI vs SNR**: strength vs cleanliness — "weak signal OR noisy signal, which is worse?" nuance.
- **dBd vs dBi, 3 dB rule**: doubling/halving — the unit conversions.
- Attenuation + interference are the two RF killers in troubleshooting — the "why does Wi-Fi drop at the conference room?" scenario.

## Related Terms

- [[Channels]], [[802.11]], [[WLAN]]
- Level 22 notes: [[Level 22 - Wireless/06. RF]]