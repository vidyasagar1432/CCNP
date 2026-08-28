---
tags: [CCNP, glossary, sdn, automation]
aliases: ["JSON", "JavaScript Object Notation"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# JSON

## Definition

**JSON (JavaScript Object Notation)** is the **lightweight data format** of REST APIs, RESTCONF, and most automation tools — built on **key-value objects `{}`, arrays `[]`, and strings/numbers/booleans** (always double-quoted). It's compact, readable, language-agnostic — and it parsed, launched, and answered a thousand network-script questions.

## The Shape

```json
{
  "switch": "SW1",
  "interfaces": [
    {"name": "GigabitEthernet0/1", "status": "up", "speed": 1000},
    {"name": "GigabitEthernet0/2", "status": "down"}
  ]
}
```

## Exam Focus

- **"In what format do REST APIs usually return data?" → JSON** — vs [[XML]] (tags) vs [[YAML]] (indentation) — the format-recognition trio.
- **JSON vocabulary**: `{}` object, `[]` array, key:value, commas; **double quotes** required — the syntax gotchas (trailing comma, unquoted keys).
- Parsing in Python: `json.loads()` / `requests.json()` — the script-pairing.
- JSON vs YAML: same concepts, YAML = friendlier (indentation, no braces) — the readability trade.

## Related Terms

- [[REST API]], [[YAML]], [[XML]], [[Python]]
- Level 24 notes: [[Level 24 - SDN & Automation/10. JSON]]