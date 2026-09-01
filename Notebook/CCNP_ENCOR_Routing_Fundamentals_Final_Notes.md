# Routing Fundamentals — CCNP ENCOR Final Notes

Routing is the process of moving an IP packet from one network to another by selecting a next hop and an outgoing interface.

Think of a router as a postal sorting facility:

- **IP packet** = the letter
- **Destination IP address** = the address on the envelope
- **Routing table / RIB** = the master directory
- **FIB** = the fast forwarding directory
- **Next hop** = the next postal facility
- **Outgoing interface** = the road used to leave the facility

The single most important distinction to remember is:

> **Routing protocols build the map. The forwarding plane uses the map.**

---

# Part 1: The Big Picture — How Routing Works

When a host wants to communicate with a destination on another IP network, it normally sends the frame to its **default gateway**.

The router then:

1. Receives the Layer 2 frame.
2. Removes the incoming Layer 2 header.
3. Reads the destination IP address in the Layer 3 packet.
4. Performs a forwarding lookup.
5. Selects the best matching route.
6. Determines the next hop and outgoing interface.
7. Re-encapsulates the packet in a new Layer 2 frame.
8. Forwards the frame toward the next hop.

A router does **not** normally forward an unknown destination by flooding it like a switch.

If there is no matching route and no usable default route:

> **The packet is dropped.**

---

# Part 2: Control Plane vs. Data Plane

This distinction is fundamental to understanding Cisco routing.

## The Control Plane — "Thinking"

The control plane learns about the network and decides which routes should be considered best.

It is responsible for:

- Connected routes
- Static routes
- OSPF
- EIGRP
- BGP
- Routing-protocol neighbor relationships
- Route calculations
- RIB construction
- Programming forwarding information toward the data plane

Think:

> **Control plane = learn, calculate, decide.**

## The Data Plane — "Doing"

The data plane forwards actual user packets.

It uses optimized forwarding information such as:

- FIB
- Adjacency information
- Hardware forwarding tables on supported platforms

Think:

> **Data plane = lookup, rewrite, forward.**

### The Golden Rule

**AD and routing-protocol metrics are control-plane concepts.**

Once the active route has been selected and programmed into the forwarding plane, an individual packet is not asking:

> "Should I use OSPF or EIGRP?"

It is effectively asking:

> "Which forwarding entry is the best match for my destination IP?"

---

# Part 3: RIB — Routing Information Base

The **RIB** is the router's master routing database.

It is commonly represented by:

```text
show ip route
show ipv6 route
```

The RIB is built from multiple sources:

- Connected routes
- Static routes
- Dynamic routing protocols
- Other route sources supported by the platform

The RIB contains information such as:

- Destination prefix
- Prefix length
- Route source
- Administrative distance
- Metric
- Next hop
- Outgoing interface

The RIB is optimized for **route selection**, not for performing millions of packet lookups directly.

---

# Part 4: Administrative Distance — "Who Do I Trust?"

**Administrative Distance (AD)** measures how trustworthy a route source is relative to other route sources.

> **Lower AD = preferred route source**

Common Cisco default values to memorize:

| Route Source | Default AD |
|---|---:|
| Connected | 0 |
| Static | 1 |
| EIGRP Internal | 90 |
| OSPF | 110 |
| RIP | 120 |
| EIGRP External | 170 |
| Unknown / unusable | 255 |

An AD of **255** means the route is considered unreachable and is not installed.

## Example

Suppose R1 learns:

```text
10.10.10.0/24 via EIGRP
10.10.10.0/24 via OSPF
```

Both routes describe the same prefix.

- EIGRP AD = 90
- OSPF AD = 110

Therefore:

> **EIGRP wins the route-source competition.**

The OSPF route can remain known to the routing process, but it does not become the active route while the better source is available.

---

# Part 5: Metric — "Which Path Is Better Within the Protocol?"

AD answers:

> **Which routing source do I trust?**

Metric answers:

> **Which path does this routing protocol prefer?**

If multiple paths to the same destination are learned through the same routing protocol, that protocol uses its own metric.

Examples:

### RIP

Uses **hop count**.

Fewer hops are preferred.

### OSPF

Uses **cost**.

Lower total cost is preferred.

### EIGRP

Uses a composite metric.

By default, the important components are:

- Bandwidth
- Delay

Lower metric is preferred.

## Important Sequence

For a simplified exam mental model:

```text
Different route sources
        ↓
Administrative Distance
        ↓
Best route source
        ↓
Same protocol / competing paths
        ↓
Protocol metric
        ↓
Best path(s)
```

Do not confuse AD with metric.

---

# Part 6: Longest Prefix Match — "Most Specific Route Wins"

Once forwarding occurs, the most important rule is:

> **Longest Prefix Match (LPM)**

The larger the prefix length, the more specific the route.

For example:

```text
10.0.0.0/8
10.1.0.0/16
10.1.1.0/24
10.1.1.128/25
```

A destination of:

```text
10.1.1.200
```

matches all of these routes, but `/25` is the longest prefix.

Therefore:

> **10.1.1.128/25 wins.**

## Another Example

Routing table:

```text
10.0.3.0/24
10.0.3.0/26
10.0.3.0/28
```

Destination:

```text
10.0.3.14
```

Matches:

- `/24`
- `/26`
- `/28`

Winner:

```text
10.0.3.0/28
```

Destination:

```text
10.0.3.42
```

Matches:

- `/24`
- `/26`

But not `/28`.

Winner:

```text
10.0.3.0/26
```

## The Critical Distinction

Do not say:

> "The router always chooses the route with the lowest AD."

That is incomplete.

