# Chapter 9 - IP protocol

[TOC]

Take a look back at the OSI model and TCP model before this chapter.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/f996e05a-8453-4cdf-bb33-8cdc6e061bf1.png)


![](https://dl.dropboxusercontent.com/u/24437878/screenshots/8b52ca9e-c7f8-47fb-9134-981b969b748c.png)


## ConnectionLess Operation

**Connectionless** communication is a data transmission method used _in packet switching_ where a message can be sent from one end point to another _without prior arrangement_. **Internet Protocol (IP)** at **Network Layer** and User Datagram Protocol (UDP) at Transport Layer are connectionless protocols.

**_Advantages_:**

* **Flexible**: this is the biggest advantage of IP as the packet is not tied to any path, it can go any route. 
* **Can be made robust**, i.e. can add another layer (TCP) to make a stronger structure.
* **No unecessary overhead**

## Internet Protocol

IP is connectionless, provides a one-off bus service. All ES [^ES] and routers _share this common network layer protocol_  as **Internet Protocol (IP)**. Thus all routers only need to implement up through IP (Network layer - LLC) as they do not need to care about the content of IP datagram. 

Example
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/1208754e-8b74-429c-8d5d-8dce6bfe35a9.png)

_IP layer provides:_

* Routing service for directing the packet.
* Datagram lifetime (TTL) for controlling the life/expiry of the packet.
* Fragmentation and reassembly service for data transmission.
* Error Control for error recovery.
* Flow Control for data rate and transmission control.

### Routing
* IP Routing uses **routing table** to indicate the next hop to which datagram is sent to. It can be dynamic or static. _Dynamic table is more flexible_ in dealing with error and congestion conditions. 
* The technique in used is **Source Routing**, which specifies the route to be followed.
* **Route Recording**: Each time a datagram packet hops on to new router, the internet address of the router is appended to the packet's list of traverse addresses. 

### Datagram Lifetime (TTL)
* IP uses a field called **TTL (Time-to-live)** to indicate the datagram packet lifetime. 
* TTL is initiated with an initial value called **hop count**. Each time it travels through a hop, _TTL decreases 1_. If TTL reaches 0 before the packet reaches destination, it will die out. 

### Fragmentation and Reassembly
* **Why fragmentation?** to keep the data packet to an _optimal size_ for better transmission, error control (smaller PDU size is better), flow control (smaller buffers on routers) and fairer usage of shared facilities. The down size is more interrupts (more headers). 
* Reassembly can be at intermediate node (routers) or at destination (ES). IP assembles packets at destination. 
* Since _IP datagrams do not come in order_, IP layer provides **a sequence number** to each packet so the _reassembling can be done in order_.

#### IP Fragmentation
Original IP datagram is split into multiple fragments, each is a **multiple of 8 bytes**. Each fragment has _the destination address, offset_ (position of the fragment in original datagram). Fragmentation uses these fields in the IP header:

* **Data Unit Identifier (ID)**: source address & destination address, the protocol layer that generate the data.
* **Data Length**: length of user data field (in octets-i.e. 8 bits block)
* **Offset**: position of the fragment in original datagram (in multiples of 64 bits) [^offset]
* **IP Flag**: 
    * M: 0 (false) if no more packet following, 1 (true) if otherwise. 
    * D: instruction not to fragment.  

[^offset]: That's why IP fragment must be in block of 8 bytes. 

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/42e4771f-74ee-44dd-9e93-e5d090fe02ae.png)
Note: 208 in octs (8 bit) is identical to 26 in 64-bit system. 

### Error and Flow Control

* **Error Control** is used to discard certain datagrams: expired lifetime, congestion, FCS error. Notification to source will be given in each case, except FCS (source address may be corrupted.) 
* **Flow Control** is to limit the incoming rate. The target hop can _send flow control packets (ICMP)_ to indicate its _busy status & its availability_ (in secs) to the source. The source _reset the waiting time when it receives the new availability_. 

### IPv4
IPv4 is defined in **RFC 791**, part of the TCP/IP suite. It has **2 specifications**: specification of _interface with a higher layer_, and sepcification of _actual protocol format and mechanism_. 

### IP Services
Includes its primitive implementation and functions and its parameters (data and control info passed by the sender/receiver). The parameters include (refer to the diagram for details):

* Source and dest addresses
* Protocol
* Type of Service
* Identification
* Fragment indicator (More)
* TTL
* Data Length
* Option Data
* User Data

In addition, there are IP Options: Security, Source routing, Route Recording, Stream Identification, Timestamping.

All those fields make up the IPv4 header.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/1447b949-30ce-483d-836d-96f7f0161785.png)

**Note:** 

* Version (4-bit): 4
* IHL (4-bit): IP Header Length, multiple of 4 bytes.
* Total Length: total length of the packet including header, multiple of 1 byte. 
* **Type of Service** is now replaced by DSCP and ECN (congestion indicator) ([Wikipedia](https://en.wikipedia.org/wiki/IPv4)):

> * Differentiated Services Code Point (DSCP) was originally defined as the Type of service (ToS) field. This field is now defined by RFC 2474 for Differentiated services (DiffServ). New technologies are emerging that require real-time data streaming and therefore make use of the DSCP field. An example is Voice over IP (VoIP), which is used for interactive data voice exchange.
> * Explicit Congestion Notification (ECN). This field is defined in RFC 3168 and allows end-to-end notification of network congestion without dropping packets. ECN is an optional feature that is only used when both endpoints support it and are willing to use it. It is only effective when supported by the underlying network.

### IPv4 Address Format
* Each IP address occupies 32-bit data length. 
* Consists of the network identifier and the host identifier. 
* Network identifier comes with prefix
    * Binary `0`: for class A IP address
    * Binary `10`: for class B IP address
    * Binary `110`: for class C IP address
    * Binary `1110`: for class D IP address, for future use
    * Binary `11110`: for class E IP address, for future use

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/6e951366-cae6-4365-a633-7faf453dddf0.png)

#### Calculate Network ID, Host ID base on IP Address and Netmask

**Network ID:**: Operate AND on the IP address and the Subnet Mask will produce the Network ID. For example: `192.228.17.57 AND 255.255.255.224 = 192.228.17.32`

**Host ID**: Operate AND on the IP address and the _bit inversion of Subnet Mask_ will produce the Host ID. For example: `192.228.17.57 AND bit-inverse(255.255.255.224) = 192.228.17.57 AND 0.0.0.31 = 25`


![](https://dl.dropboxusercontent.com/u/24437878/screenshots/5edf2cd5-49e4-410b-991c-a3ed92c691c4.png)


## Questions

### Why we need IP address if we already have Mac Address?

### Biggest advantage of IP?

### What indicates IP Datagram Life?

### Which ensemble way does IP datagram use?

### How does IHL measure the size of the IPv4 Header?

### How does Total Length measure the size of the IPv4 data?

### Calculate offset of this fragmentation.
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/42e4771f-74ee-44dd-9e93-e5d090fe02ae.png)

### Calculate Network ID and Host ID of IP Address and Subnet Mask

[^ES]: End System