import random
import decoration
import ASCII_art
import shutil

""" basicall center our program to the center"""
def print_center(text):
    terminal_width = shutil.get_terminal_size().columns
    print(text.center(terminal_width))

life = 3
computer = 3
winning_p = 0
winning_c = 0
Select = ['rock', 'paper', 'scissors']

while life != 0 and computer != 0:
    print(f"Life scores - Your current life = {life}, computer = {computer}")
    _choice = random.choice(Select)
    computer_choice = decoration.check(_choice)
    print()
    choice = input("\t\tSelect your option for this round [Rock / Paper / Scissors]: ").lower()
    user_choice = decoration.check(choice)

    print()

    user_hand_name = choice.capitalize() + " Hand"
    computer_hand_name = _choice.capitalize() + " Hand"

    user_hand = ASCII_art.hands[choice].splitlines()
    computer_hand = ASCII_art.hands[_choice].splitlines()

    # Ensuring both hands have the same number of lines for alignment 
    max_lines = max(len(user_hand), len(computer_hand))
    user_hand += [' ' * len(user_hand[0])] * (max_lines - len(user_hand))
    computer_hand += [' ' * len(computer_hand[0])] * (max_lines - len(computer_hand))

    print_center(f"{user_hand_name.ljust(40)}{computer_hand_name}")
    for u_line, c_line in zip(user_hand, computer_hand):
        print_center(f"{u_line.ljust(40)}{c_line}")

    if computer_choice == user_choice:
        print_center("It's a tie.")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print()
        print_center("Congratulations! You won this round.")
        computer -= 1
        winning_p += 1
    else:
        print()
        print_center("Oops! You lost this round.")
        life -= 1
        winning_c += 1

    print()
    print(f"Leading scores so far - User: {winning_p} - Computer: {winning_c}")
    print()
print(f"\t\t\t\t\tGame over")

if winning_p > winning_c:
    print_center("Congratulations! You won the game.")
elif winning_p < winning_c:

    print_center("sorry bro Computer wins the game. Better luck next time.")
else:
    print_center("It's a tie! The game ends with a draw.")
print()
print()