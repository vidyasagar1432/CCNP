---
tags: [CCNP, glossary, sdn, automation]
aliases: ["Git", "Version Control", "Repository", "Commit", "Branch", "GitHub"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# Git

## Definition

**Git** is a **distributed version control system** (Linus Torvalds, 2005): it tracks changes to files — configs, scripts, playbooks — with **commits**, **branches**, and **rollback**. For network engineers: the backbone of **"config as code"**, enabling review, history, and instant revert of device configurations and automation artifacts.

## The Git Flow

```text
git init/clone → working tree edits → git add (stage) → git commit (snapshot)
branches: parallel lines of work → merge/PR when ready
git log / git diff: history & changes; git revert: rollback
remote: GitHub/GitLab — push/pull, collaboration, CI/CD hooks
```

## Exam Focus

- **"Which tool tracks configuration changes with history?" → Git** — vs TFTP backups (no history) — the modern answer.
- **The three states**: working → staged → committed — the workflow stage question.
- **Basics to recognize**: commit, branch, merge, clone, push/pull, diff/log — the command-vocab.
- Why git for network: review before applying (change mgmt), rollback, audit trail — "the value of version control" answer.

## Related Terms

- [[Python]], [[Ansible]], [[Terraform]]
- Level 24 notes: [[Level 24 - SDN & Automation/16. Git]]