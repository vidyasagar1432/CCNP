---
tags: [CCNP, glossary, sdn, automation]
aliases: ["REST API", "REST", "HTTP API", "Representational State Transfer", "API", "JSON API"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: SDN & Automation
created: 2026-08-29
---

# REST API

## Definition

**REST (Representational State Transfer)** is the **HTTP-based API style**: everything is a **resource with a URL**, and actions are **HTTP verbs** — **GET** (read), **POST** (create), **PUT/PATCH** (update), **DELETE** (remove). Data rides as **[[JSON]]/[[XML]]**; status comes back as HTTP codes (200 OK, 404, 500). Network devices/controllers (DNA Center, vManage, IOS-XE) expose REST APIs — the automation's "remote control".

## The Verb Map

| Verb | CRUD | Example |
| --- | --- | --- |
| GET | Read | `GET /api/devices` |
| POST | Create | `POST /api/templates` |
| PUT / PATCH | Update (replace / partial) | `PUT /api/device/1` |
| DELETE | Remove | `DELETE /api/device/1` |

## Exam Focus

- **"What are the REST verbs?" → GET/POST/PUT/PATCH/DELETE mapped to read/create/update/delete** — the table question.
- **Statelessness**: each request carries what it needs; no server session — the "what makes REST RESTful?" fact.
- **Status codes**: 2xx success, 4xx client error, 5xx server — the error-vs-reason question.
- REST vs [[NETCONF]]/[[RESTCONF]]: REST = generic HTTP resource API; RESTCONF = REST over YANG models — the tool-choice nuance.

## Related Terms

- [[JSON]], [[XML]], [[RESTCONF]], [[DNA Center]], [[Python]]
- Level 24 notes: [[Level 24 - SDN & Automation/06. REST API]]