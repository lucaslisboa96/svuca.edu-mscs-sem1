# Chapter 19 - Realtime Systems

[TOC]

## Definitions of Real-time System
**Realtime Systems** is Computer System that requires _results produced within specified deadline_.

There are 3 types of realtime systems: 

* **Safety-Critical Systems**: if miss deadline –> CATASTROPHIC. E.g. Weapon, ABS, Flight Control, etc.
* **Hard Real-time Systems**: Guaranteed critical real-time (must completed within deadline)
* **Soft Real-time systems**: Critical real-time tasks are scheduled (but not forced).


## Characteristics of Real-time System
**Single purpose**, **small size**, **mass-produced**, _**specific timing requirements**_, and does not always provide all features such as standard desktop system.

## Features of Real-time System

### Address Translation
It uses MMU for virtual memory (sometimes disabled, or use as Address Translation), using Real Addressing Mode (i.e. Logical = Physical address) and Relocation Register to relocate the process.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/d6da896d-5d56-4f8d-b9bf-027bc90d4614.png)

### Preemptive, Priority Based Scheduling
* _Is a MUST for Real-Time Systems to be preemptive_ and real-time process should be assigned highest scheduling priority.
* Preemptive **Soft** Real-Time Systems: assign highest scheduling priority, for e.g. Solaris, Windows, Linux.
* Preemptive **Hard** Real-Time Systems: _guaranteed_ service within deadline requirements.

### Interrupt Latency & Dispatch Latency

* **Interrupt Latency**: time from arrival of interrupt to start of routine that handles interrupt:
    * Save state of current process, determine interrupt type, context switching, then hand over to ISR to handle the interrupt.
    * Increased when kernel disables interrupt handler.
* **Disptach Latency**: time for scheduler to take current process off CPU and switch to another. 
    * Preemptive Kernel keeps dispatch latency low. During the conflict phase (i.e. preemption), preempt any process running in Kernel, and release resource of low-priority processes. Some times _Priority Inversion_ is used to resolve Dispatch Latency issue. 

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/965f38bb-5ac1-4694-9167-ce77201e6876.png)

### CPU Scheduling

* Each process requires a block timing with constant interval called **period p**;
* However, in each period, it only uses a t time *(t < p)* to execute the job, **t is execution time or burst time**; 
* So the difference of `d = p - t` is defined as the **deadline**, i.e. if the process is not given the CPU before or by this d time it will not be able to finish its task on time. 

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/0b21de1b-a91f-479e-a84e-fdac496617d9.png)

There are 3 scheduling algorithms.

#### Rate-Monotonic Scheduling Algorithm
* Task's priority is inversely assigned with their period: The **shorter** the period, the **higher** the priority, and vice versa. 
* Higher priority preempts the lower one. 
* Process must execute on specific period p, and complete burst t during each period.
* Rate-Monotonic Scheduling can only shedule **n** processes with no more CPU Utilization than n(2^1/n -1), in **general is 0.69**. 

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/c89254a0-af80-485d-bc60-11dd37a25f78.png)


#### Earliest Deadline First (EDF)
* Priority sticks to the deadline, i.e. the earlier the deadline the higher priority.
* EDF is theoretically optimal.
* Algorithm
    * when a process finishes (and at the beginning), take the process with the lowest `processTimeToDeadline - processTimeToExecute` as the new current process
    * When a new process arrives, replace the current process if and only if `newProcessTimeToDeadline - newProcessTimeToExecute < currentProcessTimeToDeadline - currentProcessTimeStillNeededToExecute`.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/2473e2c4-13bd-4f09-8f42-a1d1369aba10.png)

#### Proportional Share Scheduling
* CPU shares are divided proportionaly to the the deadline, if deadline is short, more shares. 

#### Pthread API
* Pthread API is used to manage real-time threads. 
* SCHED_FIFO - for FCFS with a FIO queue, no time slicing.
* SCHED_RR - SCHED_FIFO with time-slicing for equal share of CPU time with same priority threads.
* SCHED_OTHER: not sure.

#### VxWorks
* VxWorks 5 does not distinguish between User mode and Kernel mode (only in v6).
* Events are handled in kernel.

## Questions

### Which systems below considered Hard Real Time scheduling?
**Ans**: Anti Lock Brake System.

### Why Virtual Memory is not good for Hard Real Time system?
**Ans**: Translation Time introduces latency, which is the important factor that RealTime System always wants to reduce.

### In Real-time system, which is _NOT_ related to Interrupt Latency?
**Ans**: Use the scheduler to schedule the highest priority ISR (this belongs to distpatch latency)

### Which statement is FALSE with Rate-Monotonic Scheduling?
**Ans**: The _lower_ the rate, the _lower_ the priority.

### Which one is NOT the param for Realtime Scheduling?
**Ans**: SCHED_NORMAL (not mentioned in the slides).