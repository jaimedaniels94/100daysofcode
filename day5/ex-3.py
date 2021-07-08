#Add the sum of all even numbers, including 1 and 100

total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number

print(total)


#How Angela did it:

total = 0

for number in range(2, 101, 2):
  total += number
print(total)