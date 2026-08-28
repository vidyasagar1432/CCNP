---
tags: [CCNP, glossary, switching, networking]
aliases: ["MAC Address", "Media Access Control", "Unicast MAC", "Multicast MAC", "Broadcast MAC"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Ethernet & Switching
created: 2026-08-29
---

# MAC Address

## Definition

A **MAC (Media Access Control) address** is the **Layer 2 identifier** burned into a network interface, used for local-frame delivery on Ethernet. It is a **48-bit (12 hex digit)** address: 6 bytes = **OUI (vendor) + serial**, written like `00:1A:2B:3C:4D:5E`.

## Structure & Types

| Type | I/G bit (first byte, bit 0) | Example |
| --- | --- | --- |
| Unicast | 0 | 00:1A:2B:3C:4D:5E |
| Multicast | 1 (L bit) | 01:00:5E:xx:xx:xx (IPv4 mcast) |
| Broadcast | All 1s | FF:FF:FF:FF:FF:FF |
| Locally administered | U/L bit set | 02:... (virtual/VRRP MACs) |

Format notes: **first hex digit bit0 = I/G (individual/group)**; U/L (universal/local) is the second bit — both exam favorites.

## How It's Used

- Switches learn source MACs into the **[[CAM Table]]**; frames are delivered by destination MAC ([[Forwarding]], [[Flooding]]).
- **IPv4 → MAC** mapping via [[ARP]]; **IPv6 → MAC** via NDP (solicited-node multicast).
- MACs are **link-local only** — they never cross a router (the router is the L2 boundary).

## Exam Focus

- **I/G and U/L bit reading** ("is this a unicast or multicast first octet?") — memorize 01/03/FF patterns.
- MAC ≠ identity on the Internet: filtering by MAC is a local-access security feature only.

## Related Terms

- [[Ethernet Frame]], [[CAM Table]], [[MAC Learning]], [[ARP]], [[Broadcast Domain]]
- Level 04 notes: [[Level 04 - Ethernet & Switching/01. MAC Address]]