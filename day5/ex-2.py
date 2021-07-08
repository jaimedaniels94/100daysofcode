#Write a program that finds the highest number in a list of numbers without using max or min functions.
#Starter code:
student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
#End starter code.

highest = 0

for score in student_scores:
  if score > highest:
    highest = score


print(f"The highest score in this list is {highest}")