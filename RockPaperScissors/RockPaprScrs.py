#This is a Rock-Paper-Scissors task in python3 using the random module and its choice function
#The player goes against the machine's CPU in one iteration only.

import random


user_action = input("Enter a choice R for Rock, P for paper and S for Scissors)\n")
posible_action = ["R", "P", "S"]
CPU_action = random.choice(posible_action)
while user_action not in posible_action:
    print("Invalid choise. Please try again")
    user_action = input("Enter a choice R for Rock, P for paper and S for Scissors): ")
print(f"\nYou choose {user_action}, computer choose {CPU_action}.\n")

if user_action == CPU_action:
    print(f"Both players selected {user_action}, It's a draw\n")
elif user_action == "R":
    if CPU_action == "S":
        print("Rock smash scissors! You win!\n")
    else:
        print("Paper covers Rock. You lose\n")
elif user_action == "P":
    if CPU_action == "R":
        print("Paper covers Rock. You win!\n")
    else:
        print("Scissors cut paper. You lose\n")
elif user_action == "S":
    if CPU_action == "P":
        print("Scissors cut paper. You win\n")
    else:
        print("Rock smash Scissors. You lose\n")
