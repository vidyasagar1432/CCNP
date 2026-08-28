---
tags: [CCNP, glossary, network-services, file-transfer]
aliases: ["TFTP", "Trivial File Transfer Protocol"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# TFTP

## Definition

**TFTP (Trivial File Transfer Protocol)** is the **minimal file transfer** over **UDP 69** — no auth, no directory support, fixed 512-byte blocks with lockstep ACKs. It's the classic **IOS image/config copy** tool (`copy tftp flash:`) in labs and recovery (ROMMON) because it's dead simple — and equally insecure.

## The Trade-off

| | TFTP | [[FTP]] |
| --- | --- | --- |
| Transport | UDP 69 | TCP 21/20 |
| Auth | None | Plaintext login |
| Features | Fixed blocks, simple | Modes, directory ops |
| Use | Bootstrap/images (ROMMON!) | Interactive file needs |

```text
switch: copy tftp://10.1.99.10/switch.bin flash:
   (works in ROMMON when the OS is gone — why TFTP survives)
```

## Exam Focus

- **"Which protocol can be used in ROMMON / recovery to reload an IOS?" → TFTP (UDP 69)** — the distinguishing purpose.
- **Ports to recite**: TFTP 69 vs FTP 21/20 vs [[SSH]] 22 vs [[HTTPS]] 443 — the multi-protocol table question.
- No security: TFTP in production = warning flag (trivial = no auth, no encryption) → use SCP where possible.

## Related Terms

- [[FTP]], [[DHCP Relay]], [[HTTPS]], [[SSH]]
- Level 16 notes: [[Level 16 - Network Services/09. TFTP]]