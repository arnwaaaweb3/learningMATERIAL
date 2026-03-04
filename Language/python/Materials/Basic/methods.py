#Here, we will learn about methods.
#But first! let's define a variable here:
name = "Selena"
age = 14
classmate = ["Trevor", "Ainsley", "David", "George",
             "Eliza", "Arthur", "Cassie", "Elbert",
             "Isabella", "Lisa", "Kevin", "Caitlyn",]

#let say, Selena today has a transfer classmate in her class.
#to add a new value to the list, we can use .append() method,
#.append can only add one value at a time to the list.
new_friend = "Gavin"
classmate.append(new_friend)
print(name+ "'s classmate are: " + (str(classmate) + "\n"))
#here, we add concatination to the list + switch the list to string using str() method.
#here, we add Gavin as her new classmate, a transfer student.

#let's say, Selena has more subjects to learn in her class.
#here we add a new variable (subject) to learn in the class.
#here, if we want to add more than one value to the list, we can use .extend() method.
#.extend() can add more than one value at a time to the list.
subject = ["mathematics", "citizenship", "english",]
subject.extend(["history", "biology", "chemistry", "physics"])
#actually, you can also write it like this:
#subject = subject + ["history", "biology", "chemistry", "physics"]
print(name+"'s subjects are: " + (str(subject) + "\n"))
#here, we add another concatination to our list + switch the list to string using str() method.

#this is the other variation that i mean:
hobbies = ["hiking", "swimming", "learning new things"]
#says that Selena loves baking and cycling recently.
hobbies = hobbies + ["baking", "cycling"]
print(name+"'s hobbies are: " + (str(hobbies) + "\n"))
#here, we add another concatination to our list + switch the list to string using str() method.