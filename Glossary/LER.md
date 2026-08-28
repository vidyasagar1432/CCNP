---
tags: [CCNP, glossary, mpls, networking]
aliases: ["LER", "Label Edge Router", "Ingress LER", "Egress LER"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: MPLS
created: 2026-08-29
---

# LER

## Definition

An **LER (Label Edge Router)** sits at the **edge of the MPLS domain** — the only router that touches pure IP and labels. **Ingress LER**: classifies packets into [[FEC]]s and **pushes** labels. **Egress LER**: **pops** the label and hands IP to the next domain. Providers call it **PE (Provider Edge)** when it also hosts services like [[VRF]]s and [[MPLS VPN|VPNs]].

## The Edge Job

```text
INGRESS: IP packet → FEC lookup → push outer(+inner) label → forward
EGRESS:  label-for-us → pop → forward as plain IP (or to VRF / VPN)
labels are LER-scoped decisions; core never sees the IP header
```

## Exam Focus

- **"Which router pushes/pops MPLS labels?" → the LER**; core ([[LSR]]) only swaps — the role question.
- **Edge vs core**: LERs do the deep lookups and classification; LSRs do the fast label forwarding — the division of labor.
- **PE vs LER**: LER = label plane role; PE = LER + service plane (VRF, MP-BGP) — keep them mapped correctly.
- When a label points at the router itself → pop (the "incoming label = my label" rule).

## Related Terms

- [[MPLS]], [[LSR]], [[MPLS Label]], [[FEC]], [[MP-BGP]], [[VRF]]
- Level 20 notes: [[Level 20 - MPLS/03. LER]]