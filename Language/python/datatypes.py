#A number in Python is called an integer if it is a whole number, meaning it does not have a decimal point.

#Defining variable here
name = "Nolan"
age = 21
height = 164.57
weight = 56.70
pet = ["cat", "fish", "bird"]


print(f"{name} is {age} years old.")
print(f"{name} is {height} cm tall.")
print(f"{name} weighs {weight} kg. \n")
#again, we use f-string to mix the variable with the string.
#because the name is defined as a fixed string, it will always be "Nolan" unless we change the code.
#because the age is defined as a fixed integer, it will always be 20 unless we change the code.
#because the height is defined as a fixed float, it will always be 164.57 unless we change the code.
#because the weight is defined as a fixed float, it will always be 56.70 unless we change the code.

print("There are many types of data in Python, such as:")
print(type(name))
print(type(age))
print(type(height))
print(type(name == "Nolan"))
print(type(pet))
print()
#type() is a function to tell you the type of the variable.
#but it won't print anything to the console, so you need to use print() to see the result.
#print() can also be used as a space between paragraphs, because it means you dont want to print anything, just a new line.

#Now, let's do some math with the variables
equation = height * age
print(f"1. What is {height} times {age} equal to?")
print(f"The answer is: {equation}")
print(type(equation))
print()
#here, we're using equation as a variable to store the result of the multiplication.
#python can also authomatically calculate the result of the multiplication, so you don't have to do it manually.
#use asterisk * to multiply, slash / to divide, plus + to add, and minus - to subtract. ** to eskponentiate (pangkat).
#you can also use parentheses () to group the operations, like this: (height * age) + 10.

#"Yes, That's right!" = True
#"No, That's wrong!" = False
print(f"2. Is 4 times 9 equal to 38 ?")
if 4 * 9 == 38 == True: 
    print("Yes, That's right!")
else:
    print("No, That's wrong!")
print(f"The answer is {4 * 9}\n")
#here, we're using if statement to check if the equation is right or wrong.
#our rule is: if 4 x 9 = 38, then the code will be executed and the message will be printed.
#however, if the equation is wrong, then the "else" part will be executed and the message will be printed.
