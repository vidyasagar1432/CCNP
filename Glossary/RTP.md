---
tags: [CCNP, glossary, network-services, voip]
aliases: ["RTP", "Real-Time Transport Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# RTP

## Definition

**RTP (Real-Time Transport Protocol)** carries the **actual media** (voice/video) in VoIP — **UDP**, real-time, with sequence numbers and timestamps but **no retransmission** (too late = useless). The voice payload of a call flies over RTP while [[SIP]] does the signaling.

## Why UDP and No Retransmits

```text
voice tolerance: a lost 20 ms packet > retransmission delay
RTP headers: sequence (order/reordering detection), timestamp (playback timing)
codecs: G.711 (64 kbps, PCM), G.729 (8 kbps) — bandwidth per flow varies!
RTP Control: RTCP — quality stats (jitter, loss) out-of-band
```

## Exam Focus

- **"Which protocol transports actual voice data?" → RTP** — and the "why not TCP?" answer is real-time UDP + no retransmission.
- **Codec bandwidth math** is an ENCOR-friendly question: G.711 ~= 80 kbps total on the wire with IP+UDP+RTP headers (64 kbps payload + overhead) — the "how much bandwidth does one call use?" exercise.
- **[[QoS]] marking**: voice bearer traffic = EF (46); call signaling = CS3 (SIP); per-hop behavior questions.
- Jitter/loss metrics (RTCP) feed monitoring — the telemetry tie-in.

## Related Terms

- [[SIP]], [[QoS]], [[Voice VLAN]]
- Level 16 notes: [[Level 16 - Network Services/19. RTP]]