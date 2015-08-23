# Chapter 14 - Protection

[TOC]

## Definitions

> Protection is to ensure that only authorized processes can operate on certain resources limited to its rights.

* Protection is internal. Security is external.
* **Key Principle** of Protection is the _Principle of Least Privilege_.

## Domain

* Domain = Collection of Acess Rights = Objects, {Right-Set}
* Protection Domain = Process + Domain = Process + (Objects, {Right-Sets})
* Domain covers _User_, _Process_, _Procedure_ and _Domain Switching capability_ (User, Kernel mode).
* Domain can be _static_ or _dynamic_.
* Unix Domain associates with User (instead of with process).

## Access Matrix
Access matrix is a model of protection.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/2ee2b308-2068-4968-a374-e05e458a20da.png)

* Domain can have acess rights (switch, control) to other domain.
* Access Right copy is denoted by (*), indicating the access right can be cloned to other domain in the same object.
* Owner access right allow add/remove of rights.

### Implementation of Access Matrix
#### Global Table
* Simple, large table storing access rights between Domain, Object, Right-set.
* May need to use Virtual Memory for storing.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/2ee2b308-2068-4968-a374-e05e458a20da.png)

#### Access List
* Is an implementation of Access Matrix assoc with each Object.
* Base on Object, create link of Domain/User and allowed operations.
* Likely used in UNIX.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/984454d4-d25c-4dc0-add9-3981fedfdab1.png)

#### Capability List
* Is an implementation of Access Matrix assoc with each Domain.
* Base on User/Domain, create link of Object and allowed operations.
* usually used for file descriptor table.

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/bb087969-ce91-42cf-86ac-c1ffbd5d4ce8.png)

#### Role Based Access Control (RBAC)
* Is another form of Access Matrix _used in Solaris_, but adding concept of **Role**, and **Privileges** (Right Set). 
* **Role is assigned to User/Process, and privileges and objects is assigned to Role**. 
    * Users/Process *-----*> Roles *-----*> {Objects, Set of Rights}

![](https://dl.dropboxusercontent.com/u/24437878/screenshots/af94a1d7-1d02-45c2-8cb3-6b4d6966e340.png)

## Access Rights Revocation
* **Access List**: delete access rights from access list. Simple, immediate. **Revocation of Access-Rights is implemented using an Access List**.
* **Capability List**: requires to locate the capability in the system before revoking. 

## Capability-Based System 
### Hydra System
* Fixed set of access rights known and interpreted by the system.
* operations on Objects are through pre-defined procedures.

### Cambridge CAP System
* Simpler but powerful
* Data Capability & software capability

## Language-Based Protection
* **More flexible** than the OS, but high overhead with access validation.
* Compiler-Based enforcement: restriction is built in to compiler.
* Example: **JVM** (Untrusted Classes, Stack Inspection)
 