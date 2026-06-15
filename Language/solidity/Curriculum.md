# 30-DAY SOLIDITY COMBAT COURSE
__Gemini-AI generated__

## PHASE 1: THE FOUNDATIONS (Day 1 - 7)
**Goal:** Stop being afraid of the syntax. Learn to talk to the EVM.

- [ ] **Day 1: The Basics (The "Bank" Model)**
    - Learn: `uint`, `address`, `mapping`.
    - Task: Create a contract where people can "Check-in" their address and store a number.

- [ ] **Day 2: Functions & Visibility**
    - Learn: `external`, `public`, `internal`, `private`.
    - Theory: Why `external` saves gas? (The "Door" analogy).

- [ ] **Day 3: Control Structures & Errors**
    - Learn: `require()`, `revert()`, `if/else`.
    - Task: Add a rule to Day 1: "Only addresses with more than 10 units can check-in."

- [ ] **Day 4: The Wallet (Ether Flow)**
    - Learn: `payable`, `msg.value`, `address(this).balance`.
    - Task: Create a "Digital Piggy Bank" (Deposit only).

- [ ] **Day 5: The Withdrawal Logic**
    - Learn: `transfer()`, `send()`, `call()`.
    - **CRITICAL:** Learn why `.call()` is the industry standard and why the others are "broken."

- [ ] **Day 6: Constructor & Ownership**
    - Learn: `constructor`, `msg.sender`.
    - Task: Make the Piggy Bank so ONLY the owner can withdraw.

- [ ] **Day 7: Review & Stress Test**
    - Project: Build a "Simple Donation Contract." 
    - Theory Check: What happens if someone sends ETH to a non-payable function?

---

## PHASE 2: DATA STRUCTURES & LOGIC (Day 8 - 14)
**Goal:** Moving from simple variables to complex systems.

- [ ] **Day 8: Structs & Arrays**
    - Learn: How to group data (e.g., a "User" profile with name, age, balance).

- [ ] **Day 9: Mappings of Structs**
    - Task: Build a "Voter Registration" system.

- [ ] **Day 10: Strings & Bytes**
    - Theory: Why strings are expensive and why we avoid them in Solidity.

- [ ] **Day 11: Events & Logging**
    - Learn: `event`, `emit`.
    - Theory: How Frontends "listen" to the blockchain. (The "Notification" system).

- [ ] **Day 12: Time in Solidity**
    - Learn: `block.timestamp`, `1 days`, `1 weeks`.
    - Task: Create a "Timelock" (You can't withdraw money until 7 days pass).

- [ ] **Day 13: Modifiers**
    - Learn: The `_` (underscore) magic. 
    - Task: Refactor your "Owner" logic into an `onlyOwner` modifier.

- [ ] **Day 14: Inheritance**
    - Learn: `is`, `virtual`, `override`. (The "Legacy" system).

---

## PHASE 3: THE ECOSYSTEM (Day 15 - 22)
**Goal:** Stop building in a vacuum. Start using industry standards.

- [ ] **Day 15: Contract Interaction**
    - Task: Contract A calls a function in Contract B.

- [ ] **Day 16: Interfaces (The "Agreement")**
    - Learn: `interface`. How to talk to any contract without seeing its code.

- [ ] **Day 17: ERC-20 Deep Dive (Money)**
    - Task: Read the OpenZeppelin ERC-20 code. 
    - Challenge: Launch your own "PR Token" on a testnet.

- [ ] **Day 18: ERC-721 (NFTs)**
    - Task: Mint a "Learning Certificate" NFT for yourself.

- [ ] **Day 19: OpenZeppelin Library**
    - Learn: Why we don't write our own Security logic. "Don't reinvent the wheel."

- [ ] **Day 20: Storage vs Memory vs Calldata**
    - **CRITICAL:** This is where the 10x devs are separated from the juniors. Gas optimization.

- [ ] **Day 21: Security - Reentrancy**
    - Theory: How the DAO hack happened. 
    - Task: Attack your own Piggy Bank contract.

- [ ] **Day 22: Security - Overflow/Underflow**
    - Theory: Why Solidity 0.8.x changed everything.

---

## PHASE 4: PROFESSIONAL TOOLS & DEPLOYMENT (Day 23 - 30)
**Goal:** Leave the "Browser" (Remix) and enter the "Terminal."

- [ ] **Day 23: Introduction to Foundry (or Hardhat)**
    - Task: Set up a local dev environment.

- [ ] **Day 24: Testing (The Safety Net)**
    - Learn: Write a test that fails if a non-owner tries to withdraw.

- [ ] **Day 25: Scripting & Deployment**
    - Task: Deploy a contract to Sepolia Testnet using a script.

- [ ] **Day 26: Verifying on Etherscan**
    - Theory: Transparency. Why "Verified" contracts matter for trust.

- [ ] **Day 27: Oracles (Chainlink)**
    - Learn: How to bring "Outside Data" (Price of BTC) into your contract.

- [ ] **Day 28: Project Week Begins**
    - Idea: A "Vesting Contract" for a PR Agency.

- [ ] **Day 29: Project Week - Hardening**
    - Use modifiers, events, and proper error handling.

- [ ] **Day 30: THE AUDIT**
    - Review your own code. Find 3 ways to break it. Fix them.