---
tags: [CCNP, glossary, wireless, networking]
aliases: ["SSID", "Service Set Identifier", "Wireless Network Name", "Broadcast SSID", "Hidden SSID"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# SSID

## Definition

The **SSID (Service Set Identifier)** is the **human-readable name** of a wireless network, announced in **beacons** so clients can find and join it. A controller can host **multiple SSIDs** on the same radio fabric — each mapped to its own **VLAN and security policy** (guest, corp, IoT). The SSID is a *label*; the real radios behind it are [[BSSID]]s.

## SSID Plumbing

```text
one AP (or WLC-managed radio grid) → several SSIDs:
  "CORP" → VLAN 10, WPA2-Enterprise, strong PSK? no — cert/802.1X
  "GUEST" → VLAN 100, open+portal, isolated from CORP
clients scan: passive (listen beacons) or active (probe request for name)
hiding the SSID ≠ security — probes still reveal it
```

## Exam Focus

- **"What is the SSID?" → the network name; what is the BSSID?" → the radio MAC** — the identity pair (name vs hardware).
- **Multiple SSIDs per AP**: each = separate BSS + VLAN/marketing — the "how many SSIDs per AP?" design answer.
- **Hidden SSID is not secure** — probes leak it — the security myth question.
- SSID↔VLAN mapping is where wireless meets wired segmentation — the integration angle.

## Related Terms

- [[BSSID]], [[WLAN]], [[802.11]], [[VLAN]]
- Level 22 notes: [[Level 22 - Wireless/03. SSID]]