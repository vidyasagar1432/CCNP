---
tags: [CCNP, glossary, security, switching]
aliases: ["Dynamic ARP Inspection", "DAI", "ARP Inspection"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# Dynamic ARP Inspection

## Definition

**DAI (Dynamic ARP Inspection)** validates every [[ARP]] packet against the **DHCP-snooping binding table** (IP↔MAC↔port) and drops mismatches — killing **ARP spoofing/poisoning** (man-in-the-middle via falsified ARP). Trusted ports (uplinks) skip validation; untrusted access ports are inspected. Requires **[[DHCP Snooping]]** to be on.

## How It Works

```text
ip arp inspection vlan 10,20          ← enable on the VLAN(S)
interface gi0/1: ip arp inspection trust   (uplink → trusted)
untrusted port ingress: ARP reply (or request) checked vs bindings —
  any IP/MAC mismatch or gratuitous ARP from nowhere → DROPPED + logged
static host? → ip arp inspection filter (static ACL-based validation)
```

## Exam Focus

- **"Which feature detects/prevents ARP poisoning?" → DAI** — the definition question; dependency ("requires DHCP snooping") is the trap.
- **Trust placement** mirrors snooping: trust the side toward the legitimate server/gateway — the "where do you put trust?" scenario.
- DAI drops invalid **gratuitous ARP** — the [[Gratuitous ARP]] tie-in for attack questions.
- Rate limiting: ARP packet rate on untrusted ports (`ip arp inspection limit rate`) — the flood-defense add-on.

## Related Terms

- [[ARP]], [[Gratuitous ARP]], [[DHCP Snooping]], [[IP Source Guard]], [[Port Security]]
- Level 17 notes: [[Level 17 - Security/06. Dynamic ARP Inspection]]