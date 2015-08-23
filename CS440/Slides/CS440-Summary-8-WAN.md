# WAN (Wide Area Network)

[TOC]

## Switch Communications Network

_Beyond LAN_, data is transmitted from source to destination via a network of intermediate switching nodes, aka **Switched Communication Network**. 
This network is made of many **nodes**, aka the switching devices that receive and forward data. A node can be a **switching node**, i.e. it only focuses on moving data, or a normal node. 
A normal node has many **stations**, aka end devices such as computer, terminal, etc. connected to it, to send and receive data. 
**Node-Station** link is usually _point-to-point_ link.
**Node-Node** link is usually _multiplexed_, either _FDM_ (Frequency Division Multiplexing) or _TDM_ (Time Division Multiplexing).

There are 2 different technologies used in WAN: 

1. Circuit Switching
2. Packet Switching

### Circuit Switching

Derived from **public telephone network**, Circuit Switching connects 2 nodes/stations by a _dedicated path_. It takes some time to negotiate & _establish the connection_ before the transmission can happen, and _requires disconnection_ when done, `Establish –> Transfer –> Disconnect`. It can be _inefficient_ as the dedicated path _takes up dedicated channel capacity_ during the connection, and the _capacity might be wasted_ if no data is transmitted. 

* **Usage**: it is not always used in 100%, even in voice call, might be worse for client-server terminal connection, inefficient for digital transmission.
* **Performance**: Delay prior to connection establishment, but transparent and _no transmission delay nor variation in delay_ (both are requirements of voice traffic) afterward. 
* **Application**: Public Telephone Network, PBX (to interconnect telephones within a building), private network, data switch. 
* **Characteristic**: *Blocking* or *Non-Blocking*
	* _Blocking_: only 1 connection between 2 stations at a time, use all paths, **for voice systems**.
	* _Non-Blocking_: all stations can connect at the same time, **more suitable for data connection**.


#### Circuit Switch Node 
Consists of has 3 parts: 

* the **Digital Switch** provides transparent signal path and _support full-duplex transmission_.
* **Network Interface** faces the digital devices (computer)
* and **Control Unit** to establish, maintain or terminate the connection. 
![](https://i.imgur.com/NsePWZQ.png)

#### Space Division Switching
> Space Division Switch is a switch in which _signal paths are physically separate_ from one another (divided in space). Each connection requires the establishment of a _physical path through the switch dedicatedly_ between 2 end points. Basic building block is a metallic crosspoint or semiconductor gate.

**Single Stage Switch or Crossbar Switch**
![](https://i.imgur.com/kiWw4UZ.png)

**Multi-stage Switch**
![](https://i.imgur.com/aIbCRWq.png)

Compare 2 types of space division switch. 

 | Single Stage (Crossbar) Switch | Multi-Stage Switch
---|---|---
Advantages | <ul><li>simple</li><li>non-blocking scheme, everyone can talk to each other</li>| lesser/smaller switches <br/>–> efficient in cost & hw maintenance
Disadvantages | <ul><li>list of switch grows huge, difficult to maintain</li><li>SPOF (if a switch fail, comm can't be made)</li></ul> | Maybe blocking, i.e. there is a max of number of connection can be established at the same time

#### Time Division Switching
This switch uses the TDM technique, to partition different lower-speed bit streams into chunks for sharing a higher speed stream.
Example of a synchronous TDM, it uses TSI mechanism (Time-Slot Interchange).
![](https://i.imgur.com/SYuNfWo.png)
TSI is simple and effective, but the number of connections is limited by the amount of latency it can tolerate, so people use multiple TSI to carry a portion of the traffic and improve the latency.

#### SoftSwitch
A general-purpose computer running specialized software is used as a smart phone switch. 
SoftSwitch costs less and has more functions than traditional circuit switches, very popular for VOIP approach.


### Packet Switching
Packet Switching is designed for data transmission, which breaks the big packet into smaller ones, containing user data and control info (for routing purposes). Packet Switching has several advantages over Circuit Switching:

* **Line efficiency**, single line shared by multiple packets
* it supports **data-rate conversion** so different stations using different data rates can exchange data.
* Packets are accepted & **buffered when network is busy** (which is rejected in Circuit Switching)
* **Prioritization** can be implemented.

There are 2 switching techniques:

1. **Packet Datagram**: each packet is _independent_ from each other. Datagram is primitive thus _flexible_, _no establishment setup_. Packet can go on different routes, thus _more flexible_ in case one node is down, and _arrive out of sequence_.
2. **Virtual Circuit**: similar to Circuit Switching, a _preplanned route is setup_ for transferring packets (thus taking more time for establishment). _No routing decision_ is required afterward thus packets are _fwded more quickly_. It's _less reliable_ as if one or more node in the route is down. Used in ATM, point-2-point connection. For _long message_, this is more preferrable. 

**Example:**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/49ecf255-3e3b-47c5-b12e-c5492ef3d0a4.png)


### Comparison of Communication Switching Techniques (Important)
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/5180b85f-8f2a-48ff-8947-63ee520ebaba.png)


### ATM (Asynchronous Transfer Mode)
ATM is a _switching and MUX technology_ that breaks packet into small, fixed-length packets called cells, to obtain the **performance of circuit-switching network**, and **flexibility and efficiency of a packet-switching network**, mostly used in DSL implementation.