A better mental model is:

> **Forwarding first identifies the most specific applicable prefix. Route selection determines which route is installed for a given prefix.**

---

# Part 7: RIB vs. FIB

## RIB — The Master Map

The RIB answers:

> "What routes do I know, and which route is the best route for each destination prefix?"

It is primarily a control-plane construct.

## FIB — The Fast Forwarding Map

The **Forwarding Information Base (FIB)** is derived from the active routing information and is optimized for packet forwarding.

Think:

```text
RIB
 |
 | selected forwarding information
 v
FIB
 |
 | next-hop resolution / adjacency
 v
Forward packet
```

The FIB is concerned with forwarding information rather than the full history of how a route was learned.

### Exam Mental Model

```text
RIB = routing decisions
FIB = forwarding decisions
```

---

# Part 8: CEF — Cisco Express Forwarding

**Cisco Express Forwarding (CEF)** is Cisco's primary high-performance forwarding architecture.

CEF uses:

- **FIB**
- **Adjacency information**

The major idea is:

> **Pre-build forwarding information before packets arrive.**

This is different from older demand-driven switching approaches.

## Process Switching

Historically, process switching required the CPU to perform significant forwarding work for packets.

Conceptually:

```text
Packet arrives
     ↓
CPU
     ↓
Routing lookup
     ↓
Next-hop resolution
     ↓
Layer 2 rewrite
     ↓
Forward
```

Doing this repeatedly for every packet is expensive.

## Fast Switching

Fast switching introduced caching.

The first packet could require more CPU involvement, and subsequent packets could use a cached forwarding result.

This was much better than pure process switching but remained demand-driven.

## CEF

CEF is topology-driven.

The router builds forwarding structures before packets arrive.

Conceptually:

```text
Routing information
       ↓
      RIB
       ↓
      FIB
       +
 Adjacency information
       ↓
Fast packet forwarding
```

This means the first packet does not need to create a new per-destination route cache in the old fast-switching sense.

---

# Part 9: Adjacency Information

A router may know:

```text
Destination network → next-hop IP
```

but Ethernet forwarding also requires:

```text
Next-hop IP → next-hop MAC address
```

For IPv4, ARP is used to resolve IPv4 addresses to MAC addresses.

For IPv6, Neighbor Discovery (ND) performs the corresponding neighbor-resolution functions.

CEF uses adjacency information to perform the Layer 2 rewrite efficiently.

Think:

> **FIB tells me where the packet should go.**
>
> **Adjacency information tells me how to build the Layer 2 frame to get it there.**

---

# Part 10: CEF Special Adjacency Concepts

Several CEF concepts are useful for understanding troubleshooting.

## Receive

Traffic destined for the router itself is handled locally.

Examples include:

- Router interface IP
- Certain control-plane traffic

## Attached

The destination is associated with a directly connected network.

## Glean

The router knows the destination belongs to a connected prefix, but the Layer 2 adjacency for the individual host is not yet resolved.

For IPv4, ARP resolution may be required.

## Drop

CEF can represent destinations that should be discarded.

Examples can include certain invalid, reserved, or otherwise non-forwardable destinations depending on platform and configuration.

### Important Correction

Do not memorize a universal rule that every special address is always represented by exactly one particular CEF adjacency type. Exact behavior is platform and software dependent.

---

# Part 11: The Packet Walk — CEF Mental Model

Imagine:

```text
PC-A ---- R1 ---- R2 ---- Server-B
```

PC-A:

```text
192.168.1.10
```

Server-B:

```text
10.40.40.100
```

R1 knows:

```text
10.40.40.0/24
    via 192.168.12.2
    G0/1
```

When the packet reaches R1:

### Step 1 — Receive

R1 receives the Ethernet frame.

### Step 2 — Layer 2 processing

The incoming Layer 2 header is removed.

### Step 3 — Destination IP

R1 examines:

```text
10.40.40.100
```

### Step 4 — FIB lookup

R1 finds:

```text
10.40.40.0/24
```

### Step 5 — Next hop

The next hop is:

```text
192.168.12.2
```

### Step 6 — Adjacency

R1 determines the Layer 2 information required to reach R2.

### Step 7 — Layer 3 rewrite

The router:

- Decrements TTL
- Updates the IPv4 header checksum as required
- Preserves the destination IP
- Preserves the source IP unless a feature such as NAT changes it

### Step 8 — New Layer 2 frame

The outgoing frame has new Layer 2 addresses appropriate for the next link.

### Step 9 — Forward

R1 sends the frame out the selected interface.

---

# Part 12: What Happens at Every Router Hop?

A common beginner mistake is imagining that the original Ethernet frame travels end-to-end.

It does not.

At every routed hop:

```text
Old L2 frame
     ↓
Removed
     ↓
IP packet examined
     ↓
New L2 frame created
     ↓
Next router
```

The Layer 3 packet generally remains logically end-to-end, while the Layer 2 encapsulation is rebuilt for each hop.

---

# Part 13: TTL — Preventing Infinite Routing Loops

IPv4 uses **TTL (Time To Live)**.

IPv6 uses **Hop Limit**.

Each router decrements the value by one when forwarding the packet.

If a packet becomes trapped in a routing loop:

```text
R1 → R2 → R3 → R1 → ...
```

the TTL/Hop Limit eventually reaches zero and the packet is discarded.

This prevents a routing loop from consuming the network forever.

A common symptom is:

```text
traceroute
```

showing repeating hops.

---

# Part 14: Static Routing

Static routing means an administrator explicitly configures a route.

Example:

```text
R1(config)# ip route 10.20.20.0 255.255.255.0 192.168.12.2
```

