---
tags: [CCNP, glossary, switching, vlan]
aliases: ["Private VLAN", "PVLAN", "Promiscuous Port", "Isolated VLAN"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VLAN Technologies
created: 2026-08-29
---

# Private VLAN

## Definition

A **Private VLAN (PVLAN)** subdivides a VLAN into **isolated** and **community** sub-VLANs over a single primary VLAN — hosts in an isolated sub-VLAN can ONLY talk to the **promiscuous** gateway, never to each other. One IP subnet, L2 isolation inside it.

## PVLAN Anatomy

```text
primary VLAN (carrier)  ── hosts share the IP subnet
   ├── isolated VLAN (secondary)   — isolated ports talk ONLY to promiscuous
   └── community VLAN (secondary)  — community ports talk among themselves + promiscuous

promiscuous port = the uplink/gateway (router/firewall sees everyone)
isolated/community ports = hosts
```

| Port type | Who it can talk to |
| --- | --- |
| Promiscuous | Everything (all secondary VLANs + primary) |
| Isolated | Promiscuous only |
| Community | Same community + promiscuous |

## Exam Focus

- **"Hosts must share a subnet but never L2-talk to each other?" → PVLAN (isolated)** — the hotel/ISP multi-tenant answer.
- PVLAN on the wire: sub-VLAN tags ride the primary; the downstream switch keeps separation — knows the model, not just the config.
- **Proxy ARP danger**: routers on the promiscuous port can accidentally bridge isolated hosts — the classic PVLAN isolation-bypass attack.

## Related Terms

- [[VLAN]], [[Access Port]], [[Inter-VLAN Routing]]
- Level 07 notes: [[Level 07 - VLAN Technologies/03. Private VLAN]]