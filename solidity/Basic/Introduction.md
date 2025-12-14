# Introduction

In this note, we will say hi to basic concepts of Solidity and Blockchain

---

# Basic Questions

**Q: What is a blockchain?**  
A: Think of a blockchain as a digital record book that is copied and shared across many computers around the world.  
Because every participant has a copy, no single person or authority can change the records, making it extremely secure and trustworthy.

**Q: What is a ledger?**  
A: A ledger is simply the name for that digital record book.  
It contains a complete history of all the transactions that have ever happened on the network.

**Q: How does a blockchain work?**  
A: It works by bundling new data (like transactions) into a "block."  
This block is cryptographically sealed and then validated by the network's participants.  
Once validated, this new block is permanently attached to the end of the previous block, creating a continuous, unbroken "chain" of records.

**Q: How secure is a blockchain?**  
A: It’s highly secure because of two things:  
1. **Cryptography**  
2. **Distribution**  
   - Every new block is linked to the old one using a unique cryptographic hash.  
   - If someone tries to change data in an old block, its signature changes, which instantly breaks the link to every block that followed.  
   - Since everyone in the network has a copy, the fake block is immediately noticed and rejected.

**Q: How does the record-sharing (distribution) process work?**  
A: When you send a transaction, it is first sent out (broadcasted) to the network and waits in a temporary holding area called the mempool.  
Special network participants (validators or miners) collect these waiting transactions and put them into a new block.  
To agree on which block is the correct one, the network uses a **Consensus Mechanism** (a set of rules).  
Once the new block is accepted by the consensus rules, it is shared with all other computers, and they all add a copy to their own ledger, keeping everything synchronized.

**Q: What is Solidity?**  
A: Solidity is the programming language used to write **Smart Contracts** for Ethereum.  
It defines the rules and logic for how an agreement works, and then executes the code automatically when the terms are met, all without needing a third-party lawyer or banker.

**Q: Is Solidity only for Ethereum?**  
A: No, but it is **EVM-native**, meaning it was specifically built for the Ethereum Virtual Machine (EVM).  
You can use Solidity on Ethereum, but also on any other blockchain that is compatible with the EVM (like Polygon or Avalanche C-Chain).

**Q: What is EVM?**  
A: **Ethereum Virtual Machine (EVM)** is a virtual machine that runs smart contracts within the Ethereum protocol.

**Q: How does EVM work?**  
A: EVM performs these three essential functions:  
1. **Execution Engine**  
   - Runs the bytecode of smart contracts (compiled from Solidity)  
   - Acts as the "brain" or CPU of the smart contract  

2. **State Management**  
   - Manages contract storage (variables and data types like `mapping`, `uint`, `string`, etc.)  
   - Organizes data in storage, memory, or stack  

3. **Gas Metering**  
   - Calculates gas fees for every operation  
   - Example costs:  
     - `ADD` → cheap gas fees  
     - `SSTORE` (write to storage) → expensive gas fees  
     - `KECCAK256` → moderately expensive  

For more details, refer to `EVM.txt`.

**Q: In Solidity, what is the difference between storage and memory?**  
A:  
- **Storage**:  
  - Permanent data storage (like a computer's hard disk)  
  - High gas costs  
  - Data persists on the blockchain after transaction completion  
  - Example: `string public name; // STORAGE`  

- **Memory**:  
  - Temporary data storage (exists only during function execution)  
  - Lower gas costs  
  - Data is discarded after transaction completes  

For more details, refer to the `storage` folder.

---

# Basic Notes

- **Turing Completeness**:  
  Solidity is often called Turing Complete, meaning it can solve any computation problem and perform any calculation.

- **Smart Contract Structure**:  
  A contract is a collection of functions and state variables.