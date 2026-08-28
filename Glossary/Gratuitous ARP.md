---
tags: [CCNP, glossary, switching, networking]
aliases: ["Gratuitous ARP", "GARP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# Gratuitous ARP

## Definition

A **gratuitous ARP (GARP)** is an **unsolicited ARP** announcing "my IP is at my MAC" — broadcast without anyone asking. Used for **duplicate-address detection, MAC change notification, and fast failover** (FHRP virtual IPs, NIC teaming).

## What It Does

```text
source sends: "I am 10.1.1.1 at 00:11:22:33:44:55"  (broadcast)
  → every host updates its ARP cache entry for 10.1.1.1
  → duplicate IP? another host replies or announces too → conflict detected
```

| Use | Effect |
| --- | --- |
| Duplicate IP detection | Both "owners" announce → conflict flag |
| Virtual IP takeover | [[First Hop Redundancy Protocol|HSRP/VRRP]] active router announces new MAC instantly |
| NIC/link change | Neighbors re-learn the new MAC without waiting |

## Exam Focus

- **GARP updates caches proactively** — that is why attackers use it (ARP spoofing, MITM) and why **DAI** validates it.
- "HSRP switches active — how do hosts learn the new MAC fast?" → the new active sends gratuitous ARP.
- Recognize the classic exam symptom: "after failover, traffic works but ARP cache still shows old MAC until expiry" — GARP fixes it.

## Related Terms

- [[ARP]], [[Proxy ARP]], [[First Hop Redundancy Protocol]], [[DHCP Snooping]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/11. Gratuitous ARP]]