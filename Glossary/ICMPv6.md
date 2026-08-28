---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["ICMPv6", "Internet Control Message Protocol for IPv6"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# ICMPv6

## Definition

**ICMPv6** is the control/error protocol of IPv6 — and unlike IPv4, it is **required** for basic operation: it carries **error reporting (destination unreachable, too big, time exceeded)**, **ping (echo request/reply)**, **[[Neighbor Discovery|NDP]] messages (NS/NA/RS/RA)**, and **Multicast Listener Discovery (MLD)** — all in protocol 58.

## The Message Map

```text
Types (type field, not ports):
  1   destination unreachable   (1 = no route to host, 4 = port unreachable)
  2   packet too big            ← paths MUST honor it (PMTUD)
  3   time exceeded             (hop limit expired → traceroute)
  128 echo request / 129 echo reply   (ping)
  133/134 RS/RA, 135/136 NS/NA        (NDP — “ARP” and router discovery)
  130–132 MLD                     (IPv6 multicast membership)
```

## Exam Focus

- **"Packet too big" (type 2) is IPv6's fragmentation control**: routers drop too-big packets and send this back — host re-fragments. The absence of mid-path fragmentation is the key IPv6 fact.
- **PMTUD depends on ICMPv6 being allowed** — blocking type 2 breaks large-packet connectivity; black-hole troubleshooting question.
- Ping works with **ICMPv6 echo (128/129)**; traceroute reads type 3.

## Related Terms

- [[Neighbor Discovery]], [[IPv6]], [[IPv4 Multicast]]
- Level 06 notes: [[Level 06 - IPv6/10. ICMPv6]]