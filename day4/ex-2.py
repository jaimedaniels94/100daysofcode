import random
#Write a program to select a random name out of a list. 
#Starter code:
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#End starter code.

random_index = random.randint(0, len(names) - 1)

print(f"{names[random_index]} is going to buy the meal today!")