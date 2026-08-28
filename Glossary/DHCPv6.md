---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["DHCPv6", "DHCP for IPv6", "Stateful DHCPv6"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# DHCPv6

## Definition

**DHCPv6 (DHCP for IPv6)** is the **stateful** addressing/config service for IPv6 — the server assigns (parts of) the address or other parameters, unlike [[SLAAC]] which is stateless. Two critical differences vs IPv4 DHCP: **clients already have link-local**, and it uses **multicast (ff02::1:2)** — never broadcast.

## The Two Modes

| Mode | What it provides | Use with |
| --- | --- | --- |
| Stateful (M-flag) | Full address + options from server | Networks needing central control/audit |
| Stateless (O-flag) | Only options (DNS, domain); **address stays SLAAC** | Combine SLAAC prefix + DHCP options |

```text
also: DHCPv6-PD (Prefix Delegation) — ISP hands a /56 or /48
      to the customer router, which sub-delegates /64s per VLAN
```

## Exam Focus

- **"IPv6 address assignment without a server?" → SLAAC; "with a server?" → DHCPv6.** The M/O flag reading tells you which the router requested.
- **DHCPv6 correspondence**: relay (DHCPv6 relay) matches ipv4 helper-address; prefix delegation (PD) is the modern tie-in for [[Enterprise WAN]]/ISP designs.
- IPv6 DHCP runs over **UDP 546 (client) / 547 (server)** — answer the port question confidently.

## Related Terms

- [[SLAAC]], [[IPv6]], [[Global Unicast]], [[DHCP]], [[Neighbor Discovery]]
- Level 06 notes: [[Level 06 - IPv6/08. DHCPv6]]