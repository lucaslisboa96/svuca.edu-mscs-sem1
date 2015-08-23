# Chapter 4 - LAN 
[TOC]

> The Technology and Protocol Architecture of LANs.


## Topologies
### Bus Topology

#### Characteristics
* **Full duplex** between stations and the tap (connector onto the bus/medium)
* Tranmission propagates **full length of medium**, on **both directions**, and being absorbed and removed by the terminator, at the end of the bus. Two problems arise: 
    * to identify the **target of the tranmission** –> each station has a **unique address**.
    * how to **regulate the transmission** –> transmit data in small blocks, called **frames**.
* Common topologies for LAN are **bus**, **tree**, **ring** and **star**, **which is the most dominant**, based on the use of switches.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/0d36f78a-20e6-45cf-abaa-28fe533f4954.png)

### Star Topology

#### Characteristics
* Each station connects to common central node, only one station can transmit at a time (hub).
* Central node broadcasts all messages it receives -> physical star topology, but logically is a bus

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/055028f0-6b81-4752-982e-90fb36ecbbda.png)

## IEEE 802 LAN Model

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/470710b7-75dd-42d2-bde9-5ea4d599fbe6.png)

* **IEEE 802**: a committee who defines the protocol in LAN layers: Physical layer, MAC layer, LLC layer. 
* How the **3 layers in LAN** work:
    * **Physical Layer**: convert the digital data to signal for transmission in medium.
        * Encoding & Decoding of signals
        * Preamble generation/removal for synchronization
        * Bit transmission & reception
    * **MAC Layer**: 
        * Assemble data to Frame on transmit, disassemble frame into data on receive. (Note: only MAC has trailer)
        * Recognize address and error detection (using CRC check in MAC Trailer).
        * Govern access to LAN transmission medium.
        * How does this work?
            * On the sender: 
                * Receives frame from LLC
                * Add the dest address and its address to the frame
                * pass the frame to physical layer
            * On the receiver:
                * Receives frame from Physical layer
                * Check frame errors
                * Verify if it's the receiver of the destination MAC address
                * Pass the frame up to LLC
    * **LLC Layer**: 
        * Provides services & interfaces to the higher levels
        * Provide flow control (ready to receive) and error control (frame error)

**IEEE 802 v/s OSI model**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/ebc26895-dfc7-4682-a937-f614d03d9f91.png)

**MAC frame diagram**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/077b2c00-05e5-45b0-8293-517595725f71.png)

### LLC - Logical Link Control

#### Characteristics
2 _different characteristics_ than most other link control protocols
* It must support **multi-access**, **shared medium**
* it's relieved of some details of link access by the MAC layer
* **Addressing**: using Service Access Points (s), including DSAP and SSAP.

#### Services
* **Unacknowledged Connectionless Service**: datagram-style, does not have flow and error control, data delivery is not guaranteed, useful when:
    * Higher layer of software has reliability and flow control mechanism (TCP). 
    * Avoid overhead or maintenance effort of connection establish.
* **Connection-mode Service**: logical connection setup is required, has flow control and error control, useful when:
    * in simple devices
    * little software operating above this level. But introducing more overhead in mainting table of active connections. 
* **Acknowledged Connectionless Service**: hybrid of above two: datagram-style, acknowledged, but NO logical connection setup. Useful when:
    * large comm channel needed
    * time critical or emergency control signals.

#### Protocol
Modeled after HDLC, the differences are:

* Use asynchronous balanced mode for connection-mode (type 2) service.
* Use unumbered PDU (typ 1) to support unacknowledged connectionless service.
* Use 2 new unnnumbered PDUs (type 3) to support acknowledged connectionless service.
* Permits multiplexing using LSAPs.

#### LLC PDU
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/d9afac34-8cdd-4509-97e3-6f7f0d62a174.png)

* MAC Control: (a) control the frame size, (b) define Start of Frame.

### MAC - Medium Access Control
**Keys: **

* where: control in central or distributed
    * Centralized: 
        * Pros: greater control in priorities, overrides, guaranteed capacity; simple access logic, avoid problems of distributed coordination.
        * Cons: SPOF
* how: control technique, either synchronous or asynchronous. Asynchronous has 3 categories: round robin, reservation, and contention.

#### Asynchronous Systems

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/f7a229c2-86fe-41ef-81b3-a8747d4f6fd1.png)

#### MAC Frame Handling

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/c330ca8b-16d8-4c2c-9d5f-e287c189292c.png)

* Receives data from LLC
* PDU = MAC Frame
* Detects errors 

