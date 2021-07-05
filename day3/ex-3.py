#Write a program that tells whether a given year is a leap year. 
#Starter code:
year = int(input("Which year do you want to check?"))
#End starter code.

if year % 4 == 0:
  if year %100 == 0:
    if year %400 == 0:
      print("It is a leap year!")
    else: print("Not a leap year.")
  else: print("It is a leap year!")
else:
  print("Not a leap year.")