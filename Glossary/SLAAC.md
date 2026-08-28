---
tags: [CCNP, glossary, ipv6, networking]
aliases: ["SLAAC", "Stateless Address Autoconfiguration", "Router Advertisement", "RA"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv6
created: 2026-08-29
---

# SLAAC

## Definition

**SLAAC (Stateless Address Autoconfiguration)** lets a host build its own **Global Unicast Address from a Router Advertisement**: the router sends the **/64 prefix**, the host derives its **interface ID** (EUI-64 or random), and combines them — with **no DHCP server involved** (hence "stateless"). The host also gets the router as default gateway via RA.

## The Flow

```text
host boots → joins ff02::1 (all-nodes) + asks via Router Solicitation (ff02::2)
router replies: Router Advertisement  (prefix 2001:db8:1:2::/64, default route)
host: builds 2001:db8:1:2:<IID>/64
      runs DAD (solicited-node multicast probe — Duplicate Address Detection)
      uses router's link-local as default gateway
```

## Exam Focus

- **"Which feature configures IPv6 without DHCP?"** → SLAAC — the *stateless vs stateful* contrast with [[DHCPv6]].
- **RA flag math** is a classic question: flags can say "use SLAAC" (M=0,O=0), "use DHCPv6" (M=1), or "SLAAC + DHCPv6 for other info" (O=1).
- RA security: **RA Guard** — spoofed RAs hijack default routes; first-hop security topic ([[First Hop Redundancy Protocol|FHRP]] world).

## Related Terms

- [[IPv6]], [[Global Unicast]], [[Link Local]], [[DHCPv6]], [[Neighbor Discovery]]
- Level 06 notes: [[Level 06 - IPv6/07. SLAAC]]