---
tags: [CCNP, glossary, qos, networking]
aliases: ["QoS Classification", "Classification", "Classifying Traffic", "QoS Class"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: QoS
created: 2026-08-29
---

# QoS Classification

## Definition

**Classification** is the QoS act of **sorting traffic into classes** so each class can get its own treatment. It matches on **existing fields** — [[DSCP]], IP precedence, **802.1p CoS**, source/destination, protocol/port, or even NBAR application signatures. Classification **reads**; [[QoS Marking|marking]] **writes**. In [[MQC]] terms: the class-map's match statements.

## What Can We Match?

| Classifier | Field / Method |
| --- | --- |
| L3 | DSCP / IP precedence / source-dest IP (ACL match) |
| L4 | Protocol + port (e.g. VoIP = UDP 16384–32767) |
| L2 | 802.1p CoS bits |
| Application | NBAR deep packet inspection |

## Exam Focus

- **"Which QoS step decides what class traffic belongs to?" → classification** — the definition; classification happens **at/before marking** (trust boundary).
- **Classification vs marking**: classify = read; mark = write — the eternal pairing question.
- The **first device** should classify as close to the source as possible — "where should classification occur?" → ingress edge.
- One class-map matching many fields (match any vs match all) — the MQC subtlety.

## Related Terms

- [[QoS Marking]], [[DSCP]], [[MQC]], [[Trust Boundary]], [[ACL]]
- Level 21 notes: [[Level 21 - QoS/01. Classification]]