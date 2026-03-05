# Common Comparison Operators (Python)

When writing programs, sometimes we need to **compare values**.

For example:
- Is one number bigger than another?
- Are two values the same?
- Are they different?

To do this, Python uses something called **comparison operators**.

Comparison operators compare two values and return a **Boolean result**:
- `True` if the values are equal
- `False` if the values are not equal

---

# List of Common Comparison Operators

Here are the most commonly used comparison operators in Python.

| Operator | Meaning | Example |
|--------|--------|--------|
| `>` | Greater than | `5 > 3` |
| `<` | Less than | `2 < 8` |
| `==` | Equal to | `7 == 7` |
| `!=` | Not equal to | `4 != 9` |
| `>=` | Greater than or equal to | `10 >= 10` |
| `<=` | Less than or equal to | `6 <= 8` |

These operators are used **very often** in conditions and program logic.

---

### Example 1 : Greater Than (`>`)

```python
print(10 > 5)
```

Output:
- True
Because 10 is bigger than 5.

---

### Example 2:  Less Than (<)

```python
print(3 < 1)
```

Output:
- False
Because 3 is not less than 1.

---

### Example 3: Equal To (==)

```python
print(8 == 8)
```

Output:
- True
Both values are the same.

---

### Important note:**
**== means compare values, not assign values.**

- Assignment uses only one equal sign: '='
age = 21

- Comparison uses two equal signs:
age == 21

---

### Example 4:  Not Equal (!=)

```python
print(5 != 2)
```

Output:
- True
Because 5 is different from 2.

---

### Example 5: Greater Than or Equal (>=)

```python
print(10 >= 10)
```

Output:
- True
Because 10 is equal to 10, and that is allowed.

---

### Example 6: Less Than or Equal (<=)

```python
print(4 <= 9)
```

Output:
- True
Because 4 is less than 9.

---

### Using Comparison Operators with Variables

Comparison operators are usually used with variables.

Example:

age = 20

print(age >= 18)

Output:

True

This means the condition is satisfied.

Using Comparison Operators in Conditions

These operators are most commonly used in if statements.

Example:

age = 17

if age >= 18:
    print("You are an adult")

Since 17 >= 18 is False, the code inside the if statement will not run.