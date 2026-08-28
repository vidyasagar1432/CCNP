---
tags: [CCNP, glossary, fundamentals, networking]
aliases: ["Management-Plane"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Networking Basics
created: 2026-08-29
---

# Management Plane

## Definition

The **management plane** is what operators use to **configure, monitor, and administer** network devices — over SSH/HTTPS, the console, SNMP, **[[NETCONF]]/RESTCONF**, and **gRPC telemetry**. It is the plane of *human and automation access* — separate from both [[Data Plane|data]] and [[Control Plane|control]] work.

## How It Works

```text
administrator / automation ──SSH / NETCONF / SNMP──► device
        │                  management plane access
        ▼
  config changes → pushed to control/data plane behavior
```

| Plane | What you do through it |
| --- | --- |
| Management | SSH, CLI, SNMP polling, telemetry subscriptions |
| Control | Route protocols, [[STP]] decisions |
| Data | Forwarding |

## Security Angle

- A device's **control plane is often protected from the Internet** (control-plane policing); management is protected by **copp/ACLs, AAA, and encrypted protocols**.
- Breaches via weak management (Telnet, default creds) are a classic attack story — see [[AAA]] and [[SSH]].

## Exam Focus

- **"What plane does SNMP/NETCONF/SSH touch?"** → management plane — the sure-answer question.
- Modern automation ([[Ansible]], NETCONF, telemetry) is *all* management-plane activity.
- SDN separates the *control* plane; automation reaches the *management* plane — keep the two stories straight.

## Related Terms

- [[Data Plane]], [[Control Plane]], [[Intermediary Device]], [[NETCONF]]
- Level 00 notes: [[Level 00 - Networking Basics/05. Network Components]]