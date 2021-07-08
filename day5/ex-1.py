#Build a program without len() or sum() to find the average height, given a list of heights.
#Starter code:
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#End starter code.
added_heights = 0
num_heights = 0
for height in student_heights:
  added_heights += height
  num_heights += 1

avg_height = round(added_heights / num_heights)

# print(added_heights)
# print(num_heights)
print(avg_height)