This means:

> "To reach 10.20.20.0/24, use 192.168.12.2 as the next hop."

Static routes are:

### Advantages

- Simple
- Predictable
- No routing-protocol update traffic
- Useful for small or stable topologies
- Useful for default routes
- Useful for backup/floating routes
- Useful in special designs

### Disadvantages

- Manual configuration
- Poor scalability
- Topology changes may require administrator intervention
- Easy to misconfigure

---

# Part 15: Types of Static Routes

## 1. Static Network Route

Points to a network prefix.

```text
ip route 10.20.20.0 255.255.255.0 192.168.12.2
```

## 2. Static Host Route

A `/32` IPv4 route identifies one exact host.

```text
ip route 10.20.20.50 255.255.255.255 192.168.12.2
```

IPv6 host routes use `/128`.

## 3. Default Route

Matches everything that has no more-specific match.

IPv4:

```text
ip route 0.0.0.0 0.0.0.0 192.168.12.2
```

IPv6:

```text
ipv6 route ::/0 2001:db8:12::2
```

## 4. Floating Static Route

A floating static route is configured with a higher AD so that it stays inactive while a preferred route exists.

Example:

```text
ip route 10.20.20.0 255.255.255.0 192.168.12.2 200
```

If the normal route disappears, the floating static route can become active.

Think:

> **Primary route = main road**
>
> **Floating static = backup road**

---

# Part 16: Static Route Configuration Styles

## Next-Hop-Only

```text
ip route 10.20.20.0 255.255.255.0 192.168.12.2
```

The route specifies the next-hop IP.

The router must resolve how to reach that next hop.

## Exit-Interface-Only

```text
ip route 10.20.20.0 255.255.255.0 GigabitEthernet0/0
```

The route specifies the outgoing interface.

Behavior is particularly important on multiaccess networks such as Ethernet because the router may need to resolve the actual destination at Layer 2.

## Fully Specified Static Route

```text
ip route 10.20.20.0 255.255.255.0 GigabitEthernet0/0 192.168.12.2
```

This explicitly specifies:

- Exit interface
- Next-hop IP

For IPv6, fully specified static routes are especially useful when the next hop is a link-local address.

---

# Part 17: Recursive Static Routing

A **recursive static route** is commonly understood as a static route that specifies a next-hop address without an exit interface.

Example:

```text
ip route 10.33.33.0 255.255.255.0 10.12.1.2
```

R1 needs to resolve:

```text
10.33.33.0/24
       ↓
next hop 10.12.1.2
       ↓
how do I reach 10.12.1.2?
       ↓
10.12.1.0/24
       ↓
G0/0
```

Conceptually:

```text
Lookup #1:
Destination → 10.33.33.0/24

Lookup #2:
Next hop → 10.12.1.2

Result:
Outgoing interface → G0/0
```

### Important CEF Point

This does **not** mean every packet must repeatedly walk the RIB twice in modern CEF forwarding.

CEF resolves the forwarding information and programs the resulting information into the forwarding plane.

Therefore:

> **Recursive route resolution is a control-plane/route-resolution concept; CEF can make packet forwarding use the resolved result efficiently.**

---

# Part 18: Static Route Installation

A configured static route is not automatically guaranteed to appear as an active route.

The router must be able to resolve its forwarding information.

For example, if a next-hop address cannot be resolved through the routing table, the static route may not become active.

Useful verification:

```text
show ip route
show ip route static
show ip route <destination>
show running-config | include ip route
```

For IPv6:

```text
show ipv6 route
show ipv6 route static
show ipv6 route <destination>
```

---

# Part 19: Default Route — Gateway of Last Resort

A default route is:

```text
0.0.0.0/0
```

for IPv4, and:

```text
::/0
```

for IPv6.

It is the **least specific route**.

Because `/0` matches everything, it is used only when there is no more-specific matching route.

Example:

```text
S* 0.0.0.0/0 [1/0] via 192.0.2.1
```

The `*` indicates a candidate default route in Cisco routing-table output.

## Why Default Routes Matter

A branch router may not need routes to every destination on the Internet.

Instead:

```text
Branch
   |
   | default route
   v
Core / ISP
   |
   v
Internet
```

The branch says:

> "If I don't have a more specific route, send it this way."

---

# Part 20: Dynamic Routing

Dynamic routing protocols allow routers to discover routes and react to topology changes automatically.

A dynamic routing protocol generally needs to:

1. Discover or establish relationships with neighbors.
2. Exchange routing information.
3. Calculate preferred paths.
4. Install appropriate routes.
5. React to topology changes.
6. Converge.

### Convergence

**Convergence** is the process by which routers reach a consistent understanding of the changed topology and install the resulting best paths.

Faster convergence generally means less disruption after a failure.

---

# Part 21: Dynamic Routing Protocol Families

A useful conceptual classification is:

## Distance Vector

Example:

- RIP

Mental model:

> "My neighbor says the destination is this far away."

## Link State

Examples:

- OSPF
- IS-IS

Mental model:

> "I have a topology database and calculate paths through that topology."

## Advanced Distance Vector

Example:

- EIGRP

Mental model:

> "I exchange route information with neighbors and use DUAL to maintain loop-free paths."

## Path Vector

Example:

- BGP

Mental model:

> "I select routes using path attributes, including the AS path."

---

# Part 22: Distance Vector — Routing by Rumor

Traditional distance-vector routing does not build a complete topology map in the way a link-state protocol does.

A router learns destination information from neighbors.

RIP uses:

> **Hop count**

Example:

```text
R1 → R2 → R3 → Network X
```

