import random
from unittest import result

# print welcome message
print(" Welcome to the the rock paper scissors game")
# print multiline game instruction
print(" Winning rules for the game are:  \n"
      + "Rock vs paper -> paper wins \n"
      + "Scissors vs paper -> scissors wins \n"
      + "rock vs scissors -> rock wins \n")

while True:
    print("Enter choice \n 'r' for rock, \n 'p' for paper, and \n 's' for scissors  ")

    # take user input
    choice = input("My input is : ")
    choice.lower()

    if choice != 'r' 'p' 's':
        print("You have entered an invalid input")
        choice = input("Enter a valid input")
    else:
        continue

# Initializig choice_name variable
    if choice == 'r':
        choice_name = 'Rock'
    elif choice == 'r':
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print("Your choice is" + choice_name)
    print("\n Now it is the computers turn")
    comp_choice = random.choice(['r', 'p', 's'])

    # looping comp_choice until it becomes equal to choice

    while comp_choice == choice:
        comp_choice = random.choice(['r', 'p', 's'])

# intializing the value of comp_choice_name
    if comp_choice == 'r':
        comp_choice_name = 'Rock'
    elif comp_choice == 'p':
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

# Check for a draw
    if choice == comp_choice:
        print("Draw=> ", end="")
        result = "Draw"

    # condition for winning
    if((choice == 'r' and comp_choice == 'p') or
       (choice == 'p' and comp_choice == 'r')):
        print("paper wins => ", end="")
        result = "paper"

    elif((choice == 'r' and comp_choice == 's') or
            (choice == 's' and comp_choice == 'r')):
        print("Rock wins =>", end="")
        result = "Rock"
    else:
        print("scissor wins =>", end="")
        result = "scissor"

    if result == "Draw":
        print("<== Its a tie ==>")
    if result == choice_name:
        print("\n <== User wins ==>")
    else:
        print("\n <== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input().lower

    if ans == 'n':
        break

    print("\n Thank you for playing")
