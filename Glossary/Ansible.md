---
tags: [CCNP, glossary, sdn, automation]
aliases: ["Ansible", "Playbook", "Ansible Module", "Ansible Inventory", "Ansible Controller"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# Ansible

## Definition

**Ansible** is a **push-based, agentless** automation tool: **[[YAML]] playbooks** declare what to do, and **modules** execute it against **inventory** hosts over **SSH** (no agent to install!). For networking: **ios_command / ios_config** modules, or RESTCONF via `uri`. A control node runs them; devices just need SSH.

## The Building Blocks

```yaml
---
- name: Configure VLANs
  hosts: switches
  tasks:
    - name: Create VLAN 10
      cisco.ios.ios_vlan:
        vlan_id: 10
        name: CORP
```

## Exam Focus

- **"Which automation tool is push-based and agentless?" → Ansible** — vs agent-based (Puppet/Chef) — the model question.
- **Playbook = YAML; inventory = hosts; module = the action** — the component definitions.
- **Networking modules**: `ios_command`, `ios_config` — or how vendors plug in (collections) — the recognition.
- Push (Ansible) vs pull (Puppet/Chef) — the architecture comparison.

## Related Terms

- [[YAML]], [[Python]], [[Terraform]], [[Git]]
- Level 24 notes: [[Level 24 - SDN & Automation/14. Ansible]]