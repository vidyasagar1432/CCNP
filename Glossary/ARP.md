---
tags: [CCNP, glossary, switching, networking]
aliases: ["Address Resolution Protocol", "ARP Cache", "ARP Request", "ARP Reply"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# ARP

## Definition

**ARP (Address Resolution Protocol)** maps an **IPv4 address → MAC address** on the local L2 segment — the glue between Layer 3 destinations and Layer 2 delivery. (IPv6 equivalent: **NDP**, via ICMPv6.)

## How It Works

```text
need to send to 10.1.1.2, MAC unknown →
  1. ARP request: broadcast (target = 10.1.1.2, MAC = ??) 
  2. owner replies: ARP reply, unicast, "I am 10.1.1.2, my MAC is ..."
  3. both sides cache (ARP cache/cam) for a few minutes
```

- **Request = broadcast, reply = unicast** — a textbook fact.
- Cached entries age out (default up to 4 h; refresh on use).
- If the destination is in another subnet → ARP for the **default gateway** (see [[Proxy ARP]] for the variant).

## Exam Focus

- **"Which protocol maps IPv4 → MAC?"** → ARP. "ARP is used by IPv4 only" — IPv6 never uses ARP.
- ARP poisoning/spoofing attacks → mitigation with **DAI (Dynamic ARP Inspection)**; see [[DHCP Snooping]] tie-ins.
- `show ip arp` — the cache is exam output; malformed/gratuitous ARP behaviors are attack scenarios.

## Related Terms

- [[Gratuitous ARP]], [[Proxy ARP]], [[MAC Address]], [[IPv4]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/10. ARP]]