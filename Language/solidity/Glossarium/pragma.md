# Pragma
---

## What is a pragma?
- Think of pragma like a version lock for your smart contract.

It tells the compiler:
```text
- “Hey, only use this version (or range of versions) of Solidity to compile this code.”
```
Why?
- Because different Solidity versions can behave differently. Some features change, some break, some get safer.
---

## Floating vs. Fixed Pragma: 
- In real cases, it's recommended to use fixed pragma (e.g pragma solidity 0.8.24;) for contract deployment. Why? Because you want to make sure that the compiler used during testing is the same as the compiler used during production. 

- Using ^ (caret) in the pragma statement because the latest compiler version is likely to have bugs that haven't been detected yet.

- However, using fixed pragma also had it own trade-offs. Your compiler maybe too rigid and can break easily under different environments.
---

## Common pattern:
1. Fixed Pragma: 
```text
pragma solidity 0.8.0;
Note: (strict as hell!)
```

2. Floating Pragma (Caret):
```text
pragma solidity ^0.8.0;
Note: this is what commonly used in real cases.
```

3. Range Pragma:
```text
pragma solidity >=0.8.0 <0.9.0;
Note: Perfect for complex libraries.
```
---

## Why This Matters (Real Talk)
Different Solidity versions can:
1. Add security features (like overflow checks in 0.8.x)
2. Change gas costs
3. Deprecate functions
4. Break old code

Example:
Before 0.8.0 → integer overflow was silent
After 0.8.0 → it throws error automatically

- So yeah… wrong version = potential bugs or vulnerabilities