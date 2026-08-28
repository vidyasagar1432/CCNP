---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["IPv6 Multicast", "Multicast Group", "ff00::/8"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# IPv6 Multicast

## Definition

**IPv6 multicast** (scope **ff00::/8**) is IPv6's replacement for broadcasting: packets are sent to a **group address** and delivered only to members of that group. Every broadcast-like need (ARP, DHCP, router solicitation) is expressed as a multicast group instead.

## The ff00::/8 Form

```text
ff  | flags(4) | scope(4) | group ID (112 bits)
     scope: 1=interface-local 2=link-local 5=site-local 8=organization E=global
examples:
  ff02::1      all-nodes (link-local)      — "broadcast workaround"
  ff02::2      all-routers (link-local)
  ff02::5 / ff02::6    OSPFv3 DR/BDR (all-OSPF-routers / DRs)
  ff02::1:ff00:0000/104  solicited-node    — NDP's targeted replacement for ARP
  ff05::1:3    all-DHCP-servers (site)
```

## Exam Focus

- **'Which IPv6 mode replaces broadcast?' → multicast** — specifically `ff02::1` all-nodes.
- **Solicited-node multicast (ff02::1:ffXX:XXXX)** matters for NDP: DAD and neighbor discovery hit one small group, not the whole link — that's WHY IPv6 has no broadcast storm problem like ARP.
- OSPFv3 hello destination = `ff02::5` — adjust your OSPF multicast answers for IPv6.

## Related Terms

- [[IPv6]], [[IPv4 Multicast]], [[Neighbor Discovery]], [[OSPFv3]]
- Level 06 notes: [[Level 06 - IPv6/06. Multicast]]