# Compiler for Solidity

In this note, we will talk about Compiler for Solidity

## What is actually a compiler?
A compiler is basically a "translator" that converts human-readable code (like Solidity.sol) into machine-readable code (like bytecode).

## How does a compiler work?
- First, you write your smart contract in Solidity (.sol file).
- Then, the compiler will compile your smart contract into:
  - **A. EVM bytecode** - this is the machine-readable code that can be executed by EVM
  - **B. ABI (Application Binary Interface)** - this is the manual so that your frontend can call functions in your smart contract.

## Types of compilers
1. **solc** - this is the original compiler that was created by Ethereum Foundation.
2. **solc-js** - this is the compiler Javascript version that used for DevOps / web environment.

## Importance of compiler version
It's important because:
- With a different version of compiler, you may have different result.
- This could cause you a certain bug.
- That's why, in every Solidity file, you should add directive like:

  ```solidity
  pragma solidity ^0.8.20;

This is basically telling the compiler to compile your smart contract using the higher version from `0.8.20`, but lower than `0.9.0`.

What exactly compiler does?
- The compiler does these things:
  - A. Parsing
  - B. Semantic Analysis
  - C. Optimization
  - D. Code Generation

============================================================================================
# Side-Note

- Compiler does not giving a direct instruction into blockchain.
  - It's just generates things that EVM understands.
  - From human-readable code (items) to machine-understandable items.
  - Beside ABI, there's also a lot of other thing as the output, like:
    - Metadata.JSON
    - Opcodes
    - Gas Estimation
    - Source Map
