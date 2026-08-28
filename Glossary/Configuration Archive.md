---
tags: [CCNP, glossary, ios, networking]
aliases: ["Configuration Archive", "Config Backup", "Archive", "Show Archive", "Rollback Config"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Cisco IOS and IOS XE
created: 2026-08-29
---

# Configuration Archive

## Definition

**Configuration backup** protects the config by copying it to external storage (**TFTP/FTP/SCP/USB** — or a central repo like RANCID/Git) and via the IOS **archive** feature: `archive log config` keeps a **numbered rollback point of config changes** (`show archive`, `configure replace`) — instant diff-and-revert instead of guessing what changed.

## The Archive Flow

```text
backup: copy running-config tftp://… / scp / write (config files in git = history!)
archive: archive path … log config → every configure session = archive N
rollback: configure replace flash:archive-5  → reverts to that snapshot
```

## Exam Focus

- **"Which feature stores config versions on the box?" → archive (log config)** — vs external backup targets — the mechanism question.
- **`configure replace`** = roll back to an archived snapshot — the recovery command.
- **Post-upgrade/change workflow**: backup before, archive during, verify after — the ops pattern; Git = modern config-as-code history.
- `show archive` reveals the rollback list — the verification command.

## Related Terms

- [[IOS File System]], [[IOS Upgrade]], [[Git]], [[TFTP]], [[Cisco IOS]]
- Level 28 notes: [[Level 28 - Cisco IOS and IOS XE/07. Configuration Backup]]