print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to treasure island.")
print("Your mission is to find the bootey.")
left_or_right = input("You're at a crossroads, would you like to go left or right? ")
if left_or_right == "left":
  swim_or_walk = input("You arrive at a lake, walk along the shoreline or swim? Type walk or swim. ")
  if swim_or_walk == "walk":
    red_yellow_blue = input("There are three doors. Red, yellow or blue? ")
    if red_yellow_blue == "yellow":
      print("You found the bootey! YOU WIN!")
    elif red_yellow_blue == "red":
      print("Burned by fire, you lose.")
    elif red_yellow_blue == "blue": 
      print("Eaten by blue beasts, you lose.")
    else: 
      print("You lose.")
  else: 
    print("You got eaten by piranhas.")
else:
  print("You fell in a hole.... GAME OVER.")
  