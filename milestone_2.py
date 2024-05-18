import random

word_list = ["banana", "apple", "pear", "peach", "strawberry"] #Posible words the code will choose
word = random.choice(word_list) #Picks a random word from the list


def ask_for_input(): #Checks if the guess is a single letter
    while True:
        guess = input("Which letter are you guessing? ") #Takes user guess
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Guess is not a single letter.")
        
def check_guess(guess):
    upper_guess = guess.upper() #Creates upper and lower case guesses so case doesn't need to be matched
    lower_guess = guess.lower()

    if (upper_guess or lower_guess) in word:
        print(f"Good guess! {guess} is in the word.") 
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

guess = ask_for_input()
check_guess(guess)
