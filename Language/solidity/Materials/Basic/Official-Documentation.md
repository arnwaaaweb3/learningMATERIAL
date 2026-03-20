# Official Documentation

# In this note, we will try to understand the official documentation of Solidity.

==================================================================================================
How to write a smart contract in Solidity:
1. Define the license of the smart contract source code.
2. Define the version of the Solidity compiler used to compile the smart contract.
==================================================================================================

# Example of SimpleStorage

// SPDX-License-Identifier: GPL-3.0  
--> This defines the license of the smart contract source code.  
    It specifies how the code can be used, modified, and distributed.

pragma solidity >=0.4.16 <0.9.0;  
--> This defines the version range of the Solidity compiler used.

contract SimpleStorage {  
    uint storedData;  
    --> This is a state variable that stores data on the blockchain.

    function set(uint x) public {  
        --> This function modifies the state variable.
        storedData = x;  
    }

    function get() public view returns (uint) {  
        --> This function reads and returns the stored value without modifying the state.
        return storedData;
    }
}