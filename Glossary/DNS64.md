---
tags: [CCNP, glossary, nat, dns, ipv6]
aliases: ["DNS64 resolver"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# DNS64

## Definition

**DNS64** is a DNS mechanism used alongside [[NAT64]]: when an IPv4-only domain has no AAAA record, the DNS64 resolver **synthesizes one** by embedding the IPv4 address into the NAT64 Well-Known Prefix.

```text
Original A record:        192.0.2.10
Synthesized AAAA record:  64:ff9b::c000:020a
```

## How It Works

```text
IPv6 client asks for AAAA
        ↓
No native AAAA exists
        ↓
DNS64 synthesizes AAAA from the A record
        ↓
Client now has an IPv6 destination to talk to
        ↓
Traffic to 64:ff9b::/96 is routed to the NAT64 translator
```

The synthesized address always uses the NAT64 Well-Known Prefix `64:ff9b::/96` with the IPv4 octets in the final 32 bits:

```text
192.0.2.10  =  C0 00 02 0A  →  64:ff9b::c000:020a
```

## Division of Labor

| Technology | Job |
| --- | --- |
| DNS64 | Answers **"which IPv6 address should the client use?"** |
| NAT64 | Answers **"how do I translate that IPv6 traffic into IPv4?"** |

## Exam Focus

- **DNS64 ≠ NAT64**, though they are normally deployed together. DNS64 only changes the DNS answer — it does **not** translate packets.
- NAT64 does *not strictly require* DNS64: if the application already knows a valid synthesized address, translation works without it. But for normal hostname-based apps, DNS64 is what makes IPv4-only destinations reachable.
- If the client receives only an A record (no synthesized AAAA), the IPv6-only client may not know how to reach the IPv4 server — a classic troubleshooting step 3 check.

## Related Terms

- [[NAT64]], [[NAT]]
- Level 15 notes: [[Level 15 - NAT/05. NAT64]]