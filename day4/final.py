#Build a program to play rock, paper, scissors against the computer.
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii = [rock, paper, scissors]
print("READY TO ROCK, PAPER, SCISSORS?")
player_num = int(input("Choose your weapon. \n0 for rock, 1 for paper, or 2 for scissors.\n"))
print(f"You chose:\n{ascii[player_num]}")
computer_num = random.randint(0, 2)
print(f"Computer chose:\n{ascii[computer_num]}")


if player_num == 0 and computer_num == 2:
  print("You win!")
elif player_num == 2 and computer_num == 1:
  print("You win!")
elif player_num == 1 and computer_num == 0:
  print("You win!")
elif player_num == computer_num:
  print("It's a draw. Play again.")
elif player_num > 2:
  print("Invalid entry. Play again.")
else:
  print("You lose. Hahah you lost to a computer.")