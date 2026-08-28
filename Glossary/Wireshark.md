---
tags: [CCNP, glossary, monitoring, telemetry]
aliases: ["Wireshark", "Packet Analyzer", "tcpdump", "pcap", "BPF Filter", "Display Filter"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Monitoring & Telemetry
created: 2026-08-29
---

# Wireshark

## Definition

**Wireshark** is the industry-standard **packet analyzer**: it **captures, decodes, and filters** traffic for troubleshooting (alongside the CLI **tcpdump**). It reads **pcap/pcapng** captures (from itself, a **[[SPAN]]** port, or a remote box via SSH), decodes hundreds of protocols, and answers "what exactly did the device send?"

## The Skills That Matter

```text
capture source: SPAN/ERSPAN port, tcpdump file, or live interface
capture filters (BPF): tcp port 443 → only HTTPS handshake
display filters: ip.src == 10.1.1.1 && dns → show DNS from that host
follow stream: reconstruct a TCP conversation (the smoking gun)
```

## Exam Focus

- **"Which tool shows packet-level detail?" → Wireshark** — the definition; exports pcap; CLI twin tcpdump — the pair.
- **Capture (BPF) vs display filters**: what gets stored vs what gets shown — the filter-type distinction.
- **Follow TCP/UDP stream** — the rebuilt-conversation answer; packet timestamps/checksums — the decode facts.
- Network visibility stack: NetFlow (what conversations), Telemetry (state), Wireshark (content) — the tool roles.

## Related Terms

- [[SPAN]], [[ERSPAN]], [[NetFlow]], [[Telemetry]]
- Level 26 notes: [[Level 26 - Monitoring & Telemetry/09. Wireshark]]