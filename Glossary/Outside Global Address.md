---
tags: [CCNP, glossary, nat]
aliases: ["Outside Global"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# Outside Global Address

## Definition

The **outside global address** is the IP address *owned by* the outside host — the address the outside host truly has on the outside network. It is the address the remote server's own network knows.

## How It Works

In the standard Internet NAT design (server not translated):

```text
Outside Local = Outside Global
```

| Concept | Value | Meaning |
| --- | --- | --- |
| Outside global | `198.51.100.7` | The server's real public address |
| Outside local | `198.51.100.7` | The same address, since no outside translation |

When [[Outside Source NAT]] *is* used, outside global and outside local diverge: the router keeps the real address (outside global) internally while presenting an alias (outside local) to the inside network.

## Exam Focus

- **Outside global is "the address of the outside host as it exists on the outside."**
- The exam the easiest trap: mixing up *local/global* with *private/public* — the correct mapping is *local = inside-side representation*, *global = outside-side representation*.
- In `show ip nat translations`, the last two columns are labeled "Outside local" and "Outside global"; for ping/HTTP tests against a normal server they are identical, which is a good sanity check.

## Related Terms

- [[Outside Local Address]], [[Inside Local Address]], [[Inside Global Address]], [[Outside Source NAT]], [[NAT Translation Table]]
- Level 15 notes: [[Level 15 - NAT/01. Static NAT]]