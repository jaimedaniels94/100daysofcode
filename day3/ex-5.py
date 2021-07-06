#Build a program that calculates love connection based on how many letters of the subjects' names occure in TRUE and LOVE
#Starter code:
print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#End starter code. 

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

true_points = name1.count("t")
true_points += name2.count("t")
true_points += name1.count("r")
true_points += name2.count("r")
true_points += name1.count("u")
true_points += name2.count("u")
true_points += name1.count("e")
true_points += name2.count("e")

love_points = name1.count("l")
love_points += name2.count("l")
love_points += name1.count("o")
love_points += name2.count("o")
love_points += name1.count("v")
love_points += name2.count("v")
love_points += name1.count("e")
love_points += name2.count("e")

score = str(true_points) + str(love_points)

if int(score) < 10 or int(score) > 90:
  print(f"Your score is {score}. You go together like mentos and coke. Explosive.")
elif int(score) >= 40 and int(score) <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}, you're probably not gonna last. Sorry")