R1 may see Network X as three hops away depending on the exact counting model.

### Strengths

- Simple
- Easy to understand

### Weaknesses

- Limited scalability
- Slow convergence compared with modern IGPs
- Hop-count metric is a poor representation of actual link quality

---

# Part 23: Link State — The Network Road Map

OSPF is a link-state routing protocol.

Instead of simply telling neighbors:

> "Network X is three hops away."

routers exchange information that allows the area to build a shared topology database.

Key terms:

- **LSA** — Link-State Advertisement
- **LSDB** — Link-State Database
- **SPF** — Shortest Path First
- **Dijkstra algorithm**

Mental model:

> **LSAs build the map. SPF calculates the paths.**

Each router runs SPF from its own perspective.

---

# Part 24: OSPF Fundamentals

OSPF is a major CCNP ENCOR routing topic.

Important concepts:

- Link state
- Areas
- LSAs
- LSDB
- SPF
- Router ID
- Neighbor adjacencies
- DR/BDR on broadcast networks
- Cost
- Area 0
- ABRs
- ASBRs
- External routes

---

# Part 25: OSPF Router ID

Every OSPF router needs a **Router ID**.

The Router ID is a 32-bit value written like an IPv4 address, but it is an identifier rather than necessarily an address used for packet forwarding.

Cisco OSPF router-ID selection commonly follows:

1. Manually configured router ID
2. Highest IP address on a loopback interface
3. Highest IP address on an active physical interface

A manually configured router ID is preferred because it is deterministic.

Example:

```text
router ospf 1
 router-id 1.1.1.1
```

---

# Part 26: OSPF Neighbors and Adjacencies

OSPF routers use **Hello packets** to discover and maintain neighbors.

Neighbor formation depends on matching important parameters such as:

- Area
- Network type
- Timers
- Authentication where configured
- Stub-area-related parameters where applicable
- Other protocol parameters

A neighbor relationship is not automatically the same thing as full database synchronization.

---

# Part 27: OSPF States

Know the major OSPF neighbor states conceptually:

```text
Down
  ↓
Init
  ↓
2-Way
  ↓
ExStart
  ↓
Exchange
  ↓
Loading
  ↓
Full
```

### Down

No valid Hellos have been received.

### Init

A Hello has been received, but the local router's own Router ID has not yet been seen in the neighbor's Hello.

### 2-Way

Bidirectional communication has been established.

On broadcast networks, some neighbors may remain 2-Way rather than becoming Full because of the DR/BDR process.

### ExStart

Routers establish master/slave roles and initial database-exchange parameters.

### Exchange

Database Description packets are exchanged.

### Loading

Missing LSAs are requested.

### Full

The LSDBs are synchronized.

---

# Part 28: OSPF DR and BDR

On multiaccess broadcast networks, having every OSPF router form a full adjacency with every other router would create unnecessary complexity.

OSPF elects:

- **DR — Designated Router**
- **BDR — Backup Designated Router**

Other routers form full adjacencies primarily with the DR and BDR.

### Election

The election uses:

1. Interface priority
2. Router ID as the tie-breaker

A priority of `0` prevents a router from becoming DR/BDR.

### Important

OSPF DR/BDR election is **not preemptive** in the usual sense.

A newly introduced router with a higher priority does not automatically replace the existing DR.

---

# Part 29: OSPF Cost

OSPF uses **cost** as its metric.

Conceptually:

> **Lower total path cost = preferred path**

The total cost of a route is based on the costs of the interfaces along the path.

The exact interface-cost calculation and reference bandwidth behavior depend on platform/configuration, so avoid memorizing an outdated universal bandwidth value without checking the platform.

---

# Part 30: OSPF Areas — Scaling the Topology

OSPF divides a large routing domain into **areas**.

The main idea:

> **Do not force every router to maintain every detail of the entire OSPF topology.**

Area 0 is the **backbone area**.

Other areas should normally connect to Area 0 for proper inter-area routing.

Benefits include:

- Smaller LSDB scope
- Reduced SPF work
- Route summarization at boundaries
- Better scalability
- Containment of topology changes

---

# Part 31: OSPF Router Roles

## Internal Router

All OSPF interfaces belong to the same area.

## ABR — Area Border Router

Connects different OSPF areas.

An ABR is associated with multiple areas and is a key point for inter-area information.

## ASBR — Autonomous System Boundary Router

Redistributes routes from another routing source into OSPF.

Example:

```text
BGP / Static / EIGRP
        ↓
      ASBR
        ↓
      OSPF
```

A router can be both an ABR and ASBR.

---

# Part 32: Important OSPF LSA Concepts

You do not need to memorize every LSA detail at the same time. Build the mental map first.

### Type 1 — Router LSA

Describes router links within an area.

Generated by every OSPF router.

### Type 2 — Network LSA

Generated by the DR on a multiaccess network.

Represents the multiaccess segment and attached OSPF routers.

### Type 3 — Summary LSA

Generated by ABRs to advertise inter-area networks.

Despite the name "summary," Type 3 LSAs are also used for ordinary inter-area route advertisement.

### Type 4 — ASBR Summary LSA

Provides information needed to reach an ASBR in another area.

### Type 5 — AS External LSA

Carries routes redistributed into OSPF from outside the OSPF domain.

### Type 7 — NSSA External LSA

Used for external routes inside an NSSA.

An ABR can translate Type 7 information into Type 5 information when appropriate.

---

# Part 33: OSPF Area Types

## Normal Area

Supports normal intra-area, inter-area, and external routing.

## Stub Area

Limits certain external LSAs and uses a default route for external destinations.

