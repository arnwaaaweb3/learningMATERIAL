# COMPARISON OPERATORS (Python)

# Comparison operators are used to compare two values.
# The result of a comparison will always be a BOOLEAN value:
# True  -> if the condition is correct
# False -> if the condition is not correct

# --------------------------------------------------
# LIST OF COMMON COMPARISON OPERATORS
# --------------------------------------------------

# >   greater than
# <   less than
# ==  equal to
# !=  not equal to
# >=  greater than or equal to
# <=  less than or equal to


# --------------------------------------------------
# EXAMPLE 1 : GREATER THAN (>)
# --------------------------------------------------

# Let's compare two numbers:

print(10 > 5)

# The output will be:
# True
# Because 10 is greater than 5.


# --------------------------------------------------
# EXAMPLE 2 : LESS THAN (<)
# --------------------------------------------------

print(3 < 1)

# Output:
# False
# Because 3 is NOT smaller than 1.


# --------------------------------------------------
# EXAMPLE 3 : EQUAL TO (==)
# --------------------------------------------------

print(8 == 8)

# Output:
# True
# Because both numbers are exactly the same.


# IMPORTANT NOTE:

# =  is used to ASSIGN a value to a variable
# == is used to COMPARE two values

# Example of assignment:
age = 21

# Here we store the value 21 into the variable called "age"

# Example of comparison:
print(age == 21)

# Output:
# True
# Because the value of age really is 21


# --------------------------------------------------
# EXAMPLE 4 : NOT EQUAL (!=)
# --------------------------------------------------

print(5 != 2)

# Output:
# True
# Because 5 is different from 2


# --------------------------------------------------
# EXAMPLE 5 : GREATER THAN OR EQUAL (>=)
# --------------------------------------------------

print(10 >= 10)

# Output:
# True
# Because 10 is equal to 10
# And the operator >= allows BOTH:
# greater than OR equal to


# --------------------------------------------------
# EXAMPLE 6 : LESS THAN OR EQUAL (<=)
# --------------------------------------------------

print(4 <= 9)

# Output:
# True
# Because 4 is smaller than 9


# --------------------------------------------------
# USING COMPARISON OPERATORS WITH VARIABLES
# --------------------------------------------------

# Let's create a variable first

age = 20

print(age >= 18)

# Output:
# True
# Because 20 is greater than 18

# The computer checks the condition and returns True.


# --------------------------------------------------
# USING COMPARISON OPERATORS IN CONDITIONS
# --------------------------------------------------

# Comparison operators are often used in IF statements.

age = 17

if age >= 18:
    print("You are an adult.")

# In this example:
# 17 >= 18 is False

# Since the condition is False,
# the code inside the IF block will NOT run.


# --------------------------------------------------
# ANOTHER SIMPLE EXAMPLE
# --------------------------------------------------

name = "Andrew"
favorite_team = "Real Madrid"

# Let's compare the favorite team

if favorite_team == "Real Madrid":
    print(f"{name} supports Real Madrid.")
else:
    print(f"{name} does not support Real Madrid.")

# Here we used == to compare two strings.


# --------------------------------------------------
# LAST EXAMPLE
# --------------------------------------------------

temperature = 30

if temperature > 35:
    print("It's extremely hot today.")
elif temperature >= 25:
    print("The weather is warm today.")
else:
    print("The weather is cool today.")

# Here the program compares temperature values
# to decide which message should be printed.


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

# Comparison operators help the computer answer questions like:
# - Is this value bigger?
# - Is this value smaller?
# - Are these values the same?
# - Are they different?

# The result will always be:
# True or False

# And these Boolean results are very important
# for decision making in programming.