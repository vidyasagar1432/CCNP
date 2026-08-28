---
tags: [CCNP, glossary, nat]
aliases: ["NAT address pool"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT Pool

## Definition

A **NAT pool** is a configured range of inside-global addresses that [[Dynamic NAT]] rules allocate from — and return to — as translations are created and expire.

```cisco
ip nat pool PUBLIC 203.0.113.10 203.0.113.20 netmask 255.255.255.0
```

Contains 11 usable addresses: `203.0.113.10` … `203.0.113.20`.

## How It Works

- The router picks a **free** address from the pool when an eligible flow needs translation.
- The address is linked to the [[Inside Local Address]] in the [[NAT Translation Table]].
- When the translation expires (see [[NAT Timers]]), the address returns to the pool and another host can use it.
- Without `overload`, **each active translation consumes one pool address**.

## Pool Exhaustion

```text
Inside host
    ↓
NAT lookup
    ↓
No free pool address
    ↓
Translation cannot be created
```

New inside hosts cannot get a translation until an address frees up. Solutions: enlarge the pool, reduce translation lifetimes, or enable [[NAT Overload]] (PAT).

## Exam Focus

- Pool addresses are **borrowed, not owned** — the mapping between host and global address is temporary in dynamic NAT.
- A pool with `overload` becomes a PAT pool (address + port sharing).
- `show ip nat statistics` reveals pool utilization / exhaustion.

## Related Terms

- [[Dynamic NAT]], [[PAT]], [[NAT Overload]], [[Inside Global Address]], [[NAT Timers]]
- Level 15 notes: [[Level 15 - NAT/02. Dynamic NAT]], [[Level 15 - NAT/03. PAT]]