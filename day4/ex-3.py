#Make a treasure map that marks an x according to row and column, rather than index.
#first number is vertical column, second it horizontal row.
#starter code:
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#End starter code.
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"


#Starter code:
print(f"{row1}\n{row2}\n{row3}")
#End starter code.