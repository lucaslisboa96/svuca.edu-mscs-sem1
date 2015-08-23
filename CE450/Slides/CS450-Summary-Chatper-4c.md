# Chapter 4c - Instruction-Level Parallelism (ILP)

[TOC]

## ILP
ILP is used to achieve higher throughput and lower overall latency by executing multiple instructions in parallel. 

There are 2 ways to implement parallelism in MIPS. 

1. Pipeline
2. **Multiple Issue** 

## Multiple Issue
> **Definition of multiple issue**: start multiple instructions in multiple pipelines per clock cycle.

* **Issue Width**: the number of issue slots per instruction, for example 1 slot/instruction.
* **Pros**: Better peformance
    * increase instruction throughput
    * decrease CPI (to below 1) since IPC increases. If a process can run 4 instructions per cycle (IPC), that means it needs only 1/4 cycle for 1 instruction, i.e. CPI = 1/4
* **Cons**: 
    * Greater hardware complexity
    * harder code scheduling job for the compiler
    * Some dependencies still limit ILP. 

There are 2 types of Multiple Issue:

1. **_Static_ Multiple Issue**. 
    * Static = **Software**, represented by **Compiler**, which plays key role. 
    * Compiler groups instruction into "issue packets" to be issued together in 1 slot, i.e. 1 single cycle, and _detect & avoid hazards_.
    * Issue packet = very long instruction (combined of multiple smaller instructions) = **Very Long Instruction Word (VLIW)**
2. **_Dynamic_ Multiple Issue**
    * Dynamic = **Hardware**, represented by **CPU** aka "superscalar" processor, which plays key role.
    * CPU examines instruction stream to choose which instructions for issuing each cycle. CPU also resolves hazards, by using _advanced techniques_ at runtime.

### Mechanisms

#### Speculation
* Speculation in Multiple Issue is similar to _"Guess/prediction" in pipeline term_.
* Apply to both static and dynamic multiple issue
* For **handling branch hazard**.

##### Speculation in Compiler (software) / CPU (hardware)

Compiler (software) | CPU (hardware)
---|---
Reorder instructions | Look ahead for instructions to execute
Include "fix-up" instructions (nop/bubble) to recover from incorrect guess | Buffer results until it determine when they are needed, flush buffer on incorrect speculation.
_Exception handling_: <br/> use ISA support for deferring exceptions. | _Exception handling_: <br/> Buffer exceptions until instruction completes (may not occur).

#### Scheduling 
##### Scheduling Static Multiple Issue
* _Compiler analyszes and reorders instructions_ into issue packets. Issues in the same packet has _no dependency on each other_. Possible dependencies across packets, but compiler knows, try to detect and _remove hazards_.
* _Pad with nop_ if necessary.
* In looping situation, compiler uses a technique called **loop unrolling**, it checks how many loop runs (n), expand & run the unimportant instructions n times (using different registers - i.e. _register renaming_) and run the important instruction (the loop condition check) 1 time at last. In this case the loop requires less instruction count (minus the unecessary checking of loop condition in each loop), thus **results in better CPI**. 

    Example: **Scheduling with Static Dual Issue**
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/fbe90af8-c219-4770-b3da-a2cef30c829f.png)

* **Static Dual Issue**: _one ALU/branch instruction_ and _one load/store instruction_, 64-bit size, pad unused instruction with nop. 

##### Scheduling Dynamic Multiple Issue
(aka Dynamic Pipeline Scheduling)

* CPU can execute instructions out of order to avoid stalls.
* But **commit result to registers in order**.
* **Why use dynamic scheduling?** Not all stalls are predicable, can't always schedule around branches, different implementations of ISA have different latencies and hazards.
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/06aa49d4-db85-46fd-8574-d5dcea68727d.png)
    * Overall system is called **big buffer function unit**, which consists of multiple **functional units**, and a **commit unit (aka reorder buffer)**.
        * Instructions are loaded from memory for processing.
        * If operand is available in register file or reorder buffer, its value is copied to reservation and no longer required in the register for recycle (used by others).
        * If operand is not yet available, it will wait for the function unit or reorder buffer to provision. 

## Questions
### Is pipeline easy?
No, idea is easy, but implementation (details) is hard.

### Is pipeline independent of technology?
No, more transistors (HW technology) makes more advanced piepline techniques feasible. Thus ISA design (for pipeline) needs to be aware of technology trends. 

### Is poor ISA design making pipelining harder?
Yes, complex instruction sets introduce overhead, complex addressing causes memory indirection, long delayed branches. 

### Relationship of ISA and datapath and control?
ISA influences design of data path and control, and vice versa. 

### What limits the parallelism?
Instruction dependencies, instruction complexity. 