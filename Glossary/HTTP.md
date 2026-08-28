---
tags: [CCNP, glossary, network-services, web]
aliases: ["HTTP", "Hypertext Transfer Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# HTTP

## Definition

**HTTP (Hypertext Transfer Protocol)** is the web's request/response protocol — **TCP 80**, plaintext, stateless. In the networking world HTTP matters twice: it's the protocol of web traffic you must classify/prioritize/protect, and it's a **management channel** (HTTP-based device web UIs, REST/[[NETCONF]] over HTTP).

## The Model

```text
client → GET /path HTTP/1.1 (request: method, URL, headers)
server → 200 OK + body (status: 1xx info, 2xx ok, 3xx redirect, 4xx client, 5xx server)
stateless: each request independent (sessions via cookies)
```

## Exam Focus

- **Port 80 plaintext = the "what's insecure about HTTP?" answer** → use [[HTTPS]] (TLS = port 443).
- **Status codes**: 200 OK, 301 redirect, 404 not found, 500 server error — the recognition set.
- Cisco angle: **HTTP(S) server for web UI** (`ip http server`, `ip http secure-server`) and **RESTCONF/NETCONF run over HTTP(S)** — the [[SDN & Automation|automation]] bridge.
- QoS classification: HTTP often the default "web" class — matching by port 80/443 in [[QoS]] policies.

## Related Terms

- [[HTTPS]], [[DNS]], [[SSH]]
- Level 16 notes: [[Level 16 - Network Services/10. HTTP]]