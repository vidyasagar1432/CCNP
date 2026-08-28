---
tags: [CCNP, glossary, security, access-control]
aliases: ["ACL", "Access Control List", "Access-List", "Standard ACL", "Extended ACL"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Security
created: 2026-08-29
---

# ACL

## Definition

An **ACL (Access Control List)** is an **ordered list of permit/deny rules** applied to traffic (or routes, or NAT, or QoS classification...). Matching is **first-match-wins top-down** with an **implicit deny** at the end — the two rules that drive every ACL question. Classic form: **standard** (source only, 1–99) and **extended** (src+dst+port+protocol, 100–199; modern: named).

## The Rules That Never Change

```text
access-list 100 permit tcp any host 10.1.10.5 eq 443
access-list 100 deny ip any any            ← optional, then IMPLICIT DENY anyway
top-down! first match wins!
standard ACLs go CLOSEST TO DESTINATION (source-only filtering)
extended ACLs go CLOSEST TO SOURCE (waste no bandwidth)
```

## Everywhere ACLs Are Used

- **Filtering** (`ip access-group in/out`), **NAT** selection (`ip nat inside source list`), **route filtering** (distribute-list), **QoS class maps**, **CoPP** protection, **VTY access** (`access-class`).

## Exam Focus

- **"What happens to unmatched traffic?" → implicit deny** — the one-sentence answer.
- **Placement logic**: standard→destination, extended→source — a classic justification question.
- Wildcard math: `0.0.0.255` = "don't care last octet" — the bit-compare question (`access-list 10 permit 10.1.1.0 0.0.0.63`).
- Named ACLs (`ip access-list extended NAME`) = easier maintenance; entries are sequence-numbered — modern-practice mention.

## Related Terms

- [[Prefix List]], [[Route Map]], [[CoPP]], [[Port Security]]
- Level 17 notes: [[Level 17 - Security/04. ACL]]