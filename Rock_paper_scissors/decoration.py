""" THis is just the decration page of Game that is been imported to Rock_paper_scissors from page
"""
print()
print(f"\t\t\t\t\t\t\t\t\tWelcome to [ROCK, PAPER SCISSOR] Game")
print()
print("codeded by Tee")
print(f"\t\t\t\t\t\t\t=============================================================================")
print()
print(f"\t\t\t\t\t\t\t\tGame Rules: ", end="")

print(f"""\t1. Rock wins against scissors
\t\t\t\t\t\t\t\t\t\t2. Scissors wins against papper
\t\t\t\t\t\t\t\t\t\t3. Papper wins against rock""",)
print()
print(f"\t\t\t\t\t------------------------------------------------------------------------------------------------------------------")
print()

def check(choice):
    user_choice = None
    if choice == 'rock':
        user_choice = 0
    elif choice == 'paper':
        user_choice = 1
    elif choice == "scissors":
        user_choice = 2
    return user_choice
