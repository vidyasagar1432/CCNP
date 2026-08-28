---
tags: [CCNP, glossary, sdn, automation]
aliases: ["YANG", "Yet Another Next Generation", "Data Modeling Language", "RFC 6020", "RFC 7950"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# YANG

## Definition

**YANG** (RFC 6020/7950) is the **data modeling language** that describes a device's configuration and state as a **tree of containers, lists, and leafs**. It is the vocabulary both **[[NETCONF]]** and **[[RESTCONF]]** operate on: "model the interface" → YANG defines it → protocols read/write it. One model, two protocols, any vendor that implements it.

## The Model Shape

```yaml
container interfaces {
  list interface {
    key "name";
    leaf name     { type string; }
    leaf enabled  { type boolean; }
    leaf mtu      { type uint32; }
  }
}
```

## Exam Focus

- **"What is YANG?" → data modeling language (not a protocol!)** — the definition; it doesn't transport — NETCONF/RESTCONF do — the separation.
- **YANG's structure**: containers/lists/leafs — the tree terminology; keys identify list entries.
- **Standard vs vendor models**: IETF models vs Cisco native models — the interop question.
- "Which protocol reads YANG?" → NETCONF (XML) and RESTCONF (JSON/XML) both — the consumptive pairing.

## Related Terms

- [[NETCONF]], [[RESTCONF]], [[XML]], [[JSON]]
- Level 24 notes: [[Level 24 - SDN & Automation/09. YANG]]