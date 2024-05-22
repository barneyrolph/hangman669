# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### The goal of the project
The aim of this project is not necessarily to be able to play hangman by myself but to develop my coding skills.

### What I have learnt

 - I have been able to implement a class in a meaningful way and getting to grips with all the self!
 - I found a use for the ennumerate function that I hadn't seen whilst studying the theory.
 - I've looked up how to count occurences of a character in a string.


### The implementation

The game is a class with two methods.

One method (check_guess) checks the users guess and updates the output to show if the user was correct or not.

The other method asks for an input from a user and validates their guess.  Then calls the check_guess method.  This latter method also contains the end conditions for the game.

The game also allows for the number of lives to be defined. The game will accept a list of words to choose from that must be all lower case.

### Installation

Use the following to clone the repo:

` git clone https://github.com/barneyrolph/hangman669.git ` 

Run the *hangman_game.py* file for a demo game:

` python hangman_game.py `

Edit and run the *custom_game.py* file for a game with a custom word list.


### Next steps
An obvious next step would be to remove the need for lower case only in the word list which could be achieved by splitting the users guess into an upper and lower case guess and checking both.
