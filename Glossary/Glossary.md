---
tags: [CCNP, glossary, MOC]
aliases: ["CCNP Glossary", "Terms Hub"]
status: complete
type: glossary-index
exam: ENCOR-350-401
created: 2026-08-29
---

# CCNP Glossary

> Robust one-note-per-term definitions for the concepts that recur throughout this vault. Each term note follows the same skeleton: **definition → how it works → example → exam focus → related terms**. Every time a term appears in the level notes it is backlinked to its definition here.

## Networking Basics (Level 00)

### Roles and Planes

- [[End Device]] — hosts that source and consume traffic
- [[Intermediary Device]] — the switches, routers, and firewalls in between
- [[Client-Server]] — the request/response model of most applications
- [[Peer-to-Peer]] — direct communication between equal nodes
- [[Data Plane]] — the forwarding path packets take through a device
- [[Control Plane]] — the protocols and logic that build the forwarding tables
- [[Management Plane]] — the administrative access to a network device

### Network Architectures

- [[LAN]] — a local area network (broadcast domain scale)
- [[MAN]] — a metropolitan area network
- [[WAN]] — a wide area network spanning sites
- [[PAN]] — a personal area network
- [[SAN]] — a storage area network
- [[Enterprise Network Architecture]] — the overall design layers of a business network
- [[Network Design Principles]] — hierarchy, modularity, and resilience in design

## Physical Layer (Level 01)

### Cabling and Media

- [[Fiber]] — optical cabling for distance and speed
- [[UTP]] — unshielded twisted-pair copper cabling
- [[Shielded Twisted Pair]] — copper cabling with shielding against EMI
- [[Connectors]] — the physical terminations (RJ45, LC/SC, etc.)
- [[Transceiver]] — the modular optics/copper interface (SFP, QSFP)
- [[Patch Panel]] — the passive patching point in structured cabling
- [[Media Conversion]] — translating between copper and fiber media

### Link Mechanics

- [[Ethernet]] — the dominant LAN framing and access standard
- [[Ethernet Standards]] — 802.3 speeds, distances, and cable types
- [[Auto-Negotiation]] — speed/duplex negotiation between link partners
- [[Duplex]] — half vs full-duplex transmission
- [[MTU]] — the maximum frame/packet size on a link
- [[Radio Frequency]] — the medium underpinning wireless transmission

## Network Topologies (Level 02)

- [[Bus Topology]] — one shared segment, all nodes attach
- [[Star Topology]] — nodes connect to a central device
- [[Ring Topology]] — nodes form a closed loop
- [[Mesh Topology]] — full or partial direct interconnects
- [[Hybrid Topology]] — a mix of the base topologies
- [[Collapsed Core]] — core and distribution collapsed into one tier
- [[Three-Tier]] — access/distribution/core hierarchy
- [[Spine-Leaf]] — the scale-out data-center fabric design
- [[Enterprise Campus]] — the campus network as a design unit

## OSI & TCP/IP (Level 03)

- [[OSI Model]] — the seven-layer reference model
- [[TCP-IP Model]] — the four-layer model of the real Internet
- [[PDU]] — the protocol data unit at each layer
- [[Encapsulation]] — wrapping data with headers/ trailers as it descends
- [[Decapsulation]] — stripping headers as data ascends

## Ethernet & Switching (Level 04)

### Forwarding

- [[Ethernet Frame]] — the L2 unit carrying source/destination MACs
- [[MAC Address]] — the burned-in L2 identity
- [[MAC Learning]] — how switches build their address tables
- [[CAM Table]] — the hardware table mapping MAC → port
- [[Flooding]] — sending unknown-unicast frames out all ports
- [[Filtering]] — deciding which frames a port forwards
- [[Forwarding]] — delivering frames to the correct egress port
- [[Broadcast Domain]] — the set of devices reaching each other via broadcast
- [[Collision Domain]] — the segment where frames can collide

### L2 Resolution and CEF

- [[ARP]] — resolving IPv4 addresses to MAC addresses
- [[Gratuitous ARP]] — unsolicited ARP for duplicate detection and failover
- [[Proxy ARP]] — answering ARP on behalf of another host
- [[CEF]] — Cisco Express Forwarding: the pre-built FIB/adjacency fast path

## IPv4 (Level 05)

### Addressing

