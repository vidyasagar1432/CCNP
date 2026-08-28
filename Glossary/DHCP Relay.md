---
tags: [CCNP, glossary, network-services, networking]
aliases: ["DHCP Relay", "ip helper-address", "DHCP Relay Agent"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# DHCP Relay

## Definition

**DHCP relay** forwards DHCP broadcasts across subnets to a **central DHCP server**: a router with `ip helper-address <server>` on the client VLAN intercepts DISCOVERs and forwards them **as unicast** (using the giaddr field so the server answers the right subnet). One server pool per VLAN — no server needed per segment.

## The Helper-Address Pattern

```text
interface vlan 10
  ip helper-address 10.1.99.5        ← DHCP server in another subnet
client 10.1.10.10 broadcasts DISCOVER
router inserts giaddr = 10.1.10.1 (client subnet!) → unicasts to server
server picks a pool matching the giaddr → OFFER via the same relay path
```

## Exam Focus

- **"How does a client in VLAN 20 reach a DHCP server in VLAN 10?" → DHCP relay / helper-address** — the inter-VLAN scenario.
- **giaddr** is the relay's own interface address on the client segment — the server's "which pool?" answer.
- `ip helper-address` forwards **other UDP broadcasts too** (TFTP, DNS, NetBIOS…) — trivia: it's a UDP broadcast forwarder, not DHCP-only (security note: helper on too many interfaces leaks broadcasts).

## Related Terms

- [[DHCP]], [[DHCP Snooping]], [[TFTP]], [[DNS]]
- Level 16 notes: [[Level 16 - Network Services/03. DHCP Relay]]