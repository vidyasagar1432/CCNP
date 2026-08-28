---
tags: [CCNP, glossary, wireless, networking]
aliases: ["Wireless Channels", "Channels", "Channel Width", "DFS", "20 MHz", "40 MHz", "80 MHz", "160 MHz"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Wireless
created: 2026-08-29
---

# Channels

## Definition

**Channels** are the RF sub-bands APs transmit on — the spectrum slices that let neighboring APs coexist. In 2.4 GHz: channels 1–13 with only **1, 6, 11 non-overlapping** (20 MHz). In 5 GHz: many channels, wider widths (**40/80/160 MHz**), and **DFS** channels that yield to radar. Channel planning is the #1 exam "why is my Wi-Fi slow?" answer.

## The Spectrum Cheat Sheet

| Band | Channels | Widths | Gotcha |
| --- | --- | --- | --- |
| 2.4 GHz | 1–13 | 20 MHz | Only 1/6/11 don't overlap |
| 5 GHz | 36–165 | 20/40/80/160 | DFS channels = radar avoidance |
| 6 GHz (Wi-Fi 6E) | 1–233 | 20–160 | No legacy interference |

## Exam Focus

- **"Which 2.4 GHz channels don't overlap?" → 1, 6, 11** — the classic; "how many non-overlapping 2.4 GHz channels?" → 3.
- **Wider channel = more speed, less reuse** — 80/160 MHz speeds but thins the channel count — the trade-off question.
- **DFS**: radar detection → channel availability changes dynamically — the "what is DFS?" definition.
- Adjacent-AP planning: 1-6-11 reuse pattern — the "design coverage without co-channel interference" answer.

## Related Terms

- [[802.11]], [[WLAN]], [[RF]]
- Level 22 notes: [[Level 22 - Wireless/05. Channels]]