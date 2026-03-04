# What is an Integer?

### I dont like to write a lot of explanations for this, but basically:
- An integer is a whole number.
- No decimals. No commas. No fractions.
- Just clean numbers like: -3, -2, -1, 0, 1, 2, 3.

### Integer includes:
- Positive numbers → 1, 2, 3
- Negative numbers → -1, -2, -3
- Zero → 0

### But wait! Not every number is an integer!
Watch this! Take a look at the differences between these two:
```txt
What's the difference between:
1. score = 10
and
2. score = 10.5
```

### The answer is simple!
- The first one is an integer.
- It's a whole number.
- The computer reads it as a clean numeric value, no decimal involved.
- The second one is NOT an integer.
- It's a floating number (decimal).
- Because there's a .5 behind it.

### So, what's the difference between these two?
- The first one is a whole number.
- The second one contains decimal precision.
Now look at this:
```txt
print(score / 2)
```

### If:
```txt
score = 10
```
- Result will be 5

### But if:
```txt
score = 10.5
```
- Result → 5.25

### So, what's the difference between these two?
- Integers deal with whole numbers only.
- Once decimals enter the chat, it's not an integer anymore.
- It's a floating number.

### Another example:
```txt
What's the difference between:
1. temperature = -5
2. temperature = "-5"
```
- The first one is an integer (negative integer).
- The second one is a string (just text that looks like a number).
- The computer treats them very differently.