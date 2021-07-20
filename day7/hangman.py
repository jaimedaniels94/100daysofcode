import random
from hangman_art import logo, stages
from hangman_words import word_list



end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

# Create blanks
display = []
for l in range(word_length):
  display += "_"


while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    if guess in display:
      print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
      

    if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        end_of_game = True
        print("You lose.")

    print(f"{' '.join(display)}")
    
    if "_" not in display:
      end_of_game = True
    
    print(f"{stages[lives]}")