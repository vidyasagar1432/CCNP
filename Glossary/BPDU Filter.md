---
tags: [CCNP, glossary, stp, switching]
aliases: ["BPDU Filter", "BPDUFilter"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: STP
created: 2026-08-29
---

# BPDU Filter

## Definition

**BPDU Filter** stops a port from **sending AND receiving BPDUs** — the port becomes invisible to spanning tree and is configured/expected to never talk to another switch.

## How It Works

```cisco
! Per interface
interface GigabitEthernet0/1
 spanning-tree bpdufilter enable
```

- The interface generally does not issue BPDUs and discards received ones.
- In RSTP terms, connecting a real switch to a BPDU-Filtered port is dangerous: with no BPDUs exchanged, the link can create a loop with zero STP visibility.

## BPDU Guard vs BPDU Filter

| Feature | BPDU Guard | BPDU Filter |
| --- | --- | --- |
| On BPDU received | Shuts port down (errdisable) | Drops the BPDU, port keeps forwarding |
| On BPDU send | Normal sending | Suppresses sending |
| Effect on STP | Port remains in STP | Port is effectively removed from STP |
| Safety | High (reactive) | Low (breaks STP participation) |

## Exam Focus

- **BPDU Filter is not "BPDU Guard for quiet ports."** It disables STP participation — an exam trap when the two are conflated.
- Filtering BPDUs on a trunk to a real switch removes loop protection entirely; use Guard (reactive) or PortFast-with-Guard instead.

## Related Terms

- [[BPDU Guard]], [[PortFast]], [[BPDU]], [[STP]]
- Level 08 notes: [[Level 08 - STP/11. BPDU Guard]] (BPDU Guard vs BPDU Filter section)