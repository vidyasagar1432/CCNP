---
tags: [CCNP, glossary, nat, acl]
aliases: ["NAT ACL", "NAT classification ACL"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT ACL

## Definition

A **NAT ACL** is an access-list used by a NAT rule to **classify which traffic is eligible for translation**. It decides *whether a packet is a translation candidate* — it is **not** a security filter.

```cisco
access-list 10 permit 10.0.0.0 0.0.0.255
ip nat inside source list 10 pool PUBLIC
```

## How It Works

```text
ACL 10
  ↓
Selects eligible inside source addresses
  ↓
NAT rule applies to matched traffic only
```

The NAT ACL can be:

- A **standard ACL** (source-only match) — typical for ordinary source NAT
- An **extended ACL** (source + destination + protocol + port) — typical for [[Policy NAT]]

## The Big Distinction

```text
ACL used by NAT          ≠        Security ACL
classifies traffic                permits/denies packets
for translation                   through the router
```

Same ACL syntax, entirely different purpose depending on where it is applied.

## Exam Focus

- An ACL hit (`show access-lists` counters increasing) does **not** guarantee a translation exists — classification, pool, interface roles, and routing all still matter.
- **Exam trap:** never describe a NAT ACL as "the firewall policy." Security filtering is a separate function.
- ACL too broad → unexpected hosts translated; too narrow → expected hosts missed. Verify with `show access-lists`.

## Related Terms

- [[NAT]], [[Dynamic NAT]], [[PAT]], [[Policy NAT]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/02. Dynamic NAT]], [[Level 15 - NAT/06. Troubleshooting]]