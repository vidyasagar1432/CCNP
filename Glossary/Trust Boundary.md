---
tags: [CCNP, glossary, qos, networking]
aliases: ["Trust Boundary", "QoS Trust Boundary", "Trusted Domain", "Untrusted Port"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# Trust Boundary

## Definition

The **trust boundary** is the line where the network **stops trusting** QoS markings ([[DSCP]]/CoS) forwarded by devices and **re-marks/classifies itself**: everything *inside* the boundary — network gear, IP phones, handsets — is trusted; everything outside (end-user PCs, BYOD) is **untrusted**. Default on Cisco switching: **all ports untrusted** (CoS 0 / DSCP 0) — you must explicitly trust or rebuild the markings.

## Where to Draw It

```text
[PC] ←Untrusted→ [Access switch — trust boundary] ←Trusted→ [Campus/WAN core]
access port policy: "trust dscp" only for known-good devices (phones, APs)
            or "set dscp" (re-mark per classification rules) for everything else
miscovery: phones tell the switch CoS via CDP → switch marks/trusts voice — the
"trust boundary extends to the phone" design (IP phone + PC daisy-chain)
```

## Exam Focus

- **"What is the trust boundary?" → the point past which markings are considered valid** — the definition; access edge is the classic answer.
- **Default behavior**: untrusted (markings zeroed) — the "what happens on a normal access port?" question.
- **Where to set it**: closest to the source while still being a trusted device — the design principle (edge/access, not the core).
- CDP + phone → the switch learns and trusts voice CoS — the nuanced scenario.

## Related Terms

- [[QoS Marking]], [[QoS Classification]], [[DiffServ]], [[DSCP]]
- Level 21 notes: [[Level 21 - QoS/12. QoS Marking & Trust Boundaries]]