## Totally Stubby Area

Cisco extension that limits more routing information and uses a default route for destinations outside the area.

## NSSA — Not-So-Stubby Area

Allows an otherwise stub-like area to inject external routes.

NSSA uses:

```text
Type 7 LSA
```

for external routes inside the NSSA.

### Exam Reminder

Always distinguish:

```text
Stub
Totally Stubby
NSSA
Totally NSSA
```

The exact supported behavior depends on the implementation and configuration.

---

# Part 34: EIGRP Fundamentals

EIGRP is Cisco's **advanced distance-vector** routing protocol.

Its major algorithm is:

> **DUAL — Diffusing Update Algorithm**

Important EIGRP concepts:

- Neighbor table
- Topology table
- Routing table
- Hello packets
- Updates
- Queries
- Replies
- ACKs
- Successor
- Feasible successor
- Feasible distance
- Reported distance
- Feasibility condition
- Variance

---

# Part 35: EIGRP Neighbor Relationship

EIGRP uses Hello packets to discover neighbors and maintain relationships.

Once neighbors form, they exchange routing information.

Useful command:

```text
show ip eigrp neighbors
```

The neighbor relationship is essential because EIGRP relies heavily on neighbor communication.

---

# Part 36: EIGRP Tables

## Neighbor Table

Contains information about EIGRP neighbors.

```text
show ip eigrp neighbors
```

## Topology Table

Contains EIGRP-learned paths and their associated metrics.

```text
show ip eigrp topology
```

## Routing Table

Contains the routes that have actually been selected for forwarding.

```text
show ip route
```

Mental model:

```text
Neighbors
   ↓
Topology information
   ↓
DUAL
   ↓
Best path
   ↓
Routing table
```

---

# Part 37: EIGRP Successor and Feasible Successor

## Successor

The best route to a destination.

## Feasible Successor

A backup path that satisfies EIGRP's loop-free feasibility condition.

This can allow very fast convergence.

### Feasibility Condition

A neighbor is a feasible successor when:

> **The neighbor's reported distance is less than the local feasible distance.**

Conceptually:

```text
Neighbor says:
"I can reach Network X at distance 50."

Local best feasible distance:
70

50 < 70
→ Feasibility condition satisfied
```

This condition helps guarantee that the backup path is loop-free.

---

# Part 38: EIGRP Metric

Classic EIGRP uses a composite metric.

By default, the major components are:

- Bandwidth
- Delay

The default K-values effectively use:

```text
K1 = 1
K3 = 1
K2 = 0
K4 = 0
K5 = 0
```

Load and reliability do not influence the default metric.

### Important

Do not memorize the full mathematical formula until you understand:

> **EIGRP primarily uses the minimum bandwidth along the path and cumulative delay under the default configuration.**

---

# Part 39: EIGRP Unequal-Cost Load Balancing

EIGRP has a famous feature:

> **Unequal-cost load balancing**

This is configured with:

```text
variance
```

Example:

```text
router eigrp 100
 variance 2
```

A backup path must still satisfy EIGRP's feasibility requirements before variance can make it eligible.

Variance does **not** simply mean:

> "Install any route whose metric is twice the best route."

The path must first be a valid loop-free candidate.

---

# Part 40: Equal-Cost Multipath — ECMP

When multiple valid paths have the same best metric, the router can install multiple paths.

This is:

> **Equal-Cost Multipathing (ECMP)**

The exact number of supported paths depends on protocol and platform configuration.

Do not memorize a universal "4 paths" rule as if it applies to every modern Cisco platform.

---

# Part 41: Route Selection — Put It All Together

Imagine a router knows:

```text
10.10.10.0/24 via OSPF
10.10.10.0/24 via EIGRP
10.10.10.0/16 via static
```

There are two separate ideas.

## Route-source selection

For the exact same prefix:

```text
10.10.10.0/24
```

EIGRP AD 90 beats OSPF AD 110.

## Packet forwarding

If the destination is:

```text
10.10.10.50
```

the `/24` route is more specific than `/16`.

Therefore:

```text
10.10.10.0/24
```

wins the forwarding lookup.

### The Mental Model

```text
Routing protocols
      ↓
Select active routes
      ↓
RIB
      ↓
FIB
      ↓
Longest-prefix forwarding lookup
      ↓
Next hop / interface
      ↓
Layer 2 rewrite
      ↓
Forward
```

---

# Part 42: Route Summarization

**Route summarization**, also called route aggregation, combines multiple more-specific routes into a larger prefix.

Example:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

can be summarized as:

```text
192.168.1.0/24
```

## Why Summarize?

### 1. Smaller Routing Tables

Instead of carrying many routes, routers can carry one summary.

### 2. Reduced Routing Information

Fewer prefixes need to be advertised.

### 3. Better Stability

A topology change inside a summarized region may be hidden from parts of the network that only need the summary.

### 4. Scalability

Hierarchical addressing and summarization make large networks easier to manage.

---

# Part 43: Calculating a Summary Route

Suppose we have:

```text
192.168.1.0/26
192.168.1.64/26
192.168.1.128/26
192.168.1.192/26
```

The total range is:

```text
192.168.1.0 → 192.168.1.255
```

The first 24 bits are identical.

Therefore:

```text
192.168.1.0/24
```

is the summary.

### Binary Method

Compare the lowest and highest addresses.

```text
192.168.1.0
11000000.10101000.00000001.00000000

192.168.1.255
11000000.10101000.00000001.11111111
```

The first 24 bits match.

Therefore:

```text
/24
```

---

# Part 44: EIGRP Summarization

EIGRP supports manual route summarization on interfaces.

