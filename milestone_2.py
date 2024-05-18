import random

word_list = ["banana", "apple", "pear", "peach", "strawberry"]
word = random.choice(word_list)
guess = input("Which letter are you guessing? ")
if len(guess) == 1:
    print("Nice Guess!")
elif guess == word:
    print("You win!")
else:
    print("Oops, that doesn't look like a good guess try again")
guess = input("Which letter are you guessing? ")


print(word, word_list)