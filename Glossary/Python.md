---
tags: [CCNP, glossary, sdn, automation]
aliases: ["Python", "Network Automation Language", "Netmiko", "NAPALM", "Requests", "Scripting"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# Python

## Definition

**Python** is the de-facto **network automation language**: scripts talk to devices via **REST APIs / RESTCONF**, CLI libraries (**Netmiko**, NAPALM), or **NETCONF**, and parse **JSON/YAML**. The exam wants basic fluency — reading output, parsing data, `requests` + `json` — not art.

## The Typical Script

```python
import requests, json
r = requests.get("https://172.16.1.10/api/device",
                 auth=("admin", "secret"), verify=False)
devices = r.json()
for d in devices:
    print(d["hostname"], d["status"])
```

## Exam Focus

- **"Which language for network automation?" → Python** — the ecosystem (requests, json, jinja2 templates, netmiko) — the tool-lists.
- **Reading code, not writing**: expect output-prediction questions (`dict get`, list indexing) — "what does this print?" scenarios.
- **JSON ↔ Python**: `json.loads()` (string→dict) vs `json.dumps()` (dict→string) — the conversion direction.
- Automation workflow: **retrieve → transform → push** (GET/parse/configure) — the pattern question.

## Related Terms

- [[REST API]], [[JSON]], [[YAML]], [[Ansible]], [[Git]]
- Level 24 notes: [[Level 24 - SDN & Automation/13. Python]]