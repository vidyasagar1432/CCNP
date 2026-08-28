---
tags: [CCNP, glossary, nat]
aliases: ["Dynamic Translation", "Pool NAT"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Dynamic NAT

## Definition

**Dynamic NAT** creates **temporary one-to-one mappings** between inside local addresses and addresses drawn from a configured [[NAT Pool]]. The mapping is created when eligible traffic requires translation and removed when it ages out (see [[NAT Timers]]).

```text
10.0.0.10  ◄──────►  203.0.113.10   (while active)
10.0.0.11  ◄──────►  203.0.113.11
```

## How It Works

```cisco
access-list 10 permit 10.0.0.0 0.0.0.255

ip nat pool PUBLIC 203.0.113.10 203.0.113.20 netmask 255.255.255.0
ip nat inside source list 10 pool PUBLIC
```

The **NAT ACL** selects eligible inside sources; the router allocates a free pool address; the translation lives as long as the session; when it expires the address returns to the pool.

## Key Characteristics

| Aspect | Behavior |
| --- | --- |
| Mapping | Temporary 1:1 while active |
| Creation | Traffic-triggered |
| Pool | Required |
| Ports translated | No |
| Multi-host per global IP | No (without `overload`) |
| Inbound initiation | No permanent mapping |

## Exam Focus

- **Dynamic NAT is not PAT.** It does not translate ports and does not fall back to PAT automatically when the pool is exhausted.
- **Pool exhaustion**: when every address is allocated, new translations cannot be created — check with `show ip nat statistics`.
- Without `overload` → one inside host per pool address; `overload` converts the rule into [[PAT]] (see [[NAT Overload]]).
- Because mappings are temporary, outside hosts cannot reliably initiate inbound connections to a dynamic translation.

## Related Terms

- [[Static NAT]], [[PAT]], [[NAT Pool]], [[NAT ACL]], [[NAT Timers]], [[NAT Overload]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/02. Dynamic NAT]]