- [[IPv4]] — the 32-bit addressing scheme of the Internet
- [[IPv4 Classes]] — the legacy classful address ranges
- [[Public IP]] — globally routable addresses
- [[Private IP]] — RFC 1918 addresses for internal use
- [[IPv4 Broadcast]] — the 255.255.255.255 / subnet-directed broadcast
- [[IPv4 Multicast]] — one-to-many delivery in the 224.0.0.0/4 range
- [[Loopback Address]] — the 127.0.0.0/8 local host identifier
- [[APIPA]] — automatic link-local addressing (169.254.0.0/16)

### Subnetting and Summarization

- [[CIDR]] — classless prefix notation (slash length)
- [[FLSM]] — fixed-length subnet masks
- [[VLSM]] — variable-length subnet masks
- [[Summarization]] — advertising many prefixes as one
- [[Supernetting]] — aggregating classful networks into a single block
- [[Route Aggregation]] — collapsing routes at area/boundary points

## IPv6 (Level 06)

### Addressing Types

- [[IPv6]] — the 128-bit next-generation protocol
- [[Global Unicast]] — the public 2000::/3 unicast range
- [[Unique Local]] — the private fc00::/7 range
- [[Link Local]] — fe80::/10 addresses for on-link communication
- [[Loopback Address|::1]] — the IPv6 local host identifier
- [[Anycast]] — one address, many devices; nearest wins
- [[IPv6 Multicast]] — ff00::/8-based group delivery

### IPv6 Operation

- [[Neighbor Discovery]] — the ICMPv6 replacement for ARP
- [[SLAAC]] — stateless address autoconfiguration
- [[ICMPv6]] — the control protocol carrying ND and errors
- [[DHCPv6]] — stateful and stateless address assignment

## VLAN Technologies (Level 07)

- [[VLAN]] — the logical segmentation of a switch into broadcast domains
- [[802.1Q]] — the tagging standard carrying VLANs over trunks
- [[Native VLAN]] — the untagged VLAN on a trunk
- [[Trunk Port]] — the link carrying multiple tagged VLANs
- [[Access Port]] — the port carrying a single untagged VLAN
- [[Voice VLAN]] — a dedicated VLAN for IP phones
- [[Private VLAN]] — isolating ports within a VLAN
- [[QinQ]] — stacking VLAN tags across provider networks
- [[DTP]] — the dynamic trunking negotiation protocol
- [[Inter-VLAN Routing]] — routing between VLANs
- [[Router-on-a-Stick]] — inter-VLAN routing over a single trunk

## STP (Level 08)

### Core STP Concept

- [[STP]] — the spanning-tree protocol that prevents loops on bridged topologies
- [[Bridge ID]] — the priority + MAC that roots the spanning tree
- [[Root Bridge]] — the elected root of the spanning tree
- [[BPDU]] — the bridge protocol data unit carrying STP state
- [[STP Path Cost]] — the link cost accumulator that drives tree computation
- [[STP Timers]] — hello, forward delay, and max age that pace convergence

### STP Roles and States

- [[STP Port Roles]] — root/designated/blocked roles assigned to each port
- [[STP Port States]] — blocking → listening → learning → forwarding lifecycle

### STP Variants

- [[RSTP]] — rapid convergence (IEEE 802.1w)
- [[PVST+]] — per-VLAN spanning tree (Cisco)
- [[MST]] — multiple spanning trees mapping VLANs to instances

### STP Protection

- [[PortFast]] — skip the blocking/learning delays on access ports
- [[BPDU Guard]] — shut down ports that receive unexpected BPDUs
- [[BPDU Filter]] — suppress BPDU transmission/reception on a port
- [[Root Guard]] — prevent a rogue switch from becoming root
- [[Loop Guard]] — protect against unidirectional link failures

## Routing Fundamentals (Level 09)

- [[Routing Table]] — the router's map of known networks
- [[RIB]] — the routing information base (control plane)
- [[FIB]] — the forwarding information base (hardware fast path)
- [[Recursive Lookup]] — resolving a next-hop that needs its own route
- [[Static Routing]] — manually configured paths
- [[Default Route]] — the 0.0.0.0/0 catch-all
- [[Floating Static]] — a backup route with a higher AD
- [[Dynamic Routing]] — protocols that learn routes automatically
- [[Administrative Distance]] — the trust ranking between route sources
- [[Metrics]] — comparable costs within one protocol

## OSPF (Level 10)

### Core OSPF Concept

