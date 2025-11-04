#Lists are a collection of items in a group.

#Let's try by defining a list of shopping list:
name = "Gerald"
friend = "Melissa"
shopping_list = ["eggs", "apples",
                "groceries", "milk",
                "shampoo", "soap",
                "toothpaste", "jello",
                "first aid kit", "whipcream",
                "frying oil", "seasoning powder",
                "sunscreen", "moisturizer",
                "chicken thighs", "bananas"]
shop_time = "morning"

print(name + "'s shopping list are " + str(shopping_list) + "\n")
#here, i'm using a regular () instead of f-string here, for a variation
#don't forget to use the str() function here, as it's a list, so it's not a string. We need to convert it to a string
print(type(shopping_list))
print()
#by using [] - opeing and closing square brackets, we define a list of items, and store it as a variable.
#the class is automatically set to be a list.
#list [] can also store other than strings, like integers, floats, and booleans.

#the list is ordered, which means the items are arranged in a specific order.
print(f"{name} wants to buy {shopping_list[4]} in the minimarket nearby his apartment.")
#so here, we're using f-string followed by {} to mix the variable with the string.
#so list items start counted from 0, the order process would be 0, 1, 2, 3, 4, etc.
#eggs on the list is the first item, but in python it counted as 0 because it's in the list.
#here, shopping_list[4] is the fifth item on the list, so it's shampoo.

#using if not logic here
if not shop_time == "night":
    print(f"{name} is going to buy {shopping_list[1]} not in the night, but in {shop_time}.")
else:
    print(f"Maybe, {name} is going to buy {shopping_list[1]} in the night.")
#as you can see, the [1] is actually the second item on the list, so it's apples.
#if the shop_time equals to "night", then it will print the message that {name} is going to buy {shopping_list[1]} in the night.
#else, it will print the message that {name} is going to buy {shopping_list[1]} not in the night.


#using if logic here
if friend == "Gabriel":
    print(f"Gabriel can help {name} to buy {shopping_list[2]}")
else:
    print(f"Gabriel can't help {name} to buy {shopping_list[2]}, but {friend} can help.\n")
#here, shopping_list[2] is the third item on the list, so it's groceries.

#let's make a new variable here
zoo_name = "Wildwest Perth Zoo"
zoo_animals = ["lions", "bears", "giraffes", "zebras", "elephants"
               "koalas", "kangaroos", "ostriches", "snakes", "pandas"]

print(f"After {name} and {friend} buy {shopping_list[2]}, they both go to {zoo_name} to see some {zoo_animals[-2]}.")
print(str(zoo_name) + " has a newborn of " + zoo_animals[-2] + ", called 'Nora'. She's beautiful!\n")
#if we try to print[-1] here on zoo_animals list, it will print the last item on the list.
#so, negative indexing will start counting items from behind, and not started by 0, because there is no -0.
#here zoo_animals[-2] is the second last item on the list, so it's snakes.

