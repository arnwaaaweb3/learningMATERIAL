# Python List

A **list** is one of the most commonly used data types in Python.

A list is basically **a collection of multiple values stored in one variable**.

Instead of creating many variables like this:

```python
skill1 = "Sales"
skill2 = "Marketing"
skill3 = "Communication"
skill4 = "Customer Service"
```
We can store them inside one list:

```python
skills = ["Sales", "Marketing", "Communication", "Customer Service"]
```

This is much cleaner and easier to manage.

---

## How to Create a List

In Python, lists are created using square brackets [].

- Example:
```python
fruits = ["Apple", "Banana", "Orange"]
```

- Here we created a list called fruits.
- The items inside the list are:
1. Apple
2. Banana
3. Orange

- Each item is separated by a comma.

---

## Lists Can Store Different Data Types

A list can contain **many types of data, not just strings.**
Example:
```python
random_data = ["Andrew", 34, True, 72.5]
```
This list contains:
- a string
- an integer
- a boolean
- a float

Python allows this flexibility.

---

## Accessing List Items (Index)

- Each item inside a list has a position called an index.

**Important rule:**
- Python starts counting from 0, not 1.

Example list:
```python
skills = ["Sales", "Marketing", "Customer Service", "Communication"]
```
- Index positions:
Index -> Value
0	-> Sales
1	-> Marketing
2	-> Customer Service
3	-> Communication

Example:
```python
print(skills[0])
```

Output:
- Sales

Because index 0 is the first item.
