---
tags: [CCNP, glossary, switching, first-hop]
aliases: ["First Hop Redundancy Protocol", "FHRP", "Gateway Redundancy", "Virtual Gateway"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: First Hop Redundancy
created: 2026-08-29
---

# First Hop Redundancy Protocol

## Definition

An **FHRP (First Hop Redundancy Protocol)** gives end hosts a **single virtual default gateway** backed by **multiple real routers** — if the active router dies, a standby takes over **the same virtual IP and MAC**, so hosts keep working without any client reconfiguration. FHRPs are the "make the default gateway redundant" family.

## How It Works

```text
hosts use VIP 10.1.1.254 → virtual MAC (HSRP: 0000.0c07.acxx, VRRP: 0000.5e00.01xx)
   routers run election → one ACTIVE/MASTER, others STANDBY/BACKUP
   active fails → standby assumes VIP+VMAC in seconds (hello timers, preemption)
   hosts' ARP/NDP caches: the VMAC never changes → zero host impact
repayment: FHRP sends [[Gratuitous ARP]] to announce the takeover
```

| Protocol | Vendor | Detail |
| --- | --- | --- |
| [[HSRP]] | Cisco proprietary | Active/standby, group 0–255, UDP 1985 |
| [[VRRP]] | IEEE 3761 (RFC 9568) | Master/backup, standard, virtual IP can be real |
| [[GLBP]] | Cisco proprietary | Active/standby **virtual gateway** + up to 4 AVFs → load balancing |

## Exam Focus

- **"Which technology virtualizes the default gateway?" → FHRP** — the whole level's thesis.
- **Active/Standby vs Active/Active**: HSRP/VRRP = one active; GLBP = multi-active (AVG+AVFs) — the "which one load-balances?" answer is GLBP.
- **[[Object Tracking]]** pairs with any FHRP: track the uplink, decrement priority, standby takes over — the failover design.

## Related Terms

- [[HSRP]], [[VRRP]], [[GLBP]], [[Object Tracking]], [[Gratuitous ARP]]
- Level 14 notes: [[Level 14 - First Hop Redundancy/05. Gateway Redundancy]]