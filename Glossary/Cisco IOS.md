---
tags: [CCNP, glossary, ios, networking]
aliases: ["Cisco IOS", "IOS", "Internetwork Operating System", "CLI", "Config Register"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# Cisco IOS

## Definition

**Cisco IOS (Internetwork Operating System)** is the classic network OS: a **monolithic control-plane image** with the **CLI** as its face. The CLI runs two families — **exec** (`show`, `ping`, config mode entry) and **configure** (global/interface/line submodes) — plus built-in help, **tab completion**, and `?`. The **configuration register (0x2102)** controls boot behavior and password recovery. Today IOS lives on as the **IOSd daemon inside [[IOS XE]]**.

## The CLI Mechanics

```text
user exec (>) → enable → privileged exec (#) → configure terminal → global(config)#
→ interface Gi0/0 → Gi0/0(config-if)# … hierarchy = context of your commands
no form negates; do form runs exec from config; ?/tab = help; write mem / copy run start
```

## Exam Focus

- **"What is IOS?" → the Cisco network OS (control plane image)** — vs IOS XE (Linux-based, daemons) — the architecture question.
- **Exec vs config modes / prompts**: `>` `#` `(config)#` `(config-if)#` — the prompt-recognition question.
- **Config register**: 0x2102 = normal boot, 0x2142 = ignore startup-config (password recovery) — the boot behavior fact.
- **CLI power**: `?` (context help), tab (completion), `show running-config` — the interaction basics.

## Related Terms

- [[IOS XE]], [[IOS File System]], [[IOS Upgrade]], [[ROMMON]], [[Configuration Archive]], [[SSH]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/01. CLI]], [[Level 28 - Cisco IOS and IOS XE/02. Configuration Modes]]