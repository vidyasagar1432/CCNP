---
tags: [CCNP, glossary, sdn, automation]
aliases: ["Terraform", "Infrastructure as Code", "IaC", "Terraform Plan", "Terraform Apply", "HCL"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# Terraform

## Definition

**Terraform** is **Infrastructure as Code (IaC)**: you **declare desired state** in **HCL** (HashiCorp Configuration Language) files and Terraform **plans then applies** the diff against **providers** (cloud — AWS/Azure — and increasingly network devices/controllers). Unlike Ansible's imperative steps, Terraform is **declarative**: it figures out the "how" and tracks state.

## The Flow

```text
main.tf (HCL: resources = desired state) → terraform init → plan
→ terraform apply (creates/changes only what differs) → state file
destroy: remove everything tracked — full lifecycle, not just config
```

## Exam Focus

- **"Which tool is declarative IaC?" → Terraform** (vs Ansible's imperative playbooks) — the core contrast.
- **HCL** is its language; **providers** plug into platforms; **state** tracks reality — the keyword set.
- **Plan vs Apply**: preview the diff vs execute it — the workflow steps.
- Terraform for networks: cloud networking, then network controllers — the growing use case.

## Related Terms

- [[Ansible]], [[YAML]], [[Git]]
- Level 24 notes: [[Level 24 - SDN & Automation/15. Terraform]]