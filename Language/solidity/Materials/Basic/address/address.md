# Address
address = a unique identifier for accounts on Ethereum
==================
# In this note, we will dismantle everything about the Address data type.

---

- What is an Address?
    It's a 20-byte data type (160 bits) that represents an account.
    In Solidity, it looks like a hex string: 0xAbC123...
    Think of it like a GPS coordinate for a house on a map. 
    The map is the Blockchain, and the Address tells the EVM exactly where to send data or money.

---

- Why 20 bytes (40 hex characters)?
    1. It’s derived from the Keccak-256 hash of the Public Key.

        - Public Key: think of this as your **"Digital DNA."** It’s a huge, long string of random-looking numbers that proves you own a specific account.

            - **Problem:** It's way too long and kinda "clunky" to use as a simple address.

            - **Solution:** So, in order to solve this, Ethereum uses a hash function called Keccak-256. The goal is to make the hash as short as possible, while still being secure.

        - Keccak-256 is a hashing function. You throw any data into it (like your Public Key), and it spits out a unique, fixed-length "fingerprint" that is 32 bytes long.

            - **Specialities:** It's an one-way hash function. Meaning, that you can hash something, words into it, and it will always produce the same output. But, if you try to reverse the hash (like, take the output and turn it back into the input), you'll get a different result.

    2. Ethereum takes the last 20 bytes of that hash to create your address.
    3. Why not the whole hash? Efficiency. 20 bytes is "unique enough" to avoid collisions while keeping storage costs (gas) lower.
    4. Why do we need Keccak-256 to hash our Public Key? Because using the raw Public Key is like trying to carry a giant 2-meter long physical key in your pocket. 
    By "deriving" the address via Keccak-256, we get something shorter, cleaner, and much safer to share with the world.

    Here's a step by step breakdown of how the address is created:
    1. Take the Public Key.
    2. Run it through the Keccak-256 blender.
    3. Take the result (the fingerprint).
    4. Chop off the first 12 bytes and keep only the last 20 bytes.
    And here we have our Ethereum address!

---

- There are two "flavors" of addresses:
    1. address: 
       A basic identifier. You can check its balance or use it as a key.
    2. address payable: 
       This is an address with superpowers. It has the `.transfer()` and `.send()` methods.

    Think of it like a smartphone.
    - regular address: Your phone is on "Read-Only" mode. You know that it exists, you can see it, you can feel it, but you can't do anything with it.
    - payable address: Your phone is on "Read-Write / Admin" mode. You can mostly do anything with it, much with every features.

    Both of them, yes.. are **also using the same Keccak-256 hashing algorithm.** If you looked at the raw bytecode of a compiled contract, you wouldn't see a difference.

    **The distinction only exists at the compiler level (Solidity).**
    It’s a safety feature for you, the developer, not a different type of account on the blockchain.
    
    **Analogy:**
    A regular `address` is like a business card. You know who they are.
    An `address payable` is like a business card with a physical wallet attached. You can actually shove money into it.

- address vs. address payable. Why distinguish them?
    - Type Safety: 
        - Solidity wants to prevent you from accidentally sending
            Ether to a contract that isn't designed to receive it.
        -Solidity is a statically typed language. It’s very strict
            because, in crypto, **a small mistake = lost money forever.**

    - If a contract doesn't have a `receive()` or `fallback()` function, sending it money is like throwing cash into a locked room with no door. It's stuck forever.

        - When you send Ether to a contract, the EVM looks at that contract and asks: "Hey, do you have a specific function to handle this incoming money?"
            - There are only two "doors" that allow a contract to accept plain Ether:
            
            ```solidity
           receive() external payable
            ```
            - 1. This is the main entrance. Used when someone sends ETH with no extra data.

            ```solidity
            fallback() external payable: 
            ```
            - 2. This is the back door. Used if the "main entrance" isn't there or if the sender sent some weird data the contract doesn't recognize.
            
            If neither of these exists, the contract has no door.
    
    - If money gets into a contract that doesn't have:
        1. A function to receive it.
        2. A function to withdraw it (like a withdraw() function that uses .transfer()).
        
        This means that Ether is effectively deleted from the circulating supply. 
        
        **It sits at that address on the blockchain, but since no code exists to move it, no human, no private key, and no hacker can ever touch it again. It is "locked in the room" and the room has no exit.**

    - By forcing you to use `payable`, the compiler makes you double-check your logic.

---

- The two types of "Residents" (Accounts):
    1. EOA (Externally Owned Account):
       Controlled by humans via private keys (like your MetaMask).
    2. Contract Account:
       Controlled by code. It has no private key. It only does what its script says.
    
    Critical Difference:
    - EOA: Can initiate transactions.
    - Contract: Can only "react" when an EOA or another contract pokes it.

- Common Usecases for address:
    1. Ownership (Owner)
       Storing the address of the person who deployed the contract.
       `address public owner;`
       Why? So you can restrict certain functions (like "Withdraw All Funds") to only that specific address.

    2. Mapping (The Phonebook)
       Linking an address to a value.
       `mapping(address => uint) public balances;`
       This is how ERC-20 tokens work. The contract is just a giant list of "Who owns what."

    3. Interaction (Calling other contracts)
       If you want your contract to talk to Uniswap or Aave, you need their address to know where to "call."

- Pro-Tip: The "Zero Address" (0x000...000)
    - In Solidity, if an address variable isn't initialized, it defaults to the Zero Address.
    - Burning Tokens: Sending tokens to the Zero Address is the standard way to "delete" them, because nobody has the private key for 0x0. It’s the digital black hole.
    - Security Check: Always check `require(newOwner != address(0))` to ensure you aren't accidentally destroying ownership.

- Summary of Address Logic:
    - It’s 160 bits (20 bytes).
    - It’s the destination for transactions.
    - `payable` is for sending ETH; non-payable is for data/identification.