Example:

```text
interface GigabitEthernet0/1
 ip summary-address eigrp 100 172.16.0.0 255.255.0.0
```

A key benefit is that the summary can act as a **query boundary**.

If an EIGRP route disappears inside the summarized region, queries do not necessarily need to propagate beyond the summary boundary.

---

# Part 45: OSPF Summarization

OSPF summarization is performed at area boundaries.

ABRs can summarize inter-area routes.

Example:

```text
router ospf 1
 area 12 range 172.16.0.0 255.255.0.0
```

OSPF can also summarize external routes on an ASBR using appropriate configuration.

### Important Mental Model

OSPF is link state **within an area**.

You cannot simply hide topology details from routers inside the same area by creating a normal area-style summary.

Summarization is therefore strongly associated with:

- ABRs
- ASBRs

---

# Part 46: Null0 and Summary Discard Routes

Summarization creates an important routing problem.

Imagine:

```text
172.16.0.0/16
```

is advertised as a summary, but only some of its subnets actually exist.

A packet could arrive for:

```text
172.16.5.5
```

The upstream router may send it to the summarizing router because the `/16` says:

> "I can reach this."

But the summarizing router may have no more-specific route for `172.16.5.5`.

If it then sends the packet toward a default route pointing back upstream, a loop can occur.

A discard route toward:

```text
Null0
```

prevents this.

The key forwarding principle is:

> **A more-specific valid route beats the summary discard route.**

For example:

```text
172.16.3.0/24 → real interface
172.16.0.0/16 → Null0
```

Traffic to `172.16.3.5` uses `/24`.

Traffic to an unused address such as `172.16.5.5` uses `/16 → Null0`.

---

# Part 47: Policy-Based Routing — PBR

Normal routing is primarily destination based.

The question is:

> "Where is this packet going?"

PBR allows an administrator to make forwarding decisions based on additional characteristics.

Examples can include:

- Source IP
- Destination IP
- Protocol
- Ports
- Other match criteria supported by the configuration

PBR uses:

- ACLs
- Route maps
- `set` actions

Example structure:

```text
route-map PBR permit 10
 match ip address 101
 set ip next-hop 192.0.2.2

interface GigabitEthernet0/0
 ip policy route-map PBR
```

### Mental Model

Normal routing:

```text
Destination → routing table → next hop
```

PBR:

```text
Packet attributes
      ↓
Policy match
      ↓
Policy action
      ↓
Forwarding decision
```

---

# Part 48: PBR and the Routing Table

PBR is a policy mechanism that can override the normal routing decision for matching traffic.

It does not mean the routing table has been rewritten.

Instead:

> **PBR changes how selected packets are forwarded.**

Non-matching traffic can continue using normal routing.

### PBR Verification

Useful commands include:

```text
show route-map
show ip policy
show ip policy statistics
```

Exact commands and output vary with platform/software.

---

# Part 49: VRF — Virtual Routing and Forwarding

A **VRF** creates a separate routing table on the same physical router or multilayer switch.

Think of one physical router as containing multiple virtual routers:

```text
              Physical Router
          /         |          \
       VRF-A      VRF-B       Global
      routing    routing     routing
       table      table       table
```

Routes in VRF-A are normally isolated from routes in VRF-B.

This allows overlapping or independent routing domains.

---

# Part 50: VRF-Lite

**VRF-Lite** provides VRF-based segmentation without requiring MPLS provider infrastructure.

Example:

```text
VRF-CORP
VRF-GUEST
VRF-IOT
```

Each VRF can have:

- Its own interfaces
- Its own routing table
- Its own static routes
- Its own dynamic routing process/instance where supported

### Important

A route in one VRF does not automatically appear in another VRF.

This is the purpose of the isolation.

---

# Part 51: VRF Route Leaking

Sometimes isolated routing domains need controlled communication.

For example:

```text
VRF-CORP
     |
     | controlled routes
     v
Shared services
     ^
     |
VRF-GUEST
```

This is called:

> **Route leaking**

The exact mechanism depends on the platform and design.

The important mental model is:

> **VRF creates isolation. Route leaking creates controlled exceptions to that isolation.**

---

# Part 52: Recursive Routing Loops with Tunnels

A very important troubleshooting concept occurs when a tunnel endpoint is accidentally reachable **through the tunnel itself**.

Imagine:

```text
Underlay Internet
R1 ================= R2

        GRE Tunnel
R1 ----------------- R2
```

R1 must use the physical underlay to reach R2's tunnel destination.

Suppose routing accidentally learns:

```text
R2 public endpoint → GRE Tunnel
```

Then the tunnel has a paradox:

> To build the tunnel, R1 needs to reach R2's physical endpoint.
>
> But R1's routing table says the physical endpoint is reachable through the tunnel.

That can create a recursive routing problem.

Cisco IOS may report a message similar to:

```text
%TUN-5-RECURDOWN
```

### The Fix

Ensure the underlay endpoint is reachable through the underlay.

Common design approaches include:

- More-specific underlay routes
- Static routes
- Route filtering
- Prefix filtering
- Proper separation of underlay and overlay routing

---

# Part 53: Default Route vs. Specific Route

This is one of the easiest exam concepts to test.

Suppose:

```text
10.0.0.0/8
10.1.0.0/16
0.0.0.0/0
```

Destination:

```text
10.1.5.10
```

Matches all three.

Winner:

```text
10.1.0.0/16
```

Why?

Because:

```text
/16 > /8 > /0
```

### Memorize:

> **The default route is the least specific route.**

---

# Part 54: Route Selection vs. Forwarding — Final Mental Model

