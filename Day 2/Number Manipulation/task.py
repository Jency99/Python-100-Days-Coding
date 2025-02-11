bmi = 84 / 1.65 ** 2

print(bmi)

print(int(bmi)) # Floor to whole number

print(round(bmi)) # round off the whole number based on the first decimal didgit

print(round(bmi,2)) # specify on how many digits we need after floating point

# Assignment operator =+, -+, *=, /+
score = 0
score += 1
print(score)

is_win = True

# F string
print(f"The bmi is {bmi}, your score is {score} and you are {is_win}")


