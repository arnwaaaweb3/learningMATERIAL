
==================
# uint
uint = unsigned integer
==================
# In this note, we will explore all about uint and its usecases.

- uint is: 
    a data type that can store value only between 0 and 2^256 - 1.
    this means that uint can't store a negative value, like a minus number.

- uint, unsigned here, means that the value (every bit in the uint) only served to store the value
    not to represent the value itself as positive or negative.
    To be clear, imagine that uint as a balance in a bank account. It's only show you how much money you have.
    But, balance itself can't be negative, right?
    So, the balance is unsigned, cannot represent the value of transaction itself.
    Which, in transaction itself, we need a positive value (add) and a negative value (subtract).

-  Now, the maximum value of uint is 2^256 - 1, which is the maximum value that can be stored in a uint.
    You may wonder, why 2^256-1?

- the formula of uint is:
    uintX = 2^X - 1
    X =  is the number of bits that the uint can store.
    -1 = is the maximum value that the uint can store. (in computers, we start counting from 0)

For simple example, we all know that binary code is exist between 0 and 1, Y/N.
    let's take a small number like 3 as our uint example:
        uint3 = 2^3, means there's only 8 combination we could create:
            1. 000                        5. 100
            2. 001                        6. 101
            3. 010                        7. 110
            4. 011                        8. 111
        for the smallest value, it's clearly 000
        but for the positive value, there's only 7 combination:
            001, 010, 011, 100, 101, 110, 111
        this is happened, because we (or computers) started count the combination from 0, so:
            uintX=2^X-1

- But, still! it doesn't answer the question of why 256? That seems an odd number, right?
    There's many reasons of why 256 is chosen.
    1. EVM was designed to work with word-size of 256 bits, so it's the default.
        This means that EVM "thinks" in 256 bits of block.
    2.There's a lot of cryptography operations that works heavily reliant on 256 bits.
        Things like Hashing, Elliptic Curve Cryptography, and so on.
    3. For security, 256 bits won't having an overflow issue.
        Speaking techincally, it's still does possibkle to be overflow, but it's must be happened because of error / mistake in programming the contract.
        But to imagine the size, 256 bits is super large and practically hard to reach.
        The main key is just for developers to not make an arithmetic operations pass over the limits.
        And also, to mention that compiler version should be higher than O.8.x version (the one who's auto revert overflow)
        Overflow is like when you want to add another value to the storage, but the storage itself doesn't had a space left for the new value.
        The range of 256 bits is super large!
    4. A lot of Ethereum's component are using hashing based on 256 bits, so it's also for consistency

- Now, let's talk about the best usecase for uint:
    1. Managing a financial value 
        The most common usecase of uint is if you want to manage a value that always stays between 0 and positive numbers.
        Things like: 
            - balance of an account (balance)
            - amount of tokens in an account (amount)
            - total supply of a token (totalSupply)
                Why? 
               Security:  The balance of an account or the amount of tokens must stay non-negative (>= 0)
               Standard: Majority of token standards like ERC-20 defines the balance, amount, and totalSupply as uint256
    
    2. Timestamp
        uint is also used in timestamp.
        shortly, there's no negative number in timestamp.
        timestamp in blockchain is a representation of the time in seconds since the epoch.
            In computer world, we have what we called as "Unix Epoch".
            Unix Epoch is the time in seconds since January 1, 1970, 00:00:00 UTC
                Why 1970?
                Because it's the year that the Unix was created.
                Unix Time was began from epoch 1970 convention.              And that time, engineers and computer scientists needed to create a standard time.
            Now, why blockchain also use this same timestamp?
            Because blockchain were made by modern computers, and modern computers are using Unix Epoch as their standard time.
            What happened if blockchain didn't have its own standard time?
            - No timestamp of historical transactions 
            - No timestamp of the arrangement process within the blockchain itself.
            - No deadline of the transaction 
            - No timestamp of token expiration, lock, vesting, cooldown, staking duration
            - Nodes may not be synchronized and inconsistent
    
    3. ID / Index
        uint is also used in ID and Index.
        You would never see a negative number in ID or Index either.
        Things like:
            - ID of an NFT (tokenID)
            - ID of an item (itemID)
            - ID of a user (userID)
            - Index of an array (arrayIndex)
        Why?
        Because the ID of all those stuffs must not written as a negative number.
    
    4. Counting
        uint is also used for counting.
        Things like:
            - Number of votes (voteCount)
            - Number of tokens (tokenCount)
            - Number of protocol users (numberOfUsers)
            - Number of transactions (transactionCount)

            

            

