---
tags: [CCNP, glossary, bgp, routing]
aliases: ["Local Preference", "LocalPref"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: BGP
created: 2026-08-29
---

# Local Preference

## Definition

**Local Preference** is the **well-known discretionary** BGP attribute that controls **outbound** traffic: it tells the **whole AS** which eBGP path is preferred. **Higher is better** — and it is the **step-2** best-path attribute (after Cisco weight).

## How It Works

```text
R1 (AS 65001) peers with ISP-A and ISP-B
   local-pref 200 to ISP-A path, 100 to ISP-B path
   → outbound traffic to that prefix prefers ISP-A (200)

applied: inbound on the eBGP session (from the neighbor)
         affects all routers in the AS (propagated via iBGP unchanged)
```

```cisco
route-map PREF-A permit 10
 set local-preference 200
router bgp 65001
 neighbor 203.0.113.1 route-map PREF-A in
```

## Exam Focus

- **Local pref = outbound decision; MED = inbound decision** — know which is which instantly.
- It is **transitive within the AS** but **not sent to other ASes** (stops at the eBGP boundary).
- Higher is better; the **default is 100**.
- Weight (step 1) is per-router and local-only; local pref is AS-wide via iBGP — a standard comparison question.

## Related Terms

- [[BGP]], [[BGP Path Selection]], [[MED]], [[eBGP]], [[iBGP]]
- Level 12 notes: [[Level 12 - BGP/05. Local Preference]]