This is the section to revisit before an exam.

## Control Plane

```text
Connected
Static
OSPF
EIGRP
BGP
   ↓
Route learning
   ↓
AD
   ↓
Metric
   ↓
Best route
   ↓
RIB
```

## Data Plane

```text
Packet arrives
   ↓
Destination IP
   ↓
FIB lookup
   ↓
Longest Prefix Match
   ↓
Next-hop / adjacency
   ↓
Layer 2 rewrite
   ↓
Forward
```

### One Sentence

> **AD and metrics help determine which routes enter the RIB; longest-prefix matching determines which forwarding entry matches a packet.**

---

# Part 55: Essential Cisco Verification Commands

## Routing Table

```text
show ip route
show ipv6 route
```

## Specific Destination

```text
show ip route 10.10.10.10
show ipv6 route 2001:db8::10
```

## Static Routes

```text
show ip route static
show ipv6 route static
show running-config | include ip route
```

## CEF

```text
show ip cef
show adjacency
```

Platform-specific commands may differ.

## OSPF

```text
show ip ospf neighbor
show ip ospf interface
show ip ospf database
show ip protocols
show ip route ospf
```

## EIGRP

```text
show ip eigrp neighbors
show ip eigrp topology
show ip protocols
show ip route eigrp
```

## PBR

```text
show route-map
show ip policy
show ip policy statistics
```

## VRF

Common examples:

```text
show vrf
show ip route vrf <VRF-NAME>
```

Exact syntax varies by IOS/IOS XE platform and release.

---

# Part 56: Troubleshooting Method — Follow the Packet

When routing fails, do not randomly change configuration.

Use a structured process.

## Step 1 — Is the interface up?

Check:

```text
show ip interface brief
```

Ask:

- Is the interface administratively up?
- Is the line protocol up?
- Is the IP address correct?

## Step 2 — Is the destination known?

```text
show ip route <destination>
```

If there is no route:

- Check connected routes
- Check static routes
- Check OSPF/EIGRP
- Check redistribution
- Check default route

## Step 3 — Which route wins?

Look at:

- Prefix length
- AD
- Metric
- Next hop

## Step 4 — Is the next hop reachable?

Check the route to the next hop.

## Step 5 — Is Layer 2 resolution working?

IPv4:

```text
show arp
```

IPv6:

```text
show ipv6 neighbors
```

## Step 6 — Is forwarding being overridden?

Check:

- PBR
- VRF
- ACLs
- NAT
- Tunnel behavior
- Security policies

## Step 7 — Trace the packet

Useful tools:

```text
ping
traceroute
show ip cef
```

The key troubleshooting philosophy is:

> **Follow the packet hop by hop.**

---

# Part 57: Common Exam Traps

## Trap 1 — "Lowest AD always wins."

Not by itself.

The forwarding decision is not simply:

```text
lowest AD
```

Understand prefix specificity and route selection separately.

---

## Trap 2 — "The metric is compared between OSPF and EIGRP."

Normally, no.

Different routing protocols use different metric systems.

AD determines which source wins when competing routes represent the same prefix.

---

## Trap 3 — "CEF is the routing protocol."

No.

CEF is a **forwarding architecture**.

OSPF/EIGRP/BGP are routing protocols.

---

## Trap 4 — "FIB and RIB are the same table."

No.

They are related but serve different purposes.

```text
RIB = control-plane route information
FIB = forwarding-plane information
```

---

## Trap 5 — "The Layer 2 frame travels end-to-end."

No.

Layer 2 encapsulation changes at each routed hop.

---

## Trap 6 — "A default route always wins because it is a static route."

No.

A default route is `/0`, making it the least specific route.

A more-specific route wins.

---

## Trap 7 — "EIGRP is simply a link-state protocol."

No.

For CCNP terminology:

> **EIGRP = advanced distance vector**

---

## Trap 8 — "OSPF summarizes inside an area."

Not in the normal area-boundary sense.

OSPF summarization is associated primarily with ABRs and ASBRs.

---

## Trap 9 — "A feasible successor is just any backup route."

No.

It must satisfy EIGRP's feasibility condition to be considered loop-free.

---

## Trap 10 — "PBR changes the routing table."

Not necessarily.

PBR changes the forwarding policy for matching traffic.

---

## Trap 11 — "VRFs share one routing table."

No.

The whole point of VRF is separate routing instances/tables.

---

# Part 58: Routing Decision Cheat Sheet

When you see a routing question, ask these questions in order:

### Question 1
**What destination prefix does the packet match?**

→ Longest Prefix Match

### Question 2
**If multiple route sources advertise that same prefix, which source wins?**

→ Administrative Distance

### Question 3
**If the same routing protocol has multiple paths, which path wins?**

→ Protocol metric

### Question 4
**Are there multiple equal-cost valid paths?**

→ ECMP may install multiple paths

### Question 5
**Does a policy override normal routing?**

→ Check PBR and other forwarding features

### Question 6
**Is the route in a separate VRF?**

→ Check the correct routing table

### Question 7
**Can the next hop actually be resolved?**

→ Check recursive resolution and Layer 2 adjacency

---

# Part 59: One Complete Example

Consider:

```text
R1
 |
 +---- OSPF ---- 10.20.20.0/24
 |
 +---- EIGRP --- 10.20.20.0/24
 |
 +---- Static -- 10.20.0.0/16
 |
 +---- Default - 0.0.0.0/0
```

A packet arrives for:

```text
10.20.20.50
```

First, determine matching prefixes:

```text
10.20.20.0/24   ← matches
10.20.0.0/16    ← matches
0.0.0.0/0       ← matches
```

