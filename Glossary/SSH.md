---
tags: [CCNP, glossary, network-services, security]
aliases: ["SSH", "Secure Shell"]
status: complete
type: glossary-term
exam: ENCOR-350-401
domain: Network Services
created: 2026-08-29
---

# SSH

## Definition

**SSH (Secure Shell)** is the encrypted **remote-access protocol** — **TCP 22** — replacing plaintext [[Telnet]] for device management. It provides authenticated, encrypted CLI sessions plus secure file transfer (SCP/SFTP). Version **v2** is the modern standard (v1 is deprecated/broken).

## The Config Essentials

```text
hostname + ip domain-name                  (needed for key generation)
crypto key generate rsa modulus 2048       (the host key)
ip ssh version 2
line vty 0 4
  transport input ssh                      ← kill telnet!
  login local                              (+ aaa for scale)
verify: show ip ssh  |  ssh -l admin 10.1.1.1
```

## Exam Focus

- **"Which protocol provides encrypted management CLI?" → SSH (TCP 22)** — versus Telnet 23 plaintext.
- **`transport input ssh`** is the hardening command — the "no exec from Telnet" answer.
- SSH needs a **host key**: generate before enabling; RSA 2048+ for ENCOR-era crypto.
- SCP rides SSH (port 22) for secure config/image copies — vs insecure [[TFTP]]/[[FTP]].
- Modern: SSH keys/certs for device auth — the "beyond passwords" mention.

## Related Terms

- [[Telnet]], [[HTTPS]], [[TFTP]], [[FTP]], [[AAA]]
- Level 16 notes: [[Level 16 - Network Services/12. SSH]]