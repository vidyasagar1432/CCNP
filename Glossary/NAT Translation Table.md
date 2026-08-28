---
tags: [CCNP, glossary, nat]
aliases: ["NAT table", "Translation table", "show ip nat translations"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT Translation Table

## Definition

The **NAT translation table** is the state structure on the NAT router that records how the four address terms relate for each active translation — the inside ↔ outside mapping used to translate forward traffic and reverse-translate return traffic.

## How It Works

```cisco
show ip nat translations
```

```text
Pro Inside global      Inside local       Outside local      Outside global
--- 203.0.113.10:1025  192.168.10.10:1025 198.51.100.10:443  198.51.100.10:443
```

| Column | Meaning |
| --- | --- |
| Inside global | The translated source the outside sees |
| Inside local | The real inside host address |
| Outside local | The destination as seen from inside |
| Outside global | The destination's real address |

Return traffic matches this table to reverse the translation:

```text
Outbound: src 10.0.0.10       → 203.0.113.10
Return:   dst 203.0.113.10    → 10.0.0.10
```

## Key Facts

- Entries are created **on demand** (dynamic/PAT) or **by configuration** (static).
- Dynamic entries disappear after aging out (see [[NAT Timers]]).
- `clear ip nat translation *` wipes active entries — deliberate action, it can disrupt live sessions (the *configuration* survives).
- For PAT, the **protocol + ports** column distinguishes multiple flows sharing one global address.

## Exam Focus

- The table is the **evidence** that NAT is actually creating state; empty/missing entries mean classification, routing, or rule problems.
- `show ip nat statistics` gives counters and pool/resource info — complementary to the table, not a replacement.

## Related Terms

- [[NAT]], [[Static NAT]], [[Dynamic NAT]], [[PAT]], [[Inside Local Address]], [[Inside Global Address]]
- Level 15 notes: [[Level 15 - NAT/06. Troubleshooting]], [[Level 15 - NAT/02. Dynamic NAT]]