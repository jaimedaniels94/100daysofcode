import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
word_length = len(chosen_word)
for l in range(word_length):
  display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False
while not end_of_game:
  guess = input("Guess a letter:\n").lower()

  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter


  print(display)
  if "_" not in display:
    end_of_game = True