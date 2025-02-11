print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
bill_percent = bill * tip_percent
total_bill = bill + bill_percent
split_bill = total_bill / people
round_split_bill = round(split_bill,2)
print(f"Each person should pay ${round_split_bill}")
