---
tags: [CCNP, glossary, sdn, automation]
aliases: ["YAML", "YAML Ain't Markup Language", "Playbook", "HCL"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# YAML

## Definition

**YAML** ("YAML Ain't Markup Language") is the **human-friendly data format built on indentation** — no brackets or tags, just **spaces that define structure**. It's the backbone of **[[Ansible]]** (playbooks, inventory) and countless config files. Common gotcha: **tabs are illegal** — indentation must be spaces; `---` starts a document; `-` marks list items.

## The Shape

```yaml
---
switch_name: SW1
interfaces:
  - name: GigabitEthernet0/1
    status: up
  - name: GigabitEthernet0/2
    status: down
```

## Exam Focus

- **"Which format does Ansible use for playbooks?" → YAML** — the tool-format map; Terraform uses **HCL** (its own) — the contrast.
- **Indentation = structure**: consistent spaces, never tabs — the #1 YAML error question.
- `key: value`, lists with `- `, nested maps — the block recognition.
- YAML vs JSON: same data, YAML written for humans — "why YAML for configs?" answer.

## Related Terms

- [[Ansible]], [[JSON]], [[XML]], [[Terraform]], [[Python]]
- Level 24 notes: [[Level 24 - SDN & Automation/12. YAML]]