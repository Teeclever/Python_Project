# this a function that check the value passed by the user and update to the coresponding letter on the missing spot
# its loops through from the starting index and check the guess letter wheather its in the list before updating it
# 

def check(guess_letter, list, updating_list):

    for i in range(len(list)):
        pick = list[i]
        if pick == guess_letter:
            updating_list[i] = guess_letter

#THis is the list item the randon words are generated from

guesslist = ["rice",  "apple", "egg", "beans", "spaggatti", "indomie", "school", "money", "house", "luck", "happy", "house", "bugatti", "love"]
