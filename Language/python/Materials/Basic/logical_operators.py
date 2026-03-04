#Logical Operators
# IF & ELSE

#if is a keyword that checks if a condition is true or false (or we call it a boolean value).
#else is a keyword that is used when the if condition is false.
#so "if" condition is true, it will execute the code inside the if block.
#If the condition is false, it will execute the code inside the else 
#= is an operator to assign a value to a variable.
#== is an operator to compare two values, and it returns True if they are equal, or False if they are not.

# Defining variable for Andrew here:
name = "Andrew" #his name is Andrew
age = 34 #his age is 34
occupation = "Salesman" #his occupation is Salesman
workplace = "Adira Assurance" #he works at Adira Assurance
skills = ["Sales", "Marketing", "Customer Service", "Communication"]
#using [] (list) to define a list of his skills.
#use [] to define a list, which is a collection of items that can be of any data type.

#Defining variable for eligibly work at Adira Assurance here:
minimum_age = 19 #let's say the minimum age for the job is 19, so if the age is less than 19, they're not eligible to work here.
maximum_age = 50 #let's say the maximum age for the job is 45, so if the age is more than 45, they're too old to work here.
skills_required = ["Sales", "Marketing", "Customer Service", "Communication"] 
#using [] (list) to define a list of required skills for the job.
#skills must have the exact same value as skills_required to be eligible for the job. 

# If and else statement example
if age > maximum_age or age < minimum_age: #let's say the age limit for the job is 45, if the age is less than 45, then this message will be printed.
    #use "or" to add another rule into the if statement.
    #if you use "or", the code will be executed if one of the rules are met!
    print(f"{name} is not eligible to work at {workplace} as a {occupation}.")
    #f-string here because we want to mix variables and strings together.
else: #so if the age is not less than 45, then this message will be printed.
    print(f"{name} is eligible to work at {workplace} as a {occupation} anymore.")

if skills == skills_required:
        print(f"{name} has the required skills to work at {workplace} as a {occupation}.\n")
        #this will be printed if the skills variable (Andrew) are met, which is the same as skills_required.
else:
        print(f"{name} does not have the required skills to work at {workplace} as a {occupation}.\n")
        #this will be printed if the skills variable (Andrew) are not met, which is not same as skills_required.

#Defining variable for other random person here:
name2 = "Marlina" #her name is Marlina
age2 = 27 #She is 27 years old
occupation2 = "Cashier" #let's say she's a cashier
workplace2 = "K-9 Mart" #She's working at K-9 Mart
skills2 = ["Communication", "Customer Service", "Accounting", "Cashier"] #define Marlina's skills here.
#use [] (list) to define a list of her skills.
#use [] to define a list, which is a collection of items that can be of any data type.

#Let's define the criteria to work in K-9 Mart as a Cashier here:
minimum_age2 = 20 #say K-9 Mart doesn't want to hire underage.
maximum_age2 = 45 #say that above 45 is too old for a cashier.


#Here, let's try to use "or", "and", "if", "elif", "else", "in" and "if not"
#Let's make a fictive variable here:
if not name2 == "Brandon": #the code will be executed if the name2 variable isn't Brandon.
    print(f"This is the story of {name2}, not Brandon. Wait, who's Brandon?") #Giving vibes like a story narrator!
    if name2 == "Marlina": #the code will be executed if the name2 variable is Marlina.
        print(f"This is {name2}, She is a {occupation2} at {workplace2}.\n") #Now, it's Marlina story!
    else: #this is if the name2 variable isn't Marlina, then we tell the user it should be Marlina's story.
        print("This should be Marlina's story.\n") #Reminder for the user.

#Filtering by the minimum and maximum age here:
if age2 < maximum_age2 or age2 > minimum_age2: #since we used "or", the code will be executed if one of the rules are met.
    print(f"{name2} is still eligible to work at {workplace2} as a {occupation2}.\n") #This is a statement that Marlina met the rules to work in K-9 Mart.
else: #this is if the age2 variable is more than 45, or less than 20, then he/she is not eligible to work in K-9 Mart.
    print(f"{name2} is not eligible to work at {workplace2} as a {occupation2} anymore.\n")

#Filtering by the skills required, to check if Marlina can work in Adira Assurance?
if skills2 == skills_required: #the code will be executed if the skills2 variable is the same as skills_required.
    print(f"{name2} has the required skills to work at {workplace} as a {occupation}.") #Marlina has the required skills to work in K-9 Mart.
else: #this is if the skills2 variable isn't the same as skills_required, then he/she doesn't have the required skills.
    print(f"{name2} does not have the required skills to work at {workplace} as a {occupation}.") #Mar

#Filtering by the skills required, to work in K-9 Mart as a Cashier
if "Cashier" in skills2: #the code will be executed if the skills2 variable contains "Cashier".
    print(f"{name2} can be a cashier at {workplace2}.\n") #if Marlina skills2 contains "Cashier", it will execute this message and skip the rest.
elif "Accounting" in skills2: #the code will be executed if the skills2 variable contains "Accounting".
    print(f"{name2} can also do some accounting at {workplace2}.\n") #if Marlina skills2 contains "Accounting", it will execute this message and skip the rest.
elif "Customer Service" in skills2: #the code will be executed if the skills2 variable contains "Customer Service".
    print(f"{name2} can also serve a customer at {workplace2}.\n") #if Marlina skills2 contains "Customer Service", it will execute this message and skip the rest.
elif "Communication" in skills2: #the code will be executed if the skills2 variable contains "Communication".
    print(f"{name2} is a good communicator at {workplace2}.\n") #if Marlina skills2 contains "Communication", it will execute this message and skip the rest.
else: #this is if the skills2 variable doesn't contain "Cashier", "Accounting", "Customer Service" or "Communication", then he/she can't do anything.
    print(f"{name2} can't do anything to be a {occupation2} at {workplace2}.\n")
#always remember that elif functional is to pivot from the first if statement. if the first statement is true, it will skip the rest of the elif statements.
#try to delete any string in skills2 variable to see what will happen.

#New variable:
favorite_football_team = "Real Madrid"
if favorite_football_team != "Bayern Munich": #Here we can use "!=" to check if the value of the variable is different from the value we want.
     print(f"{name} likes {favorite_football_team} better than Bayern Munich.\n")
else:
     print(f"{name} likes Bayern Munich better than {favorite_football_team}.\n")
#so the logic of "!=" is like this:
#if the value of the variable is not the same as the value we want, then the code will be executed, else the code will be skipped.
#if the value of favorite_football_team is Real Madrid, then the code will be ignored, and the else statement will be executed.
#it's like the inverse of "==" operator! h