- [[OSPF]] — the open-standard link-state IGP
- [[OSPF Router ID]] — the 32-bit identity in every LSA and election
- [[Link State Database]] — the identical per-area topology map
- [[LSA]] — the advertisement types that build the LSDB
- [[OSPF Cost]] — the bandwidth-based metric
- [[SPF Algorithm]] — Dijkstra's computation over the LSDB

### OSPF Operation

- [[OSPF Neighbor States]] — Down → Init → 2-Way → ExStart → Exchange → Loading → Full
- [[DR BDR|DR/BDR]] — election that trims adjacencies on multi-access segments
- [[OSPFv3]] — OSPF for IPv6 (link-local adjacencies, IPsec auth)

### OSPF Areas

- [[OSPF Area]] — scaling via backbone + non-backbone areas
- [[ABR]] — the area border router generating Type-3 summaries
- [[ASBR]] — the router redistributing external routes (Type 5/7)
- [[Stub Area]] — blocks external Type-5 LSAs, gets a default route
- [[Totally Stubby Area]] — stub + no inter-area summaries
- [[NSSA]] — stub-like area that still imports external routes via Type 7
- [[Virtual Link]] — logical tunnel patching backbone connectivity

### OSPF Security

- [[OSPF Authentication]] — MD5/HMAC protection of OSPF packets

## EIGRP (Level 11)

### Core EIGRP Concept

- [[EIGRP]] — the Cisco-proprietary hybrid distance-vector IGP
- [[DUAL]] — the diffusing update algorithm for loop-free convergence
- [[RTP]] — the reliable transport protocol EIGRP uses
- [[EIGRP Metric]] — the composite bandwidth + delay metric

### EIGRP Paths

- [[Successor]] — the best path installed in the routing table
- [[Feasible Successor]] — a loop-free backup in the topology table
- [[Feasibility Condition]] — the RD < FD rule that proves loop-freedom
- [[Variance]] — the multiplier enabling unequal-cost load balancing
- [[Unequal-Cost Load Balancing]] — splitting traffic over unequal paths

### EIGRP Configuration

- [[Named Mode EIGRP]] — the modern single-process IPv4+IPv6 config model
- [[EIGRP for IPv6]] — the same engine over IPv6 (no `network`, manual RID)
- [[EIGRP Stub]] — spoke-router query isolation
- [[EIGRP Authentication]] — MD5/SHA-256 protection of EIGRP packets

## BGP (Level 12)

### Core BGP Concept

- [[BGP]] — the path-vector protocol of the Internet (TCP port 179)
- [[eBGP]] — sessions between different ASes (TTL 1, next hop changes)
- [[iBGP]] — sessions within one AS (split horizon, full mesh)
- [[BGP Path Selection]] — the deterministic best-path decision process

### BGP Attributes

- [[AS Path]] — AS sequence for loop prevention and path length
- [[Local Preference]] — AS-wide outbound path preference (higher better)
- [[MED]] — inbound exit-point preference (lower better)
- [[Communities]] — transitive tags for remote policy application

### BGP Scaling

- [[Route Reflector]] — hub that re-advertises iBGP routes
- [[Confederation]] — eBGP-style peering between sub-ASes
- [[BGP Aggregation]] — summarizing more specifics into one prefix

## Routing Policies (Levels 12–13)

- [[Policy-Based Routing]] — forwarding based on policy instead of the RIB
- [[Prefix List]] — ge/le prefix-length matching for route filtering
- [[Route Map]] — the general match/set policy engine

## Route Redistribution (Level 13)

- [[Route Redistribution]] — importing routes between protocols
- [[Seed Metric]] — the default metric a redistributed route inherits
- [[Route Tag]] — the marker for loop prevention and selective filters
- [[Route Filtering]] — controlling what redistribution advertises
- [[Routing Loop]] — the ping-pong of misredistributed routes

## First Hop Redundancy (Level 14)

- [[First Hop Redundancy Protocol]] — the family of default-gateway HA protocols
- [[HSRP]] — Cisco's active/standby gateway protocol
- [[VRRP]] — the open-standard gateway redundancy protocol
- [[GLBP]] — Cisco's active/active gateway load-balancing protocol
- [[Object Tracking]] — tying failover to interface/route state

## NAT (Level 15)

### Core NAT Concept

- [[NAT]] — network address translation: rewriting addresses as packets cross a boundary
- [[Inside Local Address]] — the inside host's address as seen on the inside network
- [[Inside Global Address]] — the inside host's address as represented on the outside
- [[Outside Local Address]] — the outside host's address as represented to the inside
- [[Outside Global Address]] — the outside host's address as it truly exists on the outside

