#Variable is a word that contains a value or data.
#Input is a function that takes user input from the console.

#Introduction of the AI assistant
print("Hello, my name is Robocafe!\n" 
      + "Your personal cafe AI assistant.\n")

#Ask for the name of the user
name = input("What is your name? ")
#input() is a function that takes user input from the console.
#name here is a variable that stores the user's name.
#a word without quotes is a variable, which is contain value and data.
#a word with quotes is a string, which is a value that represents text.

if name == "Robocafe": #if is a keyword that checks if a condition is true or false 
    print(f"Hey, {name} is my name! You can't use my name to order coffee here.")
    exit() #exit() is a function that stops the program from running.
else: #else is a keyword that is used when the if condition is false.
    print(f"Hello {name}!, welcome to Le Cafe Julien.\n\n"
      +"Thank you for coming in today.\n")
#(f"aaaa") is an f-string, which allows you to mix variables and strings together.
#{name} is a variable that being input by the user
#in the f-string here, I used two newlines (\n\n), one for a new line after the greeting, and another one to create a space before the next sentence.

#Define the menu as a variable
menu = ("- Americano-style\n"
        + "- Latte\n"
        + "- Cappuccino\n"
        + "- Espresso\n"
        + "- Macchiato\n"
        + "- Matcha\n"
        + "- Hot Chocolate\n"
        + "- Tea\n"
        + "- Milktea\n"
        + "- Flat-White\n"
        + "- Cafe au Lait\n"
        + "- Cold Brew\n"
        + "- Affogato\n"
        + "- Frappucino\n"
        + "- Ristretto\n"
        + "- Cortado\n"
        + "- Irish Coffee\n"
        + "- Doppio\n"
        + "- Breve\n"
        + "- Piccolo Latte\n"
        + "- Red Eye\n"
        + "- White Coffee\n"
        + "- Nitro Cold Brew\n"
        + "- Vietnamese Coffee\n"
        + "- Lungo\n"
        + "- Mocha\n")
#\n is a newline character, which should be located at the end of each line but before the quotation mark.
#\n can be multiplied like this: \n\n\n, which will create three new lines below.

#Robocafe will ask the user what they would like to order, based on the menu definition
print(f"Here is our menu:\n" + menu)
print(name + ", what would you like to order today? ")
order = input()
print()
#here, name and menu are already defined variables, so we can use them directly.
#order is a variable that stores the user's order.
#If there's no string in the input, just simply leave it empty, like this: input().
#If you want to add a prompt, you can do it like this: input("What would you like to order? ").

#Define different prices for each order:
# Assume 'order' and 'name' variables are defined elsewhere based on user input.

if order == "Americano-style":
    # If the user's order is "Americano-style", then the price will be $4.50.
    price = 4.50  # floating-point number for price
    print("Ah, an Americano-style! A perfect choice if you love a straightforward, bold coffee with a clean finish.\n")
    #here, I add a personalized comment if the user's order is "Americano-style".

elif order == "Latte":
    # elif is a keyword that means "else if", used to check if the user's order is "Latte".
    price = 5.00  # floating-point number for price
    print(f"A Latte? excellent choice {name}! A smooth, comforting, and creamy coffee experience.\n")
    #here, I add a personalized comment if the user's order is "Latte",

elif order == "Cappuccino":
    # Checks if the user's order is "Cappuccino".
    price = 5.00  # floating-point number for price
    print(f"Cappuccino it is, {name}! You're clearly a fan of that beautiful, frothy milk and balanced coffee flavor, huh?\n")
    #here, I add a personalized comment if the user's order is "Cappuccino".

elif order == "Espresso":
    # Checks if the user's order is "Espresso".
    price = 3.50  # floating-point number for price
    print(f"Hey, that a strong choice! Direct and to the point, a greatquick, powerful coffee hit, {name}.\n")
    #here, I add a personalized comment if the user's order is "Espresso".

