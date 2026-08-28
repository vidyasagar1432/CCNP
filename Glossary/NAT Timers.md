---
tags: [CCNP, glossary, nat]
aliases: ["NAT translation timeout", "Translation aging", "NAT timers"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: NAT
created: 2026-08-29
---

# NAT Timers

## Definition

**NAT timers** control how long dynamic translations remain in the [[NAT Translation Table]] before they **age out** and their resources (pool address / port) are released.

## Typical IOS Defaults

| Timer | Typical default |
| --- | --: |
| General NAT translation timeout | 24 hours |
| TCP translation timeout | 24 hours |
| UDP translation timeout | 5 minutes |

Configure / inspect:

```cisco
ip nat translation timeout <seconds>
show running-config | include ip nat translation
```

## How It Works

```text
Translation created (traffic)
        ↓
idle … idle…
        ↓
timer expires
        ↓
entry removed → pool address / port freed
```

- After expiry, a dynamic pool address returns to the [[NAT Pool]] and can be allocated to another host.
- Static NAT entries do **not** age out (permanent by design).

## Exam Focus

- **Do not memorize timer values as universal constants** — they vary by IOS/IOS XE platform and release. For CCNP, understand the *concept*: dynamic translations are temporary and age out.
- A translation that "disappears" mid-session is often just the timeout expiring — the troubleshooting note treats this separately from rule/ACL failures.

## Related Terms

- [[NAT Translation Table]], [[Dynamic NAT]], [[NAT Pool]], [[PAT]]
- Level 15 notes: [[Level 15 - NAT/02. Dynamic NAT]], [[Level 15 - NAT/06. Troubleshooting]]