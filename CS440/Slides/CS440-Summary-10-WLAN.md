# Chapter 10 - WLAN

[TOC]

## Wireless LAN
### Wireless LAN Configuration

A typical WLAN consists of: 

* a **backbone wired LAN**, for connecting to Internet, or let other stations connecting to.
* a **Control Module (CM)** as interface of the WLAN (broadcast/receive), includes either a bridge or router linking the WLAN to the backbone.
* several **stations** or routers connecting to the Control Module.
* several **User Modules** (bridge & control a number of stations on another wired LAN)

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/6e0331ca-d862-402f-bf51-b2f52de2feb2.png)

### Wireless LAN Requirements

A wireless LAN must meet these 10 requirements: 

* **throughput**: maximize capacity by efficient use of medium
* **number of nodes**: can support several client nodes
* **connection to backbone LAN**: has connection to backbone LAN for other stationary nodes or internet connectivity.
* **service area**: wireless signal should cover certain area space
* **battery consumption**: low power usage for Wireless LAN connectivity
* **transmission robustness and security**: reliable signals, and secured connection (not easy to hack)
* **collocated network operation**: can co-exist with other Wireless LANs
* **license-free operation**: does not need to pay license fee when operating under certain bandwidth
* **handoff/roaming**: user can move from one cell to the other in the same network freely, without disrupting service.
* **dynamic configuration**: add, remove user/nodes, or reconfigure does not cause disruption to other users.

## IEEE 802.11
### IEEE 802.11 Standards
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/d0bb896b-a925-455b-9da4-8ea07080f8cb.png)

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/523be0ee-1611-411e-9031-6fe50a102208.png)


Reference: http://compnetworking.about.com/cs/wireless80211/a/aa80211standard.htm


### IEEE 802.11 Terminology

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/a860d7dc-ce70-4d38-bcd1-305d06bf97c7.png)

**Notes:**

* Frame = MAC Protocol Data Unit (MPDU)
* Access Point: Wireless router
* BSS: a set of APs and Stations
* ESS: a set of multiple BSSs, connected via DS
* Wifi Alliance: is a set of test suite for certifying the interoperability for 802.11 products


### IEEE 802.11 Services
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/56caf3ce-33b7-4f4e-b36c-b55b8bd7a6d0.png)

Logical Services include:

* **Station Service (SS)**: SS is about connecting the STA and is similar to plugging in an ethernet cable.
    * Authentication
    * Deauthentication
    * Encryption
    * MSDU delivery [^msdu_delivery]
    * Dynamic Frequency Selection (DFS)
    * Transmit Power Control (TPC)
    * Higher-layer timer synchronization (QoS only)
    * QoS traffic scheduling (QoS only)
    * Radio Measurement
    * DSE
* **Distribution System Service (DSS)**: DSS is all about how to get the data message from one point to another. It does that by exchanging the MAC frames from one station in one BSS to another station in another BSS, via the DS. Distribution service can also work in the same BSS, the frame will go through the AP between 2 stations.
    * Association: A station must be associated before the Distribution Service can deliver data to / from a station.
    * Reassociation: transfer an already established association to another AP, from one BSS to another. 
    * Disassociation: station or AP sends this signal to terminate the association, for leaving an ESS or shutting down. 
    * Distribution
    * Integration
    * QoS traffic scheduling (QoS only)
    * DSE
    * Internetworking with the DS
* **Integration Service (IS)**: enable the delivery of the MAC frames betwee the DS and a non-802.11 network via a portal, aka a frame format transfer method, basically translates a 802.11 frame into a 802.3 frame. 

[^msdu_delivery]: MSDU is a block of data (aka LLC PDU) passed down from MAC user to the MAC layer. If the MSDU is too large for a single MAC frame, it may be fragmented and transmitted in a serioes of MAC frames. These actions are supported by MSDU delivery.

#### Mobility Transition Types
A station can move while connected to the network and transmit frames while in motion. Its mobility is categorized into 3 types:

* **No Transition**: stationary or in a single BSS
* **BSS Transition**: cross different BSS in the same ESS
* **ESS transition**: cross different BSS in different ESS

### Medium Access Control

IEEE 802.11 MAC layer covers 3 functional areas: **reliable data delivery**, **access control** (register/login) and **security** (packet encryption). 

* **Reliability Data Delivery**: When a station receives a data frame from another station, it returns an acknowledgment (ACK) frame to the source station. If the source does not receive an ACK within a short period of time, either because its data frame was damaged or because the returning ACK was damaged, the source retransmits the frame.
* **Four Frame Exchange**: is the mechanism that IEEE 802.11 uses to transfer data in a more reliable way. 
    1. Source sends RTS (Request to Send) frame to the destination.
    1. Destination responds with a CTS (Clear to Send).
    1. Source transmits data after receiving CTS.
    1. Destination _responds immediately_ with an ACK each time it receives new frame. (This technique replaces the Collission Detection in CSMA/CD)
* The lower sublayer of MAC layer is the **DCF** (distributed coordination function). It uses **CSMA algorithm** (Carrier Sense Multiple Access), **without CD** (Collision Detection, normally in wire LAN it is CSMA/CD).
        ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/62cc0e93-2300-4027-bd1d-60861f0cfdb9.png)


## Questions
### Why we need to implement reliable data delivery at MAC layer?