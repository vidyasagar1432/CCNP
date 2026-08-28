---
tags: [CCNP, glossary, ospf, routing]
aliases: ["OSPF Authentication", "MD5 Authentication", "HMAC-SHA OSPF"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: OSPF
created: 2026-08-29
---

# OSPF Authentication

## Definition

**OSPF authentication** verifies that OSPF packets come from trusted neighbors, preventing spoofed hello/LSA injection. Both sides of a link must use **identical** type and key, or the adjacency fails.

## Authentication Types

| Type | Mechanism | Security |
| --- | --- | --- |
| `null` | None (default) | None |
| Simple/plaintext | Cleartext password in packets | Weak (readable) |
| Cryptographic (MD5 / HMAC-SHA) | Keyed hash, key ID, never sends the key | Strong (recommended) |

```cisco
interface GigabitEthernet0/0
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 CCNP-Key

! Or area-wide
router ospf 1
 area 0 authentication message-digest
```

## Exam Focus

- Authentication parameters are part of the **neighbor-relationship requirements** — a mismatch keeps routers stuck at Init/2-Way (see [[OSPF Neighbor States]]).
- **Key ID must match on both ends** (a classic mismatch vector).
- OSPFv3 uses **IPsec AH/ESP** for authentication instead of the v2 field — a common OSPFv2 vs OSPFv3 exam difference (see [[OSPFv3]]).
- Authentication protects the routing domain from route-injection attacks, not data confidentiality.

## Related Terms

- [[OSPF]], [[OSPF Neighbor States]], [[OSPFv3]]
- Level 10 notes: [[Level 10 - OSPF/13. Authentication]]