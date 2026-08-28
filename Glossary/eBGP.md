---
tags: [CCNP, glossary, bgp, routing]
aliases: ["External BGP"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# eBGP

## Definition

**eBGP (External BGP)** peer sessions run **between routers in different autonomous systems**. It is how one AS advertises its prefixes to the Internet and how the Internet exchanges routes at large.

## eBGP vs iBGP Rules

| Rule | eBGP | iBGP |
| --- | --- | --- |
| Peer AS | Different | Same |
| TTL (default) | **1** (one hop) | 255 (multi-hop) |
| Next-hop behavior | **Changed** to the advertising router | **Preserved** (must be IGP-reachable or `next-hop-self`) |
| Advertisement of learned routes | Yes (to other ASes) | **No — split horizon** (iBGP-learned routes not re-advertised to iBGP peers) |
| Loop prevention | [[AS Path|AS_PATH]] (path length) | iBGP Split Horizon + AS_PATH (no repeats) |
| Default timers | Keepalive 60 s / hold 180 s | Same |

```cisco
router bgp 65001
 neighbor 203.0.113.2 remote-as 65002   ! eBGP peer in another AS
```

## Exam Focus

- **TTL=1 default** — eBGP peers must be directly connected (multihop requires `ebgp-multihop`).
- **Next hop changes on eBGP advertisements** — the classic "why is next hop wrong on iBGP" chain begins here.
- Requirement for adjacency includes: TCP reachability, `remote-as` match, and **no AS_PATH loop**.

## Related Terms

- [[BGP]], [[iBGP]], [[AS Path]], [[BGP Path Selection]]
- Level 12 notes: [[Level 12 - BGP/01. eBGP]]