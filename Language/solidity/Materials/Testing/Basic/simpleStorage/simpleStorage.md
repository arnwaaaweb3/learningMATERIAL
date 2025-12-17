# Breakdown the Code

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public data; 

    function set(uint256 _data) public {
        data = _data;
    }

    function get() public view returns (uint256) {
        return data;
    }
}
```
## First (1):
### What you need to do is to define your smart contract license, and pragma the smart contract compiler version.
---
- **// SPDX-License-Identifier: GPL-3.0**

This is the SPDX-License-Identifier.  
It basically tells what your smart contract is licensed under  
Check out at SPDX.md for more explaanation.  

---
- **pragma solidity ^0.8.0;**

This is the compiler version that you need to compile this smart-contract.  
Here, ^0.8.0 means that:
**compile with 0.8.x, but not with 0.9.0 version.**  
As a Smart Contract Dev, you may throw some "feature" that only complies with specific version of compiler.  
Therefore, it's also important for you to know what's the update patch between each solidity compiler version.  
So that you won't configure a mismatch version of what compiler you need and your smart contract written pragma.  

Things like:
```text
- breaking changes
- security patch
- overflow behavior (pre-0.8 vs post-0.8)
```

Check out at Compiler.md for more explanation.

---

## Second (2):
### Next, you're going to define what your smart contract used for.
---
- **contract SimpleStorage {**

Here, I use word "contract" to define my smart contract.  
I name it "SimpleStorage". This is just a simple variable.  
Technically, you can use any name. But remember! Code readibility is number one!  
So, make sure you use a specific name that could explain it's function.  

Other tips:
    
    a. Use PascalCase: Each words are started with Capital letter, and no whitespace in-between.  
    (Example: SimpleStorage, ERC20Token, TokenVault).  
    
    b. Descriptive: Each contract name must have the ability to tell what's the function, without having the other dev need to read it first.  
    (In this example, i want a contract that acts like a storage and store some data, and the name SimpleStorage is kind of descriptive.)  

- **uint256 public data;**

Here, i define the basic needs of the SimpleStorage that i want to make.  
Commonly, the structure is like this:  

```text
[Data-Type] + [Visibility/Other Keywords] + [Variable Name]
```

I used uint256 to store zero to positive-value only (no negative value).  
I also used "public" as the visibility-specifier.  
"Public" here means, that the variable "data" is callable from outside of the contract, makes it can be seen as public.  
With "Public", other smart contract, frontends, ether.js, can easily call this variable like this:  

```text
contract.data
```

i also make the variable named as "data". This is not a fixed glossarium on Solidity.  
It's a variable name, so feel free to use a descriptive name to describe your variable.  
and this variable, is what i called as "state variable" or "contract-level variable.  
Think of it like the main tunnel from all what's happening inside your smart contract.  
In other words, yes! There'll be a local variable too.  

Other tips:
    
    a. Use camelCase: This is the most standard practice in professionals, where you should name your variable name in camelCase for a better readability.  
    First word starts with small letter, then the next word starts with Capital letter.  
    (example: newBalance, totalSupply, totalValue)  

    b. Don't use Solidity keyword: This is going to cause you some errors if you try to name your variable using Solidity's keywords.  
    Name like: "function", "view", "contract", etc are out of use.  

    c. Descriptive and Relevant: The variable name should be relevant for what it's used for.  
    And also, this variable name will be a "group name" to collaterally categorize your data.  
    So the more descriptive and relevant its name, the better name it is.  
    
    (example: Name like:  
    1. userBalance = to define numeric data of User Balance's value.  
    2. userAdress = to define a string of User Address.  
    3. totalSupply = to define a total supply of X, that could be redefined later.  
    etc...)  

---

# Third (3):  
### Define what is your contract ability (the function).  
---
- **function set(uint256 _data) public { data = _data; }**  

Here, you can use a word "function" each time you want to describe what's your contract abilities. (It's a preserved word that exist in Solidity)  
And here, i used a set() to change the state variable input into a local variable / parameter.  
It's changeable! You can use other words, as long it's not a preserved word from Solidity.  

Earlier the definition that i stated, i already named "data" as my state variable / contract-level variable.  
_(ref= **uint256 public data;**)._  
However, here i also write a different variable, a local variable (1 level down from the smart contract variable).  
and it's named "_data".  

So, this mean that i want to describe a function (**set()**), that could change the state variable value (**data**), with a local variable value (**_data**), when this function is called.  

**Summary**
```text
data        → state variable name (its name depends on Dev)  
_data       → local variable name (its name depends on Dev too)  
function    → A preserved word and a keyword to set a function to your smart contract (add ability).  
set         → function name (its name also depends Dev)  
(uint256 _data) → Parameter: (data-type + local variable name)  
public      → Visibility-specifier (It's a must have in each function / contract)  
{ data = _data; } → The function body / definition.  
```

**Key Concept**
```text
- State Variable (data): Permanent storage on blockchain, persists between function calls  
- Local Parameter (_data): Temporary, exists only during function execution  
- The function set() changes the blockchain state (requires gas fee when called)  
```

- **function get() public view returns (uint256) {**