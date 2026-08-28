---
tags: [CCNP, glossary, ios, networking]
aliases: ["IOS File System", "Flash", "bootflash", "nvram", "IOS Filesystem Prefixes"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# IOS File System

## Definition

IOS exposes a **virtual file system**: prefixes name where things live — **flash:/bootflash:** (images — the OS storage), **nvram:** (startup-config), **system:** (running config/processes), **usbflash0:**, and **network prefixes** (**tftp:/ftp:/scp:**). Commands: `dir`, `show flash`, `copy`, `delete`, `mkdir`. Knowing the layout = image/config management fluency ([[IOS Upgrade]], [[Configuration Archive]]).

## The Prefix Map

| Prefix | Holds |
| --- | --- |
| flash: / bootflash: | IOS images, files |
| nvram: | startup-config |
| system: | running-config, RAM |
| tftp:/ftp:/scp: | remote transfer targets |
| usbflash0: | USB media |

## Exam Focus

- **"Where does the startup config live?" → nvram:**; "where are images?" → flash: — the prefix-location questions.
- **`dir` vs `show flash`** — the listing commands; `copy tftp flash` = image transfer — the file-ops recognition.
- **Copy directions**: `copy running-config startup-config` (save) vs `copy startup-config running-config` (restore) — the direction question.
- **`delete` + `squeeze`** on flash — the storage hygiene step.

## Related Terms

- [[Cisco IOS]], [[IOS Upgrade]], [[Configuration Archive]], [[ROMMON]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/05. File Systems]]