---
tags: [CCNP, glossary, nat]
aliases: ["Inside Local"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Inside Local Address

## Definition

The **inside local address** is the IP address assigned to a host on the inside network, **as that address appears on the inside (private) side** of the NAT boundary. It is normally an RFC 1918 private address, but it does not have to be — it is simply the inside host's real, untranslated source address.

## How It Works

The inside local address is the address that:

- the inside host uses as its own source address,
- traffic destined to the host from the inside uses as the destination,
- the NAT router looks up as the "key" when an inside host initiates traffic.

```text
PC1 ──► NAT router ──► Internet
10.0.0.10   │         203.0.113.10
            │
            └──── Inside Local: 10.0.0.10
                  Inside Global: 203.0.113.10
```

The router translates **[[Inside Local Address]] → [[Inside Global Address]]** for outbound packets, and the reverse for return traffic.

## Example

| Concept | Value | Meaning |
| --- | --- | --- |
| Inside local | `10.0.0.10` | PC1's real address on the LAN |
| Inside global | `203.0.113.10` | How the Internet sees PC1 |
| Outside local | `198.51.100.7` | The server as PC1 sees it |
| Outside global | `198.51.100.7` | The server's real public address |

## Exam Focus

- *Local* always refers to the **inside perspective** — do not confuse *local* with "the host's own address is always private." A host can have a publicly-addressed inside local address.
- In `show ip nat translations`, the **Inside local** column is the pre-translation address.
- The mental model: **inside / outside** says *which side of the boundary the host belongs to*; **local / global** says *how that address is represented*.

## Related Terms

- [[Inside Global Address]], [[Outside Local Address]], [[Outside Global Address]], [[NAT]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/01. Static NAT]], [[Level 15 - NAT/02. Dynamic NAT]], [[Level 15 - NAT/03. PAT]]