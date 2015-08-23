# Chapter 7 - Multiplexing

[TOC]

**Problem**
> Consider 2 (or more) stations each is assigned a data link but does not use up its capacity. Thus a mean of sharing should be setup so that the capacity is properly shared between the 2 stations. This is Multiplexing.

## Definition

> Multiplexing is a popular networking technique that integrates multiple analog and digital signals into a signal transmitted over a shared medium. Multiplexers and de-multiplexers are used to convert multiple signals into one signal.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/55c86adb-46ea-4f18-9b73-658c6b25c9d1.png)

There are 2 types of Multiplexing: **Time Division Multiplexing** (TDM) and **Frequency Division Multiplexing** (FDM).

## FDM
> **FDM** is possible when the useful bandwidth of the transmission medium exceeds the required b/w of signals to be transmitted. A number of signals can be carried simultaneously if each signal is modulated onto a different carrier frequency for trasmission. 

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/2613fe15-1ef3-4235-b2fc-cf46448d0834.png)


*  Modulation equipment is required to move each signal to the required frequency band (to avoid overlapping), and then use multiplexing equipment to combine the modulated signals, each called **subcarrier**. 
* There are 2 problems the FDM system must cope:
    1. **Crosstalk**, this may happen since the component signals are close to each other. 
    2. **Intermodulation noise**.
* Long-distance, high capacity links most likely use FDM hierarchy. (AT&T, ITU-T).

### WDM - Wavelength Division Multiplexing
> **WDM** is a a derrived form of FDM, used in optical fiber where multiple beams of light are transmitted with different frequencies (thus, wavelength) on the same fiber cable. 

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/7ec6847a-e2f9-40bd-adc7-42d427381303.png)


## TDM (Time Division Multiplexing)
> **TDM** is a method of transmitting and receiving independent signals over a common signal path by letting each signal appears on the line _only a fraction of time_ in an alternating pattern.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/bc12979c-4036-47d1-92f6-8132b09e6216.png)

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/82a1b44b-db85-4efa-8634-70a5a1b19396.png)

* **Synchronous TDM** is called synchronous not because of synchronous transmission, but because its _time slots are already pre-assigned and fixed_. A slower input will take less time slot than faster inputs. 
* **Data Link Control**: TDM has _no header nor trailer_ because the _data link control protocol is not needed_ (i.e. no flow control and error control). The main reason is because TDM share transmission B/W with among all channels so if one channel miss the bus it should not stop others from transmitting, same reason for error control. _The error control should be applied to per-channel basis using HDLC_. 
* **Framing**: to maintain synchronization between source and destination, _one control bit is added into each TDM frame_.
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/173d9494-e1b0-43f7-a7e0-aa36d0ae3456.png)
* **Pulse Stuffing**: this technique stuffs extra dummy bits into each incoming signal until it matches the local clock (equalize the data rate among all sources that have different clock rates). The insertion is at fixed locations so the removal follows the same location. 
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/0dea5058-94e2-4900-8c2c-d1e9f8b6aaf2.png)

## SONET / SDH
> _Synchronous Optical Networking_ (SONET) and _Synchronous Digital Hierarchy_ (SDH) are standardized multiplexing protocols that transfer multiple digital bit streams over optical fiber using lasers or light-emitting diodes (LEDs).

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/6f73a792-22ca-4fd9-a61e-4305b0b8fe38.png)

**How to deduce the bandwidth of STS-1**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/80301ffb-c518-4c7a-9398-e13775f0f642.png)

* Frame rate: 125µs


## Questions
### What is the freq of voice or telephone signal?
**Ans**: 4Khz

### Prove why DS-1 = 1.544Mbps (1-bit stuffing)
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/c56a8c2f-6990-4a88-9dfa-8433adb2dd51.png)

### Find out how many bits are stuffes for DS-2
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/023d7a3c-7ab2-4b97-ba77-f6f8bfcb763d.png)

### What is North American TDM Carrier Standards
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/ca9c4561-9e94-4b40-9bdb-49002cae468d.png)
