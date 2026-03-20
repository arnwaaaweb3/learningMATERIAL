# Function List

### This is the list of functions that exist within Solidity programs

```text
1. set(): to change the existing variable value.
2. get(): to retrieve a variable value.
3. view: to read data without modifying state.
4. pure: to execute logic without reading or modifying state.
5. payable: to allow a function to receive ETH.
6. fallback(): triggered when no matching function is found.
7. receive(): triggered when contract receives plain ETH.
```

---

## 🔁 SET FUNCTION

* Used to modify or update a state variable inside the contract.

### Example:

```solidity
function setGreeting(string memory _greeting) public {
    greeting = _greeting;
}
```

### Best used for:

* Updating contract state
* Writing new data to blockchain

⚠️ Requires gas (state-changing operation)

### Analogy:

Like editing a Google Docs file → changes are saved permanently

---

## 📥 GET FUNCTION

* Used to retrieve or read data from the contract.

### Example:

```solidity
function getGreeting() public view returns (string memory) {
    return greeting;
}
```

### Best used for:

* Fetching stored data
* Displaying information to users

⚠️ Free when called externally (off-chain)

### Analogy:

Like viewing a document → no changes are made

---

## 👁️ VIEW FUNCTION

* A function that reads state but does NOT modify it.

### Example:

```solidity
function getBalance() public view returns (uint) {
    return address(this).balance;
}
```

### Key characteristics:

* Cannot modify state
* Can read state variables

### Use cases:

* Checking balances
* Reading stored data

### Analogy:

Like checking your bank balance → you see it, but don’t change it

---

## 🧠 PURE FUNCTION

* A function that does NOT read or modify blockchain state.

### Example:

```solidity
function add(uint a, uint b) public pure returns (uint) {
    return a + b;
}
```

### Key characteristics:

* No state access
* No state modification

### Use cases:

* Mathematical operations
* Utility logic

### Analogy:

Like using a calculator → input → output, no memory involved

---

## 💰 PAYABLE FUNCTION

* Allows the function to receive ETH.

### Example:

```solidity
function deposit() public payable {
}
```

### Key characteristics:

* Must use `payable` keyword
* Can access `msg.value`

### Use cases:

* Deposits
* NFT mint payments
* Smart contract funding

### Analogy:

Like a payment gateway → accepts money

---

## 🚨 FALLBACK FUNCTION

* Triggered when:

  * Function does not exist
  * Data is sent but no match is found

### Example:

```solidity
fallback() external payable {
}
```

### Key characteristics:

* No function name
* Can be payable

### Use cases:

* Proxy contracts
* Handling unexpected calls

### Analogy:

Like a “catch-all” handler → when nothing matches

---

## 📩 RECEIVE FUNCTION

* Triggered when contract receives plain ETH (no data).

### Example:

```solidity
receive() external payable {
}
```

### Key characteristics:

* Called automatically
* No parameters
* Must be `external payable`

### Use cases:

* Accepting direct ETH transfers

### Analogy:

Like receiving cash directly → no message, just money

---

## ⚔️ Summary Table

| Function Type | Reads State | Modifies State | Receives ETH |
| ------------- | ----------- | -------------- | ------------ |
| set()         | ❌           | ✅              | ❌            |
| get()         | ✅           | ❌              | ❌            |
| view          | ✅           | ❌              | ❌            |
| pure          | ❌           | ❌              | ❌            |
| payable       | ❌           | ✅ (optional)   | ✅            |
| fallback()    | ❌           | ❌              | ✅ (optional) |
| receive()     | ❌           | ❌              | ✅            |

---
