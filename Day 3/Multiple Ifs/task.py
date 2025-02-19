print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child bill is $5.")
    elif age <= 18:
        bill = 7
        print("adult bill $7.")
    else:
        bill = 12
        print("Young bill $12.")
    wants_photo = input("do you want a photo enter Y or N")
    if wants_photo == "Y":
        bill += 3

    print(f"the final bill:{bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
