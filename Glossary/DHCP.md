---
tags: [CCNP, glossary, network-services, networking]
aliases: ["DHCP", "Dynamic Host Configuration Protocol", "DHCP Server", "DHCP Lease"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# DHCP

## Definition

**DHCP (Dynamic Host Configuration Protocol)** automatically assigns IP **parameters** — address, mask, gateway, DNS, lease time — to hosts on boot. It replaces manual static configuration and is a core enterprise service: DORA, relays, snooping, and DHCPv6 all hang off it.

## The DORA Exchange

```text
D — DHCPDISCOVER  (client → broadcast 255.255.255.255, UDP 68 → 67)
O — DHCPOFFER     (server → client, offers an address)
R — DHCPREQUEST   (client → server: “I accept”, broadcast — for other servers to back off)
A — DHCPACK       (server → client: lease confirmed; DHCPNAK = refuse)
lease: default 24h, renewal at T1 (50%) / rebind at T2 (87.5%)
```

## Exam Focus

- **DORA is the definition question**; ports are trivia (client 68, server 67).
- Cross-segment DHCP needs **[[DHCP Relay]]** (`ip helper-address`) — the VLAN scenario.
- Security is DHCP's weakness: rogue servers, starvation → [[DHCP Snooping]] is the mitigation.
- Failure → [[APIPA|169.254]] on hosts — tie the symptom to the service.

## Related Terms

- [[DHCP Snooping]], [[DHCP Relay]], [[APIPA]], [[DHCPv6]]
- Level 16 notes: [[Level 16 - Network Services/01. DHCP]]