### NAT Types

- [[Static NAT]] — permanent one-to-one inside local ↔ inside global mapping
- [[Dynamic NAT]] — temporary one-to-one mapping allocated from a pool
- [[PAT]] — many inside hosts share one global address via Layer-4 ports
- [[NAT Overload]] — the keyword/behavior enabling PAT with a pool or interface
- [[Outside Source NAT]] — translating addresses that belong to the outside network
- [[Policy NAT]] — conditional NAT based on source + destination / protocol / port

### NAT Mechanics

- [[NAT Pool]] — the range of inside-global addresses a dynamic rule can allocate
- [[NAT Translation Table]] — the state that ties inside ↔ outside mappings together
- [[NAT Timers]] — how long translations live before aging out
- [[NAT ACL]] — the access-list used for NAT *classification*, not security
- [[NAT ALG]] — application-layer awareness for protocols that carry addresses in payloads

### IPv6 Transition

- [[NAT64]] — IPv6 ↔ IPv4 translation (stateful / stateless)
- [[DNS64]] — synthesizes AAAA records so IPv6-only clients can reach IPv4 servers

## Network Services (Level 16)

### Name and Address Services

- [[DHCP]] — dynamic address assignment (DORA)
- [[DHCP Relay]] — forwarding DHCP broadcasts across subnets
- [[DHCP Snooping]] — the L2 security feature validating DHCP trust
- [[DNS]] — name-to-address resolution

### Applications and Management

- [[HTTP]] — the web transfer protocol
- [[HTTPS]] — HTTP over TLS
- [[FTP]] — plaintext file transfer
- [[TFTP]] — trivial file transfer (config/images)
- [[SMTP]] — email submission/relay
- [[POP3]] — email retrieval (download)
- [[IMAP]] — email retrieval (server-side folders)
- [[LDAP]] — directory access for authentication/attributes
- [[SIP]] — session initiation for voice/video
- [[RTP]] — real-time transport of media payloads
- [[NTP]] — network time synchronization

### Device Management and Monitoring

- [[Telnet]] — unencrypted remote CLI access (port 23)
- [[SSH]] — encrypted remote CLI access (port 22)
- [[SNMP]] — polling/trap-based monitoring (port 161/162)
- [[Syslog]] — the syslog logging facility for device events

## Security (Level 17)

### Access Control and AAA

- [[ACL]] — the classic permit/deny filter
- [[AAA]] — authentication, authorization, accounting
- [[RADIUS]] — the UDP-based AAA protocol
- [[TACACS+]] — the TCP-based Cisco AAA protocol

### Switch Security

- [[Port Security]] — locking MAC addresses to ports
- [[DHCP Snooping]] — validating DHCP trust at L2
- [[Dynamic ARP Inspection]] — ARP packet validation
- [[IP Source Guard]] — binding IPs to ports
- [[Storm Control]] — limiting broadcast/multicast/unicast floods

### Device and Control-Plane Protection

- [[Device Hardening]] — lockdown of the device itself
- [[CoPP]] — control-plane policing of traffic to the CPU

## VPN Technologies (Level 18)

### VPN Foundations

- [[VPN]] — encrypted/private connectivity over shared networks
- [[GRE]] — the generic routing encapsulation tunnel
- [[IPsec]] — the suite securing IP traffic (AH/ESP, IKE)
- [[IKEv2]] — the modern key-exchange protocol for IPsec
- [[Virtual Tunnel Interface]] — logical tunnel endpoints for encryption

### VPN Deployments

- [[Site-to-Site VPN]] — branch-to-HQ encrypted links
- [[Remote Access VPN]] — teleworker connectivity to the enterprise
- [[SSL VPN]] — browser/portal-based remote access
- [[DMVPN]] — dynamic hub-and-spoke overlay tunnels
- [[FlexVPN]] — the unified IKEv2-based VPN framework
- [[GET VPN]] — group encryption for MPLS/any-to-any networks

## Multicast (Level 19)

### Multicast Foundations

- [[Multicast]] — one-to-many/demand delivery to groups
- [[IGMP]] — host-to-router group membership signaling
- [[IGMP Snooping]] — switches learning group membership
- [[Source-Specific Multicast]] — (S,G) scoped multicast delivery

