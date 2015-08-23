# Chapter 3 - Arithmetic for Computers

[TOC]

## Integer

### Overflow

#### Overflow conditions

**Add**

* `(+) add (-)` –> No overflow
* `(+) add (+)`, _result sign_ is 1 -> **Overflow**
* `(-) add (-)`, _result sign_ is 0 -> **Overflow**

**Subtract**

* (+) subtract (+), or (-) subtract (-) -> No overflow
* (+) subtract (-), _result sign_ is 1 -> **Overflow**
* (-) subtract (+), _result sign_ is 0 -> **Overflow**

#### How MIPS deals with overflow
_on overflow:_

* save PC in EPC (exception program counter) register (for returning later)
* jump to predefined handler address (to handle this overflow, if any)
* use `mfc0` instruction to retrieve EPC value to return after corrective action

### Multiplication
MIPS allows multiplication of two 32-bit registers, the product is stored into 2 registers:

* Upper part (aka _most significant_ 32 bits): HI
* Lower part (aka _least significant_ 32 bits): LO

**Formula**: `mult rs, rt`

To read result (2 x 32-bit registers)

* `mfhi rd`: move HI to rd
* `mflo rd`: move LO to rd

_Note_: `mul rd, rs, rt` does work too, but the result only stores least-significant 32-bit (i.e. LO)


### Division
MIPS also uses HI/LOW for division but in a different way:

* HI: stores the remainder, in 32-bit.
* LO: stores the quotient, in 32-bit.

Formula: `div rs, rt`

### Floating Point

#### Scientific Notation
**Normalzied form**

* Decimal value must be in the form of $ ±x.yyy*10^{zzz} $. There must be only 1 digit on the left of the floating point.
* Binrary value must be in the form of $±1.xxxxxx_2 * 2^{yyyy}$. There must be value '1' on the left of the floating point. 

**IEEE Std 754-1985**
There are 2 "modes" (personal opinions) to represent binary floating number:

* The first mode is the "human mode", it is how we present the number in writing, and it is the normalized form described above: $±1.xxxxxx_2 * 2^{yyyy}$
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/7e009916-5991-488b-b475-e546c9b80c00.png)

    
* The second mode is the "machine mode", it is how the machine reads and operates on floating point.
    ![](https://dl.dropboxusercontent.com/u/24437878/screenshots/d2a99d8d-d62b-4721-8870-e3463639caa6.png)


##### To convert from "human mode" to "machine mode":

* Make sure the value in "human mode" **_is already normalized_** before proceed.
* Record Sign bit (S) as 1 if this is a negative number, 0 if positive.
* The **fraction** is taken from the matissa of the floating number in "human mode". For e.g. fraction of 1.10101 is 10101. This goes straight to the Fraction bit section, starts from **_LEFT MOST BIT TO THE RIGHT_** on bit 10 for single precision, or bit 13 for double precision.
* The _Exponent value of the bit section_ is the _**binary value of the Exponent in the human mode, plus the Bias**_, which is 127 for Single Precision, and 1023 for Double Precision. 

**Invert the process to get "human mode" writing from "machine mode" floating binary.**


##### Smallest and Largest in Single-precision
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/f036e2a8-d298-4453-b736-af59297c8516.png)


##### Smallest and Largest in Double-precision
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/99c0a97a-514a-4231-9219-a8336823ad55.png)

#### Practice

##### Convert Base 10 Floating number to IEEE Binary
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/4ea8c621-de8c-4949-965d-e47f43b5821c.png)

##### Convert IEEE Binary to Base 10 Floating number
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/a70597f4-69a7-4cb4-8a71-35d19958bdc7.png)

##### Addition of Floating Point numbers in Base 10
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/24cf2b06-9eb3-4904-99a5-2a08f27edcde.png)

##### Addition of Floating Point numbers in Base 2
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/3ee87cdb-44fc-4482-9286-9a6f9a93eff7.png)

**Convert floating binary number to base 10**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/dccf4171-465a-4043-a2e6-785439018671.png)

##### Multiplication of Floating Point numbers in Base 10
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/0b027c91-e1d2-4d2e-97ce-a581edcd1bb9.png)

##### Multiplication of Floating Point numbers in Base 2
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/1e9393dc-edd3-4256-ac13-32ce003c684c.png)

#### Load/Store Floating Point Instructions in MIPS
**Using different instructions:**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/bda7d329-3826-46f7-8af9-bb6bacc776cc.png)

**and different registers:**
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/1ef64355-a26c-4b9a-a014-b3a534169d9c.png)

#### Other Operational Floating Point Instructions 
![](https://dl.dropboxusercontent.com/u/24437878/screenshots/22d4d04e-34c1-4b93-be78-3fb4c6f8d73d.png)


## Other Notes

* Shift Left/Right only works correctly on unsigned numbers, **NOT** signed number.
* MIPS ISA: uses mostly 54 core instructions, the rests are less frequent. 


## Excercise

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/bc3778a3-b236-41f0-ac3b-d1ec43fae92e.png)

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/f7b18d1c-ff0c-47cc-893b-66efb8395d3a.png)
