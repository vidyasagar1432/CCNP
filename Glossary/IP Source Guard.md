---
tags: [CCNP, glossary, security, switching]
aliases: ["IP Source Guard", "IPSG"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# IP Source Guard

## Definition

**IP Source Guard (IPSG)** filters **ingress traffic by source IP** at the port, using the **DHCP-snooping binding table**: packets whose source IP isn't bound to that port (or lack an IP/MAC match) are dropped — blocking **IP spoofing** and **MAC/IP impersonation** on access ports. Port-based, per-VLAN, and typically paired with [[Dynamic ARP Inspection]] and [[DHCP Snooping]].

## The Stack

```text
ip dhcp snooping vlan 10                  ← bindings source
ip dhcp snooping trust (uplinks)
ip arp inspection vlan 10                 ← DAI: validates ARP against bindings
interface gi0/1
  ip verify source port-security           ← IPSG: validate DATA plane by IP(+MAC)
  (port-security variant: also check MAC → 'ip verify source port-security')
```

## Exam Focus

- **"Which feature blocks spoofed source-IP traffic on access ports?" → IP Source Guard** — the definition; `ip verify source` is the command.
- **It consumes the DHCP-snooping binding table** — "what must be enabled first?" → DHCP snooping (or static `ip source binding`).
- IPSG + DAI + snooping = the **first-hop security trio** (spoofed ARP, spoofed IP, rogue DHCP all covered) — the "which combination?" question.
- DHCP-based bindings only: static hosts need manual binding entries — the config gap worth mentioning.

## Related Terms

- [[DHCP Snooping]], [[Dynamic ARP Inspection]], [[Port Security]], [[ARP]]
- Level 17 notes: [[Level 17 - Security/07. IP Source Guard]]