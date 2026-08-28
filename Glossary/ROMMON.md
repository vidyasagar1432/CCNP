---
tags: [CCNP, glossary, ios, networking]
aliases: ["ROMMON", "ROM Monitor", "Password Recovery", "Config Register", "Xmodem", "Boot Helper"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# ROMMON

## Definition

**ROMMON (ROM Monitor)** is the tiny **boot firmware** that runs before IOS: it handles **power-on self-test and image loading**, and it's the **rescue environment** — when flash is empty/corrupt you drop to `rommon 1 >` and recover via **xmodem/tftp or a USB boot helper**. The **config register** (e.g. **0x2142 = ignore startup config**) is the lever behind **password recovery** (break into ROMMON → skip config → clear secrets → restore 0x2102).

## The Recovery Path

```text
break during boot → rommon 1 >
password recovery: confreg 0x2142 → reset → boots unconfigured →
  enable → copy start run (or reset) → clear secret → confreg 0x2102 → save
image recovery: rommon → tftpdnld / xmodem new image → boot
```

## Exam Focus

- **"What is ROMMON and when do you see it?" → boot firmware/ROM monitor, on failed boot** — the definition; `rommon 1 >` prompt.
- **Config register**: **0x2102** = normal, **0x2142** = skip startup-config (password recovery) — the classic pair question.
- **Password recovery procedure**: break → confreg 2142 → reload → clear → fix registers — the ordered steps.
- **Image recovery via ROMMON**: tftp/xmodem when flash has no image — the bricked-box rescue.

## Related Terms

- [[Cisco IOS]], [[IOS File System]], [[IOS Upgrade]], [[Device Hardening]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/08. Recovery]]