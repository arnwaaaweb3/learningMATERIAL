# 🚀 ABI Note - Solidity Application Binary Interface

## In this note, we will talk about Solidity ABI
============================================================================================

### What is Solidity ABI?

Technically, ABI is a standard encoding that ensures every data from frontend can be conversed into binary format that EVM understands.
Think of it as the **"recipe book"** for any EVM-based blockchain.
It stands for **"Solidity Application Binary Interface"**
ABI is usually represented as a **JSON file** that describes the functions and data of the smart contract.
It's a universal standard for an EVM-based blockchain.
Solidity is just one of many languages that generates ABI.
ABI is not a written-text rules for human to understand, but the idea is to be a format that integrates frontend and backend to communicate with the smart contract.

### Imagine this (Analogy):

You have a smart coffee maker machine. Let's analogy it as the smart contract.
The machine has a lot buttons for you to understand with.
This machine of yours doesn't have printed label on each buttons, which cause confusion, yes.
But, lucky you, there's a **manual book** that you can read to understand each buttons function.
* And this manual book, is what we analogy as **Solidity ABI**.
* Things like:
    * `makeLatte()`
    * `addSugar()`
    * `withdrawCoffee()`
* It's all written in Solidity ABI.

### What happens if a Solidity ABI doesn’t exist?

Without an ABI, your smart contract becomes a **black box**.
Sure, you still have the contract address on-chain, but no application will know how to interact with it.
Your dApp wouldn’t know:
* how to encode function calls,
* how to decode the returned data,
* what inputs each function expects, or even,
* which functions exist.

Wallets and libraries like MetaMask, WalletConnect, Ethers.js, or Web3.js rely on the ABI to convert human-readable function calls into low-level EVM bytes.
Without it, they literally have no **“language”** to communicate with the contract.
In short:
> The contract still exists, but every tool around it goes blind.
> It’s not optional, ABI is a fundamental requirement for any off-chain interaction.

### How does Solidity ABI looks like?

It will look like this, a JSON file with a lot of functions and information:

```json
[
    {
        "inputs": [],
        "name": "getOwner",
        "outputs": [
        {
            "internalType": "address",
            "name": "",
            "type": "address"
        }],
        "stateMutability": "view",
        "type": "function"
    }
]
```

# What if My dApp and its smart contract didn't use ABI as in Solidity ABI?

First, your frontend (dApp) will go blind.
You can still call the contract, but you need to manually encode the calldata, which is very impractical.

With ABI, you can:
1. Get your dApp encoding data to send to smart contract
2. Your dApp can decode the data from smart contract
3. Your dApp can listen to the events from smart contract
4. Your dApp can call the functions from smart contract without misunderstanding.

---

# How to read Solidity ABI?

As a dev, what you only need to know is these fields:

1.  **name**: The name of the function.
2.  **inputs**: The parameters type that you send to the function.
3.  **outputs**: The return type of the function.
4.  **stateMutability**: The state of the function.
    There are four states:
    * **A. view**: The function is read-only. But this function allowed to view the states variables.
    * **B. pure**: The function is read-only and not allowed to view the states variables.
        * View and pure actually won't consuming gas fees, if they're being called off-chain.
    * **C. payable**: The function is payable.
    * **D. nonpayable**:
        * The function is not payable.
        * This function is allowed to write-off the state changes, but not allowed to receive any amount of ETH.

5.  **type**: The type of the function.
    It could be:
    * **A. function**: This is a function.
    * **B. constructor**: This is a constructor which will be called only once to initialize the early state. You can't call constructor once the smart contract is alive
    * **C. event**: This is an event.

---

# Compilation Output

It doesn't matter where you compile the contract:
From:
* Remix
* Hardhat
* Truffle
* Foundry
* etc.

They will all generate a JSON format, that contains:
a. **bytecode**: executable code on the chain
b. **ABI**: structured interface definition
c. **metadata**: information about compiler, source map, etc