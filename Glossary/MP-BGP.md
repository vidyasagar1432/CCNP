---
tags: [CCNP, glossary, mpls, networking]
aliases: ["MP-BGP", "Multiprotocol BGP", "BGP VPNv4", "VPNv4", "Address Family"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# MP-BGP

## Definition

**MP-BGP (Multiprotocol BGP)** extends [[BGP]] with **address families** and labeled routes — the control plane of MPLS L3VPNs. Between PEs it carries **VPNv4** routes: customer prefixes made unique by prepending the **RD** (`RD:prefix`), tagged with **RTs** for import/export, plus the **VPN label** learned through BGP. No IGP can carry those — only MP-BGP.

## The VPNv4 Exchange

```text
PE1: customer route 10.1.0.0/16 (VRF red) →
     VPNv4: RD 65000:100 → 65000:100:10.1.0.0/16
     community RT 65000:100 → controls who imports it
     accompanying label = the far PE's forwarding instruction
PEs peer over MP-BGP (address-family vpnv4 unicast), cores stay label-only
```

## Exam Focus

- **"Which protocol carries VPNv4 between PEs?" → MP-BGP** — the L3VPN control-plane answer; BGP alone can't (no address families / no VPN labels).
- **RD can't be translated**: VPNv4 = RD + prefix; RT decides import/export — the RD/RT pair question (see [[VRF]]).
- Classic CLI: `address-family vpnv4` + `neighbor X activate` — the configuration recognition.
- MP-BGP is also how **IPv6** rides in BGP (AF ipv6), and how labeled unicast works — "multiprotocol" is the general mechanism.

## Related Terms

- [[BGP]], [[VRF]], [[MPLS VPN]], [[MPLS]], [[Route Tag]]
- Level 20 notes: [[Level 20 - MPLS/08. MP-BGP]]