### Multicast Routing

- [[PIM]] — the protocol-independent multicast routing family
- [[PIM-DM]] — flood-and-prune dense-mode operation
- [[PIM-SM]] — pull-based sparse-mode with a rendezvous point
- [[Rendezvous Point]] — the meeting point for sources and receivers
- [[PIM DR]] — the designated router for LAN delivery
- [[Reverse Path Forwarding]] — the loop-prevention check for multicast

## MPLS (Level 20)

### MPLS Core

- [[MPLS]] — label-switched forwarding between edge devices
- [[MPLS Label]] — the 20-bit forwarding tag
- [[FEC]] — the forwarding equivalence class mapped to a label
- [[LER]] — the label edge router (ingress/egress)
- [[LSR]] — the label switch router in the core
- [[LFIB]] — the label forwarding table

### MPLS VPNs

- [[VRF]] — per-customer routing tables on the PE
- [[MP-BGP]] — BGP carrying VPNv4 routes and labels
- [[MPLS VPN]] — L3VPN service over the MPLS core

## QoS (Level 21)

### Classification and Marking

- [[QoS]] — the toolkit for managing delay, jitter, and loss
- [[QoS Classification]] — matching traffic into classes
- [[QoS Marking]] — setting DSCP/CoS/EXP values
- [[DSCP]] — the 6-bit differentiated services code point
- [[DiffServ]] — the per-hop-behavior QoS model
- [[IntServ]] — the signal-every-hop RSVP-based model
- [[Trust Boundary]] — where marking is accepted from

### Rate Control and Scheduling

- [[Policing]] — dropping/remarking excess traffic
- [[Shaping]] — buffering excess traffic to a rate
- [[Queuing]] — scheduling classes through an interface
- [[MQC]] — the modular QoS CLI (class-map/policy-map)
- [[CBWFQ]] — per-class weighted fair queuing
- [[LLQ]] — strict priority for voice/video in CBWFQ
- [[WRED]] — congestion avoidance via probabilistic drop

## Wireless (Level 22)

- [[WLAN]] — the wireless LAN itself
- [[802.11]] — the WLAN standards family
- [[SSID]] — the wireless network name
- [[BSSID]] — the AP's radio MAC identity
- [[Channels]] — frequency segments within the RF band
- [[RF]] — the radio-frequency transport medium
- [[WLC]] — the wireless LAN controller
- [[CAPWAP]] — the AP-to-controller tunnel protocol
- [[Mobility]] — roaming support across APs/controllers
- [[Roaming]] — client movement between access points
- [[WPA2]] — the 802.11i security standard (AES-CCMP)
- [[WPA3]] — the modern WPA standard (SAE handshake)

## Enterprise WAN (Level 23)

### Transport Technologies

- [[PPP]] — the point-to-point WAN link protocol
- [[PPPoE]] — PPP over Ethernet (broadband)
- [[Metro Ethernet]] — carrier Ethernet WAN services
- [[MPLS WAN]] — provider MPLS VPN WAN connectivity
- [[Broadband]] — DSL/cable/fiber subscriber access
- [[LTE]] — cellular WAN backup/primary links

### SD-WAN

- [[SD-WAN]] — the software-defined WAN architecture
- [[vManage]] — the SD-WAN management dashboard
- [[vSmart]] — the SD-WAN control/route engine
- [[vBond]] — the SD-WAN orchestrator/authentication
- [[WAN Edge]] — the SD-WAN data-plane device at sites

## SDN & Automation (Level 24)

### SDN Architectures

- [[SDN]] — programmable, centralized network control
- [[DNA Center]] — Cisco's intent-based campus controller
- [[SD-Access]] — the DNA Center fabric architecture
- [[VXLAN]] — the overlay encapsulation for fabrics
- [[LISP]] — location/identity separation for host mobility

### Programmable Interfaces

- [[REST API]] — HTTP-based programmatic access
- [[RESTCONF]] — REST-style NETCONF data access
- [[NETCONF]] — the XML-based device configuration protocol
- [[YANG]] — the data-modeling language for device state

### Data Formats

- [[JSON]] — the lightweight data interchange format
- [[XML]] — the extensible markup language
- [[YAML]] — the human-friendly data serialization format

### Automation Tooling

- [[Python]] — the scripting language of network automation
- [[Ansible]] — the agentless configuration tool
- [[Terraform]] — the infrastructure-as-code provisioner
- [[Git]] — the version-control system for config-as-code

