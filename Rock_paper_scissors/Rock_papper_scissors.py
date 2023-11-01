import random
""" A module that import a random value of 0 or 1 for each execution time
"""
computer_choice = random.randint(0, 2)
print(computer_choice)

print(f"\t\t\t\t\t\t\t\t\tWelcome to [ROCK, PAPPER SCISSOR] Game")
print()

print(f"\t\t\t\t\t\t\t=============================================================================")
print()
print(f"\t\t\t\t\t\t\t\tGame Rules: ", end="")

print(f"""\t1. Rock wins against scissors
\t\t\t\t\t\t\t\t\t\t2. Scissors wins against papper
\t\t\t\t\t\t\t\t\t\t3. Papper wins against rock""",)
print()
print(f"\t\t\t\t\t------------------------------------------------------------------------------------------------------------------")
print()
user_choice = int(input(f"\t\t\tSelect your option for this round [Rock / papper / scissors]: "))
print()

if computer_choice == 2 and user_choice == 0:
   print("computer won this round")
elif user_choice == 2 and computer_choice == 0:
    print("user won this round")
elif user_choice > computer_choice:
    print("You won this around")
elif computer_choice > user_choice:
    print("computer won this round")

elif user_choice == computer_choice:
    print("its a tie you draw")


print(computer_choice)