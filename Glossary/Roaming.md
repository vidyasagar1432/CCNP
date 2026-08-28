---
tags: [CCNP, glossary, wireless, networking]
aliases: ["Roaming", "Wireless Roaming", "Layer 2 Roaming", "Layer 3 Roaming", "Fast Roaming", "802.11r"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# Roaming

## Definition

**Roaming** is a client **moving from one AP/BSS to another and keeping its session**. Types: **Layer 2 roaming** (same subnet — new AP, no IP change; easiest), **Layer 3 roaming** (new subnet — needs mobility anchoring to keep the IP/state). **Fast roaming** (802.11r, i.e. **FT**) cuts re-auth latency for voice by pre-shared keys across the ESS. The exam loves the roam-type table.

## Roam Types

| Type | When | What changes | Needs |
| --- | --- | --- | --- |
| L2 roam | Same VLAN, new AP | BSSID only | Nothing extra |
| L3 roam | New VLAN/subnet | IP would change | WLC mobility (anchor keeps IP) |
| Fast roam | High-latency apps | Handshake per AP | 802.11r (FT), 802.11k (measure) |

## Exam Focus

- **"What differentiates L2 vs L3 roaming?" → whether the client crosses subnets** — the core; L3 needs the WLC to anchor.
- **802.11r = fast transition**: key caching so re-association is quick — the "which amendment fixes voice roam latency?" answer.
- Roaming vs [[Mobility]]: roaming = the client act; mobility = the WLC/network machinery — the scope pairing.
- Roaming is seamless only if the network anticipates it (same SSID, proper channel planning) — the design angle.

## Related Terms

- [[Mobility]], [[WLC]], [[BSSID]], [[WLAN]]
- Level 22 notes: [[Level 22 - Wireless/10. Roaming]]