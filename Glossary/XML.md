---
tags: [CCNP, glossary, sdn, automation]
aliases: ["XML", "eXtensible Markup Language"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# XML

## Definition

**XML (eXtensible Markup Language)** is the **tag-based** data format: every value sits between an **opening and closing tag** (`<name>SW1</name>`), with **attributes** adding metadata. It's the natural format for **[[NETCONF]]** (XML RPCs) and legacy SOAP APIs; verbose but self-describing and schema-able (XSD).

## The Shape

```xml
<device>
  <name>SW1</name>
  <interfaces>
    <interface>
      <name>GigabitEthernet0/1</name>
      <status>up</status>
    </interface>
  </interfaces>
</device>
```

## Exam Focus

- **"Which protocol speaks XML?" → NETCONF** (and SOAP) — the format-protocol match; RESTCONF can too.
- **XML mechanics**: tags open/close; attributes inside the opening tag; tree hierarchy — the parse questions.
- **XML vs JSON**: verbose/typed vs compact — "why JSON won the API world?" answer (bandwidth + readability).
- Escaping entities (`&lt;` `&amp;`) — the formatting gotcha.

## Related Terms

- [[NETCONF]], [[JSON]], [[YANG]], [[YAML]]
- Level 24 notes: [[Level 24 - SDN & Automation/11. XML]]