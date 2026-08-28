---
tags: [CCNP, glossary, nat]
aliases: ["Outside NAT"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Outside Source NAT

## Definition

**Outside Source NAT** translates the source address of a packet that is **owned by the outside network** — rewriting how the outside host appears to the inside network. It is the opposite direction from ordinary inside source NAT.

```cisco
ip nat outside source static 203.0.113.99 198.51.100.99
```

```text
Outside address            Translated to
203.0.113.99    ────────►   198.51.100.99   (as seen from inside)
```

## How It Works

- The command **direction** (`inside source` vs `outside source`) describes *which side's source address is translated*, not merely where the packet physically enters the router.
- For inside source NAT: `ip nat inside source ...` — inside host's source is rewritten.
- For outside source NAT: `ip nat outside source ...` — outside host's source is rewritten.

## Where It Is Used

- **Overlapping address spaces** (the inside network uses an address range that collides with a remote network's addresses)
- Merging networks with duplicate addressing
- Certain VPN / partner connectivity designs

## Exam Focus

- **Outside source NAT is NOT the same as [[Policy NAT]].** It is a NAT direction/type; policy NAT is a selectivity mechanism. This is an explicit exam trap.
- After outside source NAT, [[Outside Local Address]] ≠ [[Outside Global Address]].

## Related Terms

- [[NAT]], [[Policy NAT]], [[Outside Local Address]], [[Outside Global Address]]
- Level 15 notes: [[Level 15 - NAT/04. Policy NAT]]