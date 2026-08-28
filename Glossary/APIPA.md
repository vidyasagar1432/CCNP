---
tags: [CCNP, glossary, ipv4, networking]
aliases: ["APIPA", "Automatic Private IP Addressing", "169.254"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: IPv4
created: 2026-08-29
---

# APIPA

## Definition

**APIPA (Automatic Private IP Addressing)** is what a DHCP-configured host uses when **no DHCP server answers**: it self-assigns an address from **169.254.0.0/16** (link-local). Seeing `169.254.x.x` = "this host couldn't get a lease" — a pure diagnostic.

## How It Works

```text
host boots, DHCP discover → 3 tries, no offer
    └► self-assigns 169.254.x.x (random, with conflict probing)
        └► no default gateway → local link only
        └► keeps retrying DHCP in background
```

## Exam Focus

- **"Why does a PC have 169.254.x.x?"** → DHCP failure — check the server, VLAN, or DHCP snooping, not the address itself.
- **APIPA addresses have no default gateway** — internet-bound traffic fails even though link-local talking works.
- IPv6's equivalent by-design feature is **link-local** addressing (SLAAC/NDP always uses it) — a "not a bug" contrast.

## Related Terms

- [[Private IP]], [[IPv4]], [[DHCP]]
- Level 05 notes: [[Level 05 - IPv4/07. APIPA]]