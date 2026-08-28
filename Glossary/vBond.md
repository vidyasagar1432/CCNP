---
tags: [CCNP, glossary, wan, networking]
aliases: ["vBond", "SD-WAN Orchestration Plane", "SD-WAN Orchestrator"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Enterprise WAN
created: 2026-08-29
---

# vBond

## Definition

**vBond** is the **orchestration plane** of Cisco [[SD-WAN]] — the **"front door"** of the fabric: it **authenticates and onboards** every device ([[WAN Edge|edges]], [[vSmart|vSmarts]], [[vManage|vManages]]) that joins, hands them **certificates**, and tells each device **which controller to talk to**. Once onboarding completes, vBond is *not* in the steady-state path (config flows vManage↔edge; control vSmart↔edge) — but it must be **publicly reachable** so new edges can find the network.

## The Onboarding Flow

```text
new edge boots → finds vBond (DNS/IP) → mutual auth (ID/password, certificates)
→ vBond: "your vManage is X, your vSmart is Y" → edge joins the fabric
secure: all validation via PKI/whitelist — untrusted devices can't join
```

## Exam Focus

- **"Which SD-WAN component introduces devices to the network?" → vBond** — the definition; plane = orchestration — the plane-match question.
- **Why must vBond be reachable?** → new/roaming edges need the bootstrap — the design fact; vBond off the data path afterward — the "is vBond in the path?" trick (no).
- Placement: DMZ/public DNS — the deployment note; typically 2 for HA.
- The onboarding handshake (auth → certificate → controller assignment) — the process question.

## Related Terms

- [[SD-WAN]], [[vManage]], [[vSmart]], [[WAN Edge]]
- Level 23 notes: [[Level 23 - Enterprise WAN/10. vBond]]