import random

word_list = ["ardvark", "baboon", "camel"]

#TODO-1: Choose a random word from the list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

#TODO-2: Ask the user to guess a letter and assign it to a variable called guess. Make guess lowercase.
guess = input("Guess a letter:\n").lower()

#TODO-3: Check to see if the letter the user guessed (guess) matches a letter in the chosen_word.
for letter in chosen_word:
  if letter == guess:
    print("You got it.")
  else:
    print("Wrong... ")