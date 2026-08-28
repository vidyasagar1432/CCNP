---
tags: [CCNP, glossary, nat]
aliases: ["NAT overload", "overload keyword"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT Overload

## Definition

**NAT Overload** is the *behavior enabled by the `overload` keyword* that turns an ordinary address-translation rule into [[PAT]] — allowing many inside hosts to share one (or a few) inside-global addresses through port multiplexing.

## How It Works

```cisco
! Without overload — 1:1 Dynamic NAT
ip nat inside source list 10 pool PUBLIC

! With overload — port multiplexing / PAT
ip nat inside source list 10 pool PUBLIC overload
```

Without `overload`:

```text
10.0.0.10  →  203.0.113.10
10.0.0.11  →  203.0.113.11
```

With `overload`:

```text
10.0.0.10:50001  →  203.0.113.10:50001
10.0.0.11:50002  →  203.0.113.10:50002
```

## Key Facts

- `overload` works with pool-based rules **and** interface-based rules (`ip nat inside source list X interface Gi0/1 overload`).
- The global address can be reused for **simultaneous** translations.
- It solves pool exhaustion caused by [[Dynamic NAT]] without collapsing back into 1:1 behavior.

## Exam Focus

- **Exam trap:** `overload` is *the* keyword that enables PAT behavior. Know what changes when it is present vs absent.
- Dynamic NAT does **not automatically fall back to PAT** when the pool is full — `overload` must be explicitly configured.

## Related Terms

- [[PAT]], [[Dynamic NAT]], [[NAT Pool]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/03. PAT]], [[Level 15 - NAT/02. Dynamic NAT]]