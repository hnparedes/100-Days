print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
tip_percent = tip / 100
total_amount = tip_percent * bill
total_bill = bill + total_amount
total_person = total_bill / split
total_sum = round(total_person, 2)
print(f"Each person should pay: ${total_sum}")
