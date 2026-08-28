---
tags: [CCNP, glossary, network-services, voip]
aliases: ["SIP", "Session Initiation Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# SIP

## Definition

**SIP (Session Initiation Protocol)** is the **signaling** protocol for VoIP/UC sessions — it sets up, modifies, and tears down calls. **UDP/TCP 5060** (5061 TLS). Signaling only: the actual voice rides [[RTP]] on separate UDP ports. A call = **SIP signaling + RTP media**, two different traffic profiles.

## The Call Setup in Brief

```text
INVITE (caller → proxy → callee) → 180/200 OK → ACK
media streams then flow directly (RTP, negotiated SDP)
BYE ends the session
proxies/registrars: location (REGISTER), routing, presence
```

## Exam Focus

- **"Which protocol sets up and tears down VoIP calls?" → SIP**; **"Which carries the actual voice?" → [[RTP]]** — the pair is quizzed as a team.
- **QoS angle**: SIP = small, delay-tolerant signaling; RTP = delay-sensitive media — different [[QoS]] treatment (marking, EF for voice payload).
- Port trivia: SIP is 5060 (and 5061 TLS); RTP is dynamic UDP (16384+ typical).
- SIP is text-based (HTTP-inspired); NAT traversal pain (SDP carries private IPs) → ALG/SBC fixes — the enterprise-Collab design wrinkle.

## Related Terms

- [[RTP]], [[QoS]], [[Voice VLAN]]
- Level 16 notes: [[Level 16 - Network Services/18. SIP]]