elif order == "Macchiato":
    # Checks if the user's order is "Macchiato".
    price = 4.00  # floating-point number for price
    print(f"Wonderful, {name}! Macchiato, a strong coffee with just a kiss of milk to mellow it out. A very smart pick!\n")
    #here, I add a personalized comment if the user's order is "Macchiato".

elif order == "Matcha":
    # Checks if the user's order is "Matcha".
    price = 5.50  # floating-point number for price
    print(f"Feeling for something vibrant and green, eh {name}? The flavor of matcha is just right, the balance between smooth and sweetness.\n")
    #here, I add a personalized comment if the user's order is "Matcha".

elif order == "Hot Chocolate":
    # Checks if the user's order is "Hot Chocolate".
    price = 4.50  # floating-point number for price
    print(f"A delightful choice for comfort and sweetness, {name}. Perfect for warming up! You've picked perfectly!\n")
    #here, I add a personalized comment if the user's order is "Hot Chocolate".

elif order == "Tea":
    # Checks if the user's order is "Tea".
    price = 3.50  # floating-point number for price
    print(f"Tea, how lovely, {name}! A classic and calming choice. Always a good decision!\n")
    #here, I add a personalized comment if the user's order is "Tea".

elif order == "Milktea":
    # Checks if the user's order is "Milktea".
    price = 4.75  # floating-point number for price
    print(f"Milktea! A refreshing and sweet treat, {name}. Perfect for a chill afternoon!\n")
    #here, I add a personalized comment if the user's order is "Milktea".

elif order == "Flat-White":
    # Checks if the user's order is "Flat-White".
    price = 5.25  # floating-point number for price
    print(f"A Flat-White! You know your coffee, {name}! You love your espresso front and center, beautifully blended with velvety milk. Excellent pick!\n")
    #here, I add a personalized comment if the user's order is "Flat-White".

elif order == "Cafe au Lait":
    # Checks if the user's order is "Cafe au Lait".
    price = 4.75  # floating-point number for price
    print(f"A charming, classic choice, {name}. Simple, comforting, and perfect for a relaxed start or a cozy break.\n")
    #here, I add a personalized comment if the user's order is "Cafe au Lait".

elif order == "Cold Brew":
    # Checks if the user's order is "Cold Brew".
    price = 5.75  # floating-point number for price
    print(f"Excellent choice for a smooth, low-acid, and naturally sweet coffee, {name}. Super refreshing!\n")
    #here, I add a personalized comment if the user's order is "Cold Brew".

elif order == "Affogato":
    # Checks if the user's order is "Affogato".
    price = 6.00  # floating-point number for price
    print(f"Affogato? Such a fun and decadent choice, {name}. The perfect marriage of hot espresso and cold ice cream.\n")
    #here, I add a personalized comment if the user's order is "Affogato".

elif order == "Frappuccino":
    # Checks if the user's order is "Frappuccino".
    price = 6.50  # floating-point number for price
    print(f"Going for something fun, frosty, and sweet, I see, {name}! Perfect for a refreshing treat. A fantastic choice!\n")
    #here, I add a personalized comment if the user's order is "Frappuccino".

elif order == "Ristretto":
    # Checks if the user's order is "Ristretto".
    price = 3.75  # floating-point number for price
    print(f"You're really diving deep into the essence of coffee, {name}! This short, intense shot is packed with flavor. A delightful pick!\n")
    #here, I add a personalized comment if the user's order is "Ristretto".

elif order == "Cortado":
    # Checks if the user's order is "Cortado".
    price = 4.25  # floating-point number for price
    print(f"Ohh.. You appreciate balance, the harmony of espresso and just enough steamed milk, {name}. Good choice!\n")
    #here, I add a personalized comment if the user's order is "Cortado".

elif order == "Irish Coffee":
    # Checks if the user's order is "Irish Coffee".
    price = 7.00  # floating-point number for price
    print(f"A unique and warming choice, {name}, perfect for a little indulgence.\n")
    #here, I add a personalized comment if the user's order is "Irish Coffee".

