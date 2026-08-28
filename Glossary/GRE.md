---
tags: [CCNP, glossary, vpn, tunneling]
aliases: ["GRE", "Generic Routing Encapsulation", "GRE Tunnel"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: VPN Technologies
created: 2026-08-29
---

# GRE

## Definition

**GRE (Generic Routing Encapsulation)** is a **tunneling protocol**: it wraps any payload protocol (IPv4, IPv6, multicast, broadcast) inside an **IP packet** (IP protocol 47) to carry it over arbitrary networks. **No encryption** — GRE is for transport (routing over a tunnel), not secrecy; classic pairing is **GRE-over-IPsec** to add the crypto.

## GRE Facts to Bank

```text
tunnel source / tunnel destination = real interface addresses
tunnel 0: ip address 10.0.0.1/30 (virtual point-to-point)
encapsulation: [outer IP (proto 47)][GRE header][inner packet]
carries multicast/broadcast → routing protocols (OSPF/EIGRP) run INSIDE tunnels
keepalives: tunnel keepalive — detects dead far end
adds 4-byte GRE header (+ 20 IP) → MTU/PMTU exercises!
```

## Exam Focus

- **"Which tunneling protocol carries multicast and broadcasts?" → GRE** — its superpower vs plain IPsec (which does not).
- **GRE is unencrypted** — "what protects GRE?" → nothing; pair with IPsec (or use IPsec VTI for modern).
- **IP protocol 47** = GRE; the packet-encapsulation order question (outer IP → GRE → inner packet).
- Routed vs routed: GRE tunnels plus routing (usually OSPF/EIGRP inside) = overlay routing design — DMVPN builds on exactly this.

## Related Terms

- [[IPsec]], [[DMVPN]], [[Virtual Tunnel Interface]], [[MTU]]
- Level 18 notes: [[Level 18 - VPN Technologies/01. GRE]]