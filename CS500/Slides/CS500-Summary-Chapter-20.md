# Multimedia Systems

[TOC]


## Definitions / Concepts

* **Multimedia Timing Requirements**
    * Multimedia data must be accessed within _specific timing requirements_ (for e.g. 24-30 fps)
    * **Continuous media data** is data with _specific rate requirements_.
* **Streaming** has _2 types_:
    * Progressive Download: content stored on client's computer (Youtube, ESPN, CNN)
    * Realtime Streaming: content not stored on client's computer (TV broadcast, Internet Radio, etc.)
        * Live Streaming
        * On-Demand Streaming

## Characteristics of Multimedia Systems
> Large, very high data rates, and sensitive to timing delays during playback.

## Quality of Service (QoS)
Requires both **CPU**, **Disk**, and **Network**. **Rate requirements** are most important to QoS.

### Compression
Compress or Encoded can be lossy or lossless.

#### Definition

* **Lossy**: 
    * **Image**: some pixel data is lost.
    * **Audio**: some very high freqs or very low freqs (undetectable by human ear) are omitted.
    * **Video**: stores on differences between frames.
* **Lossless**: decodable to original form.

#### Lossy Compression Schemes

Using _MPEG Compression techniques_.

   * Layer 3 for audio.
   * Layer 2 for video.
   * Layer 1 for timing information synching between audio and video.

There are _3 or 4 MPEG schemes_

* **MPEG-1**: 
    * Used for low-res video, 1.5Mbps.
    * MP3 audio
    * Compression ratio 200:1
* **MPEG-2**:
    * Used for DVD and HDTV local playback.
    * Higer level (res) and profile (quality) video compression, 1.5Mbps to 15Mbps.
* ~~MPEG-3 (discontinued)~~
* **MPEG-4**:
    * Used for transmitting audio/video via internet.
    * Scalable quality.

### QoS Levels
* **Best Effort**: _no guarantee_ of requirements, mostly used in traditional OS.
* **Soft QoS**: priorize certain traffic streams, but still _no guarantee_ of requirement.
* **Hard QoS**: guarantee the quality requirements.

### QoS Parameters
* **Throughput**, i.e. data rate.
* **Delay**, delay of stream data delivery.
* **Jitter**, delays during playback.
* **Reliability**: errors rate in transmission and processing of data.

Parameters are negotiated between Client and Server, usually _data rate_. 

Guarantee of QoS is provided by **Admission Control**.

* Using Semaphores: simple admission control policy.
* Using Resource Managers: used for each type of resource. 
    * **CPU Scheduling**: soft real-time, and hard real-time (requires critical process to be serviced within a guaranteed period of time)
    * **Disk Scheduling**
        * using _EDF_, i.e. Earliest Deadline First, similar to Shortest Seek Time First, order requests by deadline. EDF may have higher seek times.
        * using _SCAN-EDF_, similar to EDF but grouping and order requests with relatively close deadlines. *Batch reordering must ensure request being served within deadline*.
    * **Network Management**
        * Protocols: RTP/RSTP, HTTP (stateless)
            * RTSP/RTP: Use HTTP to transfer the meta file, and RTP/RTSP for content delivery. RTSP commands include SETUP, PLAY, PAUSE, TEARDOWN.
        * Methods: Unicast, Broadcast, and Multicast. Unicast is most common.




