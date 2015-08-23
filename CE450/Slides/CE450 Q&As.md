# CE450 Q&As

[TOC]

## Theory Questions

### What are the 4 Classes of Computers?
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/92cc9eca-f627-4309-a517-c8a7684a609e.png)

### What are 2 classes of Computer PostPC Era?
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/53a3bf1e-8cec-4e7f-9b0f-9cd65cd38f05.png)

### Performance depends on?

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/82782b13-9498-405d-b80f-17ce2e58acde.png)


### Which software factors that affect the program performance?

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/c27cd5b6-09cd-4786-834b-fca38f1cd3b1.png)

### 4 principles of MIPS design
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/ba7c9ffe-fe59-47fb-a325-4d883b4f04c8.png)

### Range of 2-s Complement Signed Interger
_Range_: $-2^{n-1}$ to $+2^{n-1}-1$

* _Most Positive_: `0111 1111 ... 1111`
* _Most Negative_: `1000 0000 ... 0000`

### What are 32 MIPS registers?

Register Name | Common Name | Description
--- | --- | ---
$0 | zero | 0 
$1 | at | Assembler Temporary
\$2-$3 | v0-v1 | Result register of functions
\$4-$7 | a0-a3 | Arguments
\$8-$15 | t0-t7 | Temporary Registers 
\$16-$23 | s0-s7| Saved registeres for input/output
\$24-$25 | t8-t9 | Temporary Registers
\$26-$27 | k0-k1 | Reserved for OS kernel
$28 | gp | Global Pointer
$29 | sp | Stack Pointer
\$s30 | s8 | Saved registers
$31 | ra | return address

### What is R-type instruction format?
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/d3bab805-3371-416c-9e1e-40be2d614483.png)

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/6d71eb55-6458-43f7-bc33-7cd293cd7bf5.png)

**Opcode**: 0
**Func Code**:

add | sub | mult | div | sll | srl | and | or | nor | jr | slt
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- 
32 | 34 | 24 | 26| 0 | 2 | 36 | 37 | 39 | 8 | 42


### What is I-Type instruction format?
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/767a5f20-3a87-4dfb-9612-b3e25dfcb1ba.png)

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/63b2b201-62b1-4dd1-8ef0-8c3ce90fafa3.png)


**Func Code**: 0
**Opcode**: 

addi | beq | bne | lw | sw 
--- | --- | --- | --- | ---
8 | 4 | 5 | 35 | 43

### What is J-Type instruction format?

| opcode (6) | target (26)
--- | --- 

**Opcode:**

j | jal 
--- | ---
2 | 3

### What is the steps in procedure calling?
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/63dbd8bc-774e-466b-9ce6-e9cd5f620d35.png)

### Size per Character
* Byte-Encoded (ASCII, Latin): 1 byte per char
* Java: 2 bytes per char
* Unicode: 4 bytes per char

### How to achieve atomic memory update in shared memory using load linked (ll) and store conditional (sc)?
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/56983ffb-acd8-4d48-9635-d5c00797d33c.png)

### What is the code translation & startup process in MIPS
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/b432cc1e-1dd1-40b0-a977-d66d0270527e.png)

### What is the differences between Array and Point implementation in MIPS

Array | Pointer
--- | ---
Must have "multiply" inside the loop to recalculate the address | only "add" is required
require base address, and index of current step | require only current location (stored in the pointer)

### MIPS Fallacies
* Powerful instruction leads to high performance is NOT TRUE
* Using assembly code to achieve high performance is NOT TRUE
* Instruction set of MIPS doesn't change (i.e. Backward compatibility) is NOT TRUE



## Practical Questions

### Performance Formula

$ Performance = \frac {1}{Execution Time} $

Expand **Clock Cycle Time** => $ Clock Cycle Time = \frac {1}{ClockRate} $

$ CPU Time =  Clock Cycles * Clock Cycle Time = \frac {Clock Cycles} {ClockRate} $

Expand **Clock Cycle** => $ Clock Cycles = Instruction Count * Cycles Per Instruction $ 
$ CPU Time =  InstructionCount * CPI * ClockCycleTime = \frac {InstructionCount*CPI} {ClockRate} $

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/d7067e5d-f439-4416-a137-b4e4aa22626b.png)

$ CPU Time = \frac{Instructions}{Program}\frac{ClockCycles}{Instruction}\frac{Seconds}{ClockCycle} $

### The Power Consumption Forumla

$Power = Capacity * Voltage^2 * Frequency $

### The Amdahl's Law Formula

$ T_{improved} = \frac{T_{affected}}{improvementFactor} + T_{unaffected} $

### How to calculate 2-s complement number?

1. Invert the digits in positive binary form.

    $2_{10} = 0010_2$, inverted: $1101_2$
2. Then add 1 

    $1101_2+1_2 = 1110_2=-2_{10}$
    
Repeat the same process to convert 2-s negative number to positive number. 