## Virtualization & Cloud (Level 25)

### Virtualization

- [[Virtual Machine]] — a full OS on a hypervisor
- [[Hypervisor]] — the virtualization layer (Type 1/2)
- [[Container]] — OS-level lightweight packaging
- [[Docker]] — the container runtime/engine
- [[Kubernetes]] — container orchestration at scale

### Cloud Models

- [[Public Cloud]] — shared multi-tenant provider infrastructure
- [[Private Cloud]] — dedicated single-tenant infrastructure
- [[Hybrid Cloud]] — the blend of private + public
- [[IaaS]] — infrastructure as a service (VMs, storage)
- [[PaaS]] — platform as a service (managed middleware)
- [[SaaS]] — software as a service (managed applications)

## Monitoring & Telemetry (Level 26)

- [[NetFlow]] — flow-based traffic accounting (IPFIX precursor)
- [[Flexible NetFlow]] — extensible flow records and caching
- [[SPAN]] — port mirroring to a local analyzer
- [[ERSPAN]] — remote encapsulated port mirroring
- [[IP SLA]] — active service-level measurements
- [[Telemetry]] — model-driven streaming device data
- [[Wireshark]] — the packet-capture analysis tool

## High Availability (Level 27)

- [[High Availability]] — the design goal of zero/minimal downtime
- [[SSO]] — stateful switchover of the active supervisor
- [[NSF]] — nonstop forwarding so peers keep routing during failover
- [[Redundant Supervisors]] — dual control engines in a chassis
- [[ISSU]] — in-service software upgrades
- [[Virtual Switching System]] — two chassis in one logical switch
- [[EtherChannel]] — link aggregation that STP treats as one logical link

## Cisco IOS and IOS XE (Level 28)

- [[Cisco IOS]] — the classic Cisco operating system (CLI, config)
- [[IOS XE]] — IOS re-architected as daemons on Linux
- [[Cisco Licensing]] — the entitlement model for feature levels
- [[Smart Licensing]] — portal-based license management
- [[IOS File System]] — the virtual file system (flash:, nvram:, tftp:)
- [[IOS Upgrade]] — the image copy → set boot → reload workflow
- [[Configuration Archive]] — config versioning and rollback
- [[ROMMON]] — the boot firmware/rescue environment
- [[ISSU|ISSU (IOS)]] — in-service software upgrade (see High Availability)

## Troubleshooting (Level 29)

- [[Troubleshooting]] — the systematic method for network fault isolation

## Labs (Level 30)

- [[Network Simulator]] — the lab platforms (PT, CML, GNS3, EVE-NG)

## Related

- [[00. MOC - CCNP Study Map]] — the master study map
- [[Networking Basics Overview]] — Level 00 index
- [[Physical Layer Overview]] — Level 01 index
- [[Network Topologies Overview]] — Level 02 index
- [[OSI & TCP IP Overview]] — Level 03 index
- [[Ethernet & Switching Overview]] — Level 04 index
- [[IPv4 Overview]] — Level 05 index
- [[IPv6 Overview]] — Level 06 index
- [[VLAN Technologies Overview]] — Level 07 index
- [[STP Overview]] — Level 08 index
- [[Routing Fundamentals Overview]] — Level 09 index
- [[OSPF Overview]] — Level 10 index
- [[EIGRP Overview]] — Level 11 index
- [[BGP Overview]] — Level 12 index
- [[Route Redistribution Overview]] — Level 13 index
- [[First Hop Redundancy Overview]] — Level 14 index
- [[NAT Overview]] — Level 15 index
- [[Network Services Overview]] — Level 16 index
- [[Security Overview]] — Level 17 index
- [[VPN Technologies Overview]] — Level 18 index
- [[Multicast Overview]] — Level 19 index
- [[MPLS Overview]] — Level 20 index
- [[QoS Overview]] — Level 21 index
- [[Wireless Overview]] — Level 22 index
- [[Enterprise WAN Overview]] — Level 23 index
- [[SDN & Automation Overview]] — Level 24 index
- [[Virtualization & Cloud Overview]] — Level 25 index
- [[Monitoring & Telemetry Overview]] — Level 26 index
- [[High Availability Overview]] — Level 27 index
- [[Cisco IOS and IOS XE Overview]] — Level 28 index
- [[Troubleshooting Overview]] — Level 29 index
- [[Labs Overview]] — Level 30 index