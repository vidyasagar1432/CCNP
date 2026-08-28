---
tags: [CCNP, glossary, security, switching]
aliases: ["DHCP Snooping", "DHCP Starvation", "Rogue DHCP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# DHCP Snooping

## Definition

**DHCP snooping** is a switch security feature that builds a **trust boundary around DHCP**: **trusted ports** (uplinks toward the legitimate server) may send DHCP server replies; **untrusted ports** (toward hosts) may only send **DISCOVER/REQUEST**. Any OFFER/ACK arriving on an untrusted port is dropped — killing rogue-DHCP attacks. It also builds an **IP↔MAC↔port** binding database used by [[IP Source Guard]] and DAI.

## How It Works

```text
switchport:  interface gi0/1 → ip dhcp snooping trust   (uplink = trusted)
             host ports: untrusted (default)
untrusted ingress: DHCP OFFER/ACK → dropped (rogue server blocked)
                   DHCP release → rate-limited… (starvation blocked)
binding table: ip dhcp snooping binding (IP, MAC, VLAN, port, lease)
  → DAI validates ARP against this; IP Source Guard filters traffic by it
```

## Exam Focus

- **"Which feature stops rogue DHCP servers?" → DHCP snooping**, with trust placement = the config question (trust only toward the real server).
- **DHCP starvation**: attacker floods DISCOVERs to exhaust the pool — mitigation = per-port rate limiting (`ip dhcp snooping limit rate`).
- **DERIVED facts**: snooping's bindings feed **DAI ([[ARP]] validation)** and **IP Source Guard** — the three-way security stack; snooping must be on for those to work.

## Related Terms

- [[DHCP]], [[ARP]], [[IP Source Guard]], [[Port Security]]
- Level 16 notes: [[Level 16 - Network Services/02. DHCP Snooping]]