The `/24` is more specific than `/16` and `/0`.

So the `/24` forwarding entry is the relevant prefix.

Now suppose both OSPF and EIGRP advertise that `/24`.

Compare AD:

```text
EIGRP = 90
OSPF  = 110
```

EIGRP becomes the active route for that prefix.

If EIGRP then has two equal-metric paths, multiple paths may be installed according to the platform/protocol configuration.

Finally, CEF uses the resulting forwarding information to send the packet.

### Complete Chain

```text
Packet:
10.20.20.50
      ↓
Longest Prefix Match
      ↓
10.20.20.0/24
      ↓
EIGRP beats OSPF by AD
      ↓
EIGRP metric selects best path(s)
      ↓
RIB
      ↓
CEF/FIB
      ↓
Adjacency
      ↓
Layer 2 rewrite
      ↓
Forward
```

---

# Part 60: Final Memory Map

If you remember only one page, remember this:

```text
                         ROUTING
                            |
          +-----------------+------------------+
          |                                    |
      CONTROL PLANE                         DATA PLANE
          |                                    |
   Learn / calculate                      Forward packets
          |                                    |
   +------+------+                             |
   |             |                             |
 Static       Dynamic                          |
 routes       protocols                        |
   |             |                             |
   +------+------+                             |
          |                                    |
          v                                    |
         RIB                                   |
          |                                    |
     AD + Metric                               |
          |                                    |
          v                                    |
     Best routes                               |
          |                                    |
          v                                    |
         FIB <--------------------------------+
          |
   Longest Prefix Match
          |
          v
   Next-hop / adjacency
          |
          v
   L2 rewrite + transmit
```

## Routing Protocol Map

```text
RIP
 ↓
Distance Vector
 ↓
Hop Count

EIGRP
 ↓
Advanced Distance Vector
 ↓
DUAL
 ↓
Bandwidth + Delay by default

OSPF
 ↓
Link State
 ↓
LSDB
 ↓
SPF
 ↓
Cost

BGP
 ↓
Path Vector
 ↓
Path Attributes
 ↓
AS_PATH and policy
```

## Route Source Map

```text
Connected       AD 0
Static          AD 1
EIGRP Internal  AD 90
OSPF            AD 110
RIP             AD 120
EIGRP External  AD 170
```

## Forwarding Rule

> **Longest Prefix Match wins.**

## Route-Selection Rule

> **For competing routes to the same prefix, lower AD wins; within a routing protocol, the protocol metric selects the preferred path.**

## CEF Rule

> **RIB decides what should be forwarded; FIB and adjacency information make forwarding fast.**

## Static Route Rule

> **Know the destination prefix, next hop, and how that next hop is resolved.**

## OSPF Rule

> **LSAs build the topology view; SPF calculates the shortest paths.**

## EIGRP Rule

> **DUAL maintains loop-free paths; successor is best, feasible successor is a qualifying backup.**

## PBR Rule

> **Normal routing is destination based; PBR lets policy steer selected traffic.**

## VRF Rule

> **VRF separates routing tables; route leaking creates controlled communication between them.**

---

# Final Exam Checklist

Before considering Routing Fundamentals mastered, make sure you can explain these without notes:

- [ ] What routing actually does
- [ ] Default gateway
- [ ] Control plane vs. data plane
- [ ] RIB vs. FIB
- [ ] CEF
- [ ] Adjacency information
- [ ] Longest Prefix Match
- [ ] Administrative Distance
- [ ] Routing metrics
- [ ] Connected routes
- [ ] Static routes
- [ ] Recursive static routes
- [ ] Fully specified static routes
- [ ] Floating static routes
- [ ] Default routes
- [ ] Dynamic routing
- [ ] Convergence
- [ ] Distance vector
- [ ] Link state
- [ ] EIGRP
- [ ] DUAL
- [ ] Successor / feasible successor
- [ ] EIGRP metric
- [ ] EIGRP variance
- [ ] OSPF
- [ ] OSPF Router ID
- [ ] OSPF neighbor states
- [ ] DR / BDR
- [ ] OSPF cost
- [ ] OSPF areas
- [ ] ABR / ASBR
- [ ] Important OSPF LSAs
- [ ] OSPF area types
- [ ] Route summarization
- [ ] EIGRP summarization
- [ ] OSPF summarization
- [ ] Null0 summary routes
- [ ] PBR
- [ ] VRF-Lite
- [ ] Route leaking
- [ ] Recursive tunnel routing problems
- [ ] Routing verification commands
- [ ] Packet-by-packet troubleshooting

---

# The One-Minute Revision

If you are walking into an exam and have one minute:

> **Routing protocols learn routes and calculate paths.**
>
> **The RIB is the control-plane routing table.**
>
> **AD chooses between competing route sources for the same prefix.**
>
> **Metrics choose the preferred path within a routing protocol.**
>
> **The FIB is derived from the active routing information and is used for fast forwarding.**
>
> **CEF uses the FIB and adjacency information to forward efficiently.**
>
> **Packets are forwarded using longest-prefix matching.**
>
> **Static routes are manually configured; floating static routes provide backups using a higher AD.**
>
> **OSPF is link state: LSAs → LSDB → SPF.**
>
> **EIGRP is advanced distance vector: neighbors → topology table → DUAL → successor/feasible successor.**
>
> **Summarization reduces routing information and can create boundaries.**
>
> **PBR can override normal destination-based forwarding for selected traffic.**
>
> **VRF creates separate routing tables and routing domains.**
>
> **When troubleshooting, follow the packet: interface → route → best prefix → next hop → adjacency → forwarding → next hop.**

