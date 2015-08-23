# Chapter 4b - Pipeline Multiple Instructions

[TOC]

## Pipeline

### Summary
* Pipeline _improves performance_, _increase throughput_, _reduce average latency_ (but same abs latency). But it also depends on _structure hazards, data hazards, and control hazards_. 
* Pipeline implementation varies base on ISA design.
* Pipeline datapatch can be written in 2 ways. They are identical.
    * Logical: `IF->ID->EX->MEM->WB`
    * Physical: `IM->REG->ALU->DM->REG`

### Possible Pipeline actions on Branch

* **Stall on branch**: Wait until branch outcome is determined before fetching next instructions.
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/a043fd6f-03fc-42c3-b6bb-001e9a77ed5e.png)
* **Prediction on branch**: predict one possible outcome (could be base on past records). If it turns out correct, fine; if not, invalidate it by bubbles (noop).
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/97191bb9-ee69-4630-a542-8b1ae94e34d2.png)

### Pipeline Registers
Between each stages (IF, ID, EX, MEM, WB) there is a pipe that stores **pipeline registers**, which is used to hold result from previous cycle. Pipeline uses pipeline control to control signals derived from instruction in each cycle.

There are 2 types of diagram used to describe pipeline datapath: **"single clock cycle" pipeline diagram, and "multi clock cycle" diagram**.

**Single clock cycle diagram**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/1d45d16d-ca69-4efd-9a58-3e1ac390d146.png)

**Multi-clock cycle (or multicycle) diagram**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/6942206c-1cc6-4e4d-9730-dc2008009c3e.png)

## Hazards

### Structural Hazards
* Required resource is busy (IO, load, store)
* Stalling instruction fetch for that cycle cause pipeline buble
* Fixed by writing to register in first half of clock, then reading from register during second half.

### Data Hazards
* Need to wait for previous instruction to complete its data read/write.
* Forward result from one stage to another (although load will still cause stall)

#### Data Required In ALU Stage
"Newer" instruction require data available in registers _before going through ALU_. In some cases it can be resolved by **Forwarding (aka ByPassing)** data from older instruction. 

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/161495de-dce8-46a0-a84c-a9ec96417c41.png)

##### Forward Conditions for R-Type

> R-Type returns the data **right after ALU**, i.e. _result in EX|MEM or MEM|WB_.

**Forward data from old EX|MEM to new ID|EX**

    old EX|MEM.RegisterRd == new ID|EX.RegisterRs 
    old EX|MEM.RegisterRd == new ID|EX.RegisterRt 
    
**Forward data from old MEM|WB to new ID|EX**

    old MEM|WB.RegisterRd == new ID|EX.RegisterRs 
    old MEM|WB.RegisterRd == new ID|EX.RegisterRt 

**AND the old instruction outputs to registers**

    EX|MEM.RegWrite, MEM|WB.RegWrite
    
**AND if the control signal (or output) is not writing to to $zero**
    
    EX|MEM.RegisterRd ≠ 0
    MEM|WB.RegisterRD ≠ 0
    
**In Combination:**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/524535f3-3478-4b1b-b8fe-5389b384f693.png)

##### Stall Conditions for Load (I-type)
> Stall aka Bubble

> Load only returns the data **right after MEM**, i.e. _result appearing in MEM|WB only_. Thus to work with Load, we need to detect earlier at **ID|EX** (for old instr) and **IF|ID** (for new instr). 

If this condition meets, **stall and insert buble**.
    
    Old ID|EX.MemRead AND 
        ((ID|EX.RegisterRt == IF|ID.RegisterRs) OR
        (ID|EX.RegisterRt == IF|ID.RegisterRt)
        )

**How to stall**
> Set control values in old instr ID|EX register to 0 (bubble/no-op in EX, MEM, WB)
> Prevent updating PC and IF/ID registers in new instr. This result in refetch and re-decode in new instr.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/8131923a-08ff-4311-8383-3f2b2531cfbc.png)

**Stall characteristics**: stall reduces performance, but essential to get correct results. 


#### Data Required in ID stage

> This happens for **Branch as the newer instruction**.


* If a comparison register in beq is a destination of 2nd or 3rd _preceding ALU instruction_, **it needs 1 stall cycle** (BEQ needs data at ID, not EX).
    
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/46a57897-7cbf-41a0-9279-27a3c528e5c5.png)

* If a comparison register is a destination of immediately preceding load
instruction, **it need 2 stall cycle**.
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/66e03e6a-14ad-4056-b974-600c4f161c55.png)

### Control Hazard
Fetching next instruction depends on branch outcome
Options are move branch comparator to stage 2, predict branch outcome, and flush pipeline if wrong 

#### Stall in Branch

> _Similar to load_, if branch is _the preceding instruction_, **Branch** outcome only **determined in MEM**, i.e. MEM|WB, DM|REG

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/1c0c8709-3b72-4646-8ed3-7c1a8fb34cc0.png)

#### Dynamic Branch Prediction

* Using prediction buffer, aka branch history table. 
* Stores outcome, if wrong, flush pipeline and flip prediction.

##### 1-bit Predictor
Will waste 2 times if wrong.

##### 2-bit Predictor
Only change prediction on 2 successive mispredictions.


## Exceptions and Interrupt

### Exception
* **Exception**: unexpected events require change in flow of control, usually arise within the CPU in opposed to Interrupt arise from ext IO controller.
* **Handling**: 
    * Use **EPC (Exception Program Counter)** to save the Exception instruction address.
    * Use **Cause Register** to save Exception reason.
    * Use **Rescue** register to jump to rescue handler at `800000180`
* Alternative mechanism
    * Use vectored Interrupts, labeling them with specified opcode.
* **Handler actions**:
    * Find the cause
    * Find next action
        * if restartable: take corrective action and use EPC to return to program.
        * otherise: terminate program, report error
* If multiple exceptions: deal with earliest instruction