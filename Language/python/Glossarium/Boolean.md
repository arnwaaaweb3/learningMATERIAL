# Boolean (True or False)

When you're learning programming, one of the most important concepts is **Boolean**.

A Boolean is a **data type that only has two possible values**:

- `True`
- `False`

That's it. Nothing more.

You can think of Boolean like a **yes/no question**.

Examples in real life:
- Is the light on? → Yes / No  
- Is the door locked? → Yes / No  
- Are you logged in? → Yes / No  

In Python, these answers become:
- "True"
or
- "False"

---

# Creating Boolean Values

The simplest way to use Boolean in Python is like this:

```python
is_logged_in = True
is_admin = False
```

Here we created two variables:
is_logged_in → value is True
is_admin → value is False
This means that currently, the user is logged in and the user is not an admin.
Python understands that these variables store Boolean values.

## Boolean from Comparisons

- Booleans often come from comparisons.
- A comparison checks whether something is true or false.

Example:
```python
print(5 > 3)
```

Output:
```python
True
```

Why?
- Because 5 is bigger than 3.

Another example:
```python
print(10 < 2)
```

Output:
```python
False
```

- Because 10 is not smaller than 2.

## Why Boolean is Important

- Boolean is the foundation of logic in programming.
- It allows programs to:
1. Make decisions
2. Control behavior
3. React to conditions

- Without Boolean, programs would just run from top to bottom without thinking.
- With Boolean, programs can decide what to do.