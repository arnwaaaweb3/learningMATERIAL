# What is a Float?

### I dont like to write a lot of explanations for this, but basically:
- A float is a number that contains **decimal points**.
- It's a data type used to store **numbers with fractions**.
- Unlike integers, floats are **not whole numbers**.

Examples of floats:
- 3.14
- 10.5
- -2.75
- 0.5

---

### But wait! Floats look very similar to integers!

Watch this! Take a look at the differences between these two:

```txt
What's the difference between:
1. price = 10
and
2. price = 10.5
```

### The answer is simple!

- The first one is an **integer**.
- It's a whole number without any decimal point.
- The computer reads it as a standard numeric value.

- The second one is a **float**.
- Because it contains a decimal point.
- The computer reads it as a number with fractional precision.

---

### So, what happens when we do math with floats?

Example:

```txt
price = 10.5
print(price + 2)
```

The result will be:

```txt
12.5
```

Why?

Because the computer reads **10.5 as a number**, so it can perform mathematical operations normally.

---

### Now compare it with this example:

```txt
price = "10.5"
print(price + "2")
```

The result will be:

```txt
10.52
```

Why?

Because **"10.5" is a string**, not a number.

The computer reads it like text and simply **concatenates** the characters together.

So instead of doing math, it just combines the text.

---

### Quick Summary

- A **float** is a number with decimal points.
- Floats can be used in mathematical operations.
- Floats are different from integers because they contain fractions.
- Floats are different from strings because they are still numeric values.

Examples of floats:

```txt
3.14
0.75
-8.5
100.01
```