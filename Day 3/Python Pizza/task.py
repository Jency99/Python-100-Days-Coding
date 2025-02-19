print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
bill = 0

if size == "S":
    bill += small_pizza_price
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += medium_pizza_price
    if pepperoni == "Y":
        bill += 3
else:
    bill += large_pizza_price
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")