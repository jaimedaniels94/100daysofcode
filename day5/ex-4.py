#Write a program that prints the solution to FizzBuzz.
#Rules:
#If number is divisible by 3, print "Fizz"
#If number is divisible by 5, print "Buzz"
#If number is divisible by 3 and 5, print "FizzBuzz"

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

  