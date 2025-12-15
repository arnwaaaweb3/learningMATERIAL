# Breakdown the Code

```json
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
It basically tells what your smart-contract licensed is.
Check out at SPDX.md for more explaanation.

---
- **pragma solidity ^0.8.0;**

This is the compiler version that you need to compile this smart-contract.
As a Smart Contract Dev, you may throw some "feature" that only complies with specific version of compiler.
Therefore, it's also important for you to know what's the update patch between each solidity compiler version.
So that you won't configure a mismatch version of what compiler you need and your smart contract written pragma.
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

```json
[Data-Type] + [Visibility/Other Keywords] + [Variable Name]
```

I used uint256 to store zero to positive-value only (no negative value).
I also used "public" as the visibility-specifier, so that the uint256 that i asked can be view as public.
i also make the variable named as "data". This is not a fixed glossarium on Solidity.
It's a variable name, so feel free to use a descriptive name to describe your variable.

Other tips:
    
    a. Use camelCase: This is the most standard practice in professionals, where you should name your variable name in camelCase for a better readability.
    First word starts with small letter, then the next word starts with Capital letter.
    (example: newBalance, totalSupply, totalValue)

    b. Don't use Solidity keyword: This is going to cause you some errors if you try to name your variable using Solidity's keywords.
    Name like: "function", "view", "contract", etc are out of use.

    c. Descriptive and Relevant: The variable name should be relevant for what it's used for. 
    And also, this variable name will be a "group name" to collaterally categorize your data.
    So the more descriptive and relevant its name, the better name it is.\
    
    (example: Name like: 
    1. userBalance = to define numeric data of User Balance's value.
    2. userAdress = to define a string of User Address.
    3. totalSupply = to define a total supply of X, that could be redefined later.
    etc...)

