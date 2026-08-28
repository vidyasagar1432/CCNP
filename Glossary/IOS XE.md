---
tags: [CCNP, glossary, ios, networking]
aliases: ["IOS XE", "IOS-XE", "IOS XE Architecture", "IOSd", "Linux Kernel", "Cisco IOS XE"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# IOS XE

## Definition

**IOS XE** is **IOS re-architected to run on Linux**: the classic IOS control plane is now the **IOSd daemon** on a Linux kernel, with other processes (platform, routing, data) as **separate daemons** — crash isolation, easier patches (**SMUs**), and native integration with model-driven management (**[[NETCONF]]/[[RESTCONF]] + [[YANG]]**). One kernel, many processes: IOS the OS became a component.

## The Architecture

```text
Linux kernel (the host) → services/daemons:
  IOSd (control plane — the CLI/routing state you know)
  platform processes (hardware mgmt), data-plane processes
benefits: process isolation (one crash ≠ whole box), SMU hot-patches,
  modern APIs (NETCONF/RESTCONF/gNMI), container-like evolution
```

## Exam Focus

- **"What's different about IOS XE?" → IOS running as a daemon on Linux** — the architecture answer; "what is IOSd?" → the IOS control-plane process.
- **Why XE?** → modularity, crash containment, programmability (NETCONF/RESTCONF) — the value question.
- **CLI still works!** — config/commands identical to classic IOS — "does the CLI change?" → no — the continuity fact.
- Platforms: Catalyst 9000, ISR 4K, ASR 1K — "where does IOS XE run?" recognition.

## Related Terms

- [[Cisco IOS]], [[YANG]], [[NETCONF]], [[RESTCONF]], [[Smart Licensing]], [[ISSU]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/09. IOS XE Architecture (Linux-based)]]