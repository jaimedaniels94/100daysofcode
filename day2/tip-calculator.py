print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people will split the bill? "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / split

final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount})