elif order == "Doppio":
    # Checks if the user's order is "Doppio".
    price = 4.00  # floating-point number for price
    print(f"A Doppio! Double the espresso, double the kick, {name}!\n")
    #here, I add a personalized comment if the user's order is "Doppio".

elif order == "Breve":
    # Checks if the user's order is "Breve".
    price = 5.75  # floating-point number for price
    print(f"You're treating yourself to something extra rich and creamy today, huh {name}! Made with half-and-half, it's wonderfully decadent.\n")
    #here, I add a personalized comment if the user's order is "Breve".

elif order == "Piccolo Latte":
    # Checks if the user's order is "Piccolo Latte".
    price = 4.75  # floating-point number for price
    print(f"A small but mighty choice, {name}! You get the intensity of espresso with just a splash of milk. Piccolo Latte, yes!\n")
    #here, I add a personalized comment if the user's order is "Piccolo Latte".

elif order == "Red Eye":
    # Checks if the user's order is "Red Eye".
    price = 6.00  # floating-point number for price
    print(f"Red Eye? Wow, {name}, you're in for a serious caffeine boost! Coffee with a shot of espresso! you're ready to conquer anything today!\n")
    #here, I add a personalized comment if the user's order is "Red Eye".

elif order == "White Coffee":
    # Checks if the user's order is "White Coffee".
    price = 5.50  # floating-point number for price
    print(f"White Coffe? An interesting choice, {name}. It's lightly roasted, giving it a unique nutty flavor and usually more caffeine.\n")
    #here, I add a personalized comment if the user's order is "White Coffee".

elif order == "Nitro Cold Brew":
    # Checks if the user's order is "Nitro Cold Brew".
    price = 6.25  # floating-point number for price
    print(f"Ohh, Going for that silky smooth, cascading texture and rich flavor, I see, {name}! It's like a beer but coffee.\n")
    # Personalized comment for a "Nitro Cold Brew" order.

elif order == "Vietnamese Coffee":
    # Checks if the user's order is "Vietnamese Coffee".
    price = 5.75  # floating-point number for price
    print(f"A beautifully sweet and strong choice, {name}. The condensed milk perfectly complements the bold coffee.\n")
    #here, I add a personalized comment if the user's order is "Vietnamese Coffee".

elif order == "Lungo":
    # Checks if the user's order is "Lungo".
    price = 4.00  # floating-point number for price
    print(f"Oh, you want a longer pull on your espresso, huh? giving it a slightly different, extended flavor profile? {name}, you have a thoughtful choice!\n")
    #here, I add a personalized comment if the user's order is "Lungo".

elif order == "Mocha":
    # Checks if the user's order is "Mocha".
    price = 5.50  # floating-point number for price
    print(f"A perfect blend of rich chocolate and bold coffee. A sweet and energizing pick!, {name}\n")
    #here, I add a personalized comment if the user's order is "Mocha".

else:
    # If the order does not match any of the above, this message is displayed.
    print("Sorry, that's not on our menu. Please choose from our available options.")
    # Generic message for an unrecognized order.

quantity = input("How many " + order + " would you like to order, " + name + "? \n") #string
print()
#quantity here is a variable that contains string and order variable.
#i add the order variable inside, to automatically add the user's order to the string.

#Robocafe notes the order and asks the user to wait
total = price * int(quantity) #because quantity is a string, we need to convert it to an integer using int().
print("Perfect " + name + "!, your " + quantity + " " + order + " will be ready in a moment.")
print(f"That will be $" + str(total) + " in total.\n") #this (total) is still an integer, so we need to convert it to a string using str().
#print here is a function that prints output to the console. () is what inside the print function itself.
#"Perfect " is a string, a text. Do notice that i put a space after the word Perfect, so that the output will be more readable.
#"!, your " is also a string, a text. I also put a space after the word your, so that the output have some space between your and order (variable).
#order is what the user inputted.
#" will be ready in a moment." is a string, a text. I also put a space after the word will, so that there's a space between order (variable) and will.
#str() is a function that converts an integer to a string, so that it can be printed as text.
#int() is a function that converts a string to an integer, so that it can be used in calculations.
