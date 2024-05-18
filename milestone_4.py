import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) #random word from list
        self.word_chars = list(self.word) #splits the word into characters
        self.word_guessed = [] #To be displayed to player
        for char in self.word_chars: #fills the word_guessed list with the correct number of underscores
            self.word_guessed.append("_")
        self.list_of_guesses=[] #list of letters guessed
        self.num_letters = 0 #number of correct letters
    
    def check_guess(self, guess):
        lower_guess = guess.lower()
        if lower_guess in self.word:
            n = self.word.count(lower_guess)
            print(f"Good guess, {lower_guess} is in the word {n} time(s).")
            for i, char in enumerate(self.word_chars):
                if char == lower_guess:
                    self.word_guessed[i]=lower_guess
            self.num_letters += n
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f"Unlucky, {lower_guess} isn't in the word.  You have {self.num_lives} lives remaining.")
    
    def ask_for_input(self):
        print(self.word_guessed)
        while self.num_lives > 0 and self.num_letters < len(self.word_chars):
            guess = input("Which letter are you guessing? ")
            if not (guess.isalpha() and len(guess) == 1):
                print("Guess is not a single letter.")
            elif guess in self.list_of_guesses:
                print("You already guessed that!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

        if self.num_letters == len(self.word_chars):
            print("Congratulations! You've guessed the word!")
        else:
            print(f"Game over! The word was {self.word}.")


test = Hangman(["banana"])
test.ask_for_input()
