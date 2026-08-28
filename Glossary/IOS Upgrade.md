---
tags: [CCNP, glossary, ios, networking]
aliases: ["IOS Upgrade", "Software Upgrade", "IOS Image", "Boot System", "Copy Tftp Flash", "IOS XE Upgrade"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# IOS Upgrade

## Definition

**Upgrading IOS/IOS XE** = **copy the new image to flash** (`copy tftp flash`), **make it the boot image** (`boot system flash:…` or `install` on IOS XE), **reload**, then **verify** (`show version`). Images are NOT run in-place — they're loaded at boot. IOS XE adds **SMU/install mode** (activation without touching the rest) and **ISSU** for hitless changes on dual-RP boxes.

## The Upgrade Sequence

```text
1. copy tftp://server/image.bin flash:   (or use install add file … activate commit)
2. boot system flash:image.bin  (config) or set the new package as default
3. reload → watch boot → show version (check version/features)
4. rollback = boot the old image (keep it!), or ISSU for no-downtime
```

## Exam Focus

- **"How do you upgrade IOS?" → copy image → set boot → reload → verify** — the ordered steps.
- **`boot system` importance**: without it the box boots whatever is first on flash — the "why must you point boot?" trick.
- **ISSU vs reload upgrade**: hitless vs maintenance-window — the availability contrast (see [[ISSU]]).
- IOS XE: `install add/activate/commit` bundle packaging — the modern method question.

## Related Terms

- [[IOS File System]], [[Cisco IOS]], [[ISSU]], [[Configuration Archive]], [[ROMMON]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/06. Software Upgrade]]