# What is a string?

### I dont like to write a lot of explanations for this, but basically:
- A string is a sequence of characters, like a sentence.
- It's a data type, if the whole data based on alphabets characters, and no commas, no numbers, or anything else. Just pure letters.

### But wait! A number can also be turned into a string too!
Watch this! Take a look at the differences between these two:
```txt
What's the difference between:
1. age= 22
and
2. age= "22"
```

### The answer is simple!
- The first one is an **integer**. A typical number that can be applied to some mathematical operations. 
- So, the computer reads that the variable of age is valued to 22, and it's eligible to be used in mathematical operations!
- The second one is a **string**. A typical letter or word that can be applied to some string operations.
- Strings are used to store text, for a certain variable, and it's not eligible to be used in mathematical operations.
- So, the computer reads the second one like this:
"Hey! there's a variable here named age, and all i see here is that it's contain a text that says 22!". So? this is not a number, basically just a text.

### So, what's the difference between these two?
- The first one is a **number**. And you can do this too!
```txt
print (age + 2)
```
- The answer will be 24, because the computer able to read the first one as a number and perform the mathematical operation.
- However, the second one is a text.
- When you try to do this:
```txt
print (age + "2")
```
- You won't get the answer 24, because the computer didn't able to perform any mathematical operation on the second one, because it's a text.
- What you will get is 222, because the computer read it as a text "22" and it will concatenate it with another  number 2. So, it will become "222".