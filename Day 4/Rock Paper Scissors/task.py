import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock,paper,scissors]
your_choice = int(input("What do you want to choose? 0 for Rock,1 for paper,2 for scissor"))
computer_choice = random.randint(0,2)
print("your choose", choice[your_choice])
print("computer choice",choice[computer_choice])

if your_choice == computer_choice:
    print("Draw")
else:
    if choice[your_choice] == rock:
        if choice[computer_choice] == paper:
            print("you lose")
        else:
            print("you win")
    elif choice[your_choice] == paper:
        if choice[computer_choice] == rock:
            print("you win")
        else:
            print("you lose")
    else:
        if choice[computer_choice] == paper:
            print("you win")
        else:
            print("you lose")