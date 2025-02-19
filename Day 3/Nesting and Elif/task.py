print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("enter your age"))
    if age <= 12:
        print("pay 5")
    elif age >= 18:
        print("Pay 20")
    else:
        print("pay 30")
else:
    print("Sorry you have to grow taller before you can ride.")
