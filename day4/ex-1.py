#Create a coin toss program.
import random

random_num = random.randint(0, 1)

if random_num == 0:
  print("You flipped heads!")
elif random_num == 1:
  print("You flipped tails!")