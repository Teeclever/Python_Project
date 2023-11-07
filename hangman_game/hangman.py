import random
from list_check_generator import check, guesslist  
import hangman_diagram

# welcomeeee
print()
print("\t\t\t\t\t\t      Welcome, let's play Hangman game!!")
print("---------------------------------------------------------------\n")
print("Game Rules :\t\t\t\t\t  There will be words generated from\n\t\t\t\t\t\the words we use in our day-to-day activity.\n\t\t\t\t\t   You need to guess each letter of the generated word.\n")
print("---------------------------------------------------------------")
print("\t\t\tYou have only 6 lives so try to guess the word within 6 attempts! Good luck\n")

option = random.choice(guesslist)
display = ['_' for _ in option]
life = 6

print(f"\t\t\t          For this round, you have {len(option)}-letter word to guess from\n")
print(f"\t\t\t\t\t\t{' '.join(display)}\n")

game_over = False

while not game_over:
    letter_guess = input("Guess a letter: ")
    print()
    #A function that check the guess list and update the value if it present
    check(letter_guess, option, display)  
    print(f"\t\t\t\t\t\t{' '.join(display)}\n")
    
    if letter_guess not in option:
        life -= 1
        print(f"\t\t\t    Sorry, you guessed the wrong letter '{letter_guess}' which is not in the word.\n\nLife lost. Your remaining life trials = {life}\n")
        if life == 1:
            num = random.randrange(0, len(option))
            print(f"Hint: {option[num]}")
        if life == 0:
            game_over = True
            print("---------------------------------------------------------------")
            print(f"\t\t\tYou lost this round!\n\n       The correct word is '{option}'. Try again next time.\n")
    
    if '_' not in display:
        game_over = True
        print("---------------------------------------------------------------")
        print(f"\t\t\tCongratulations! You won this round with {life} lives left!\n\nYour guessed word was '{option}'. Well done!\n")
    
    print('\t', hangman_diagram.draw_hangman(life))  
