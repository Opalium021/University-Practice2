#python
#Javad Razaz Rahmaty
#Hangman game


import os
import random

print("\n\n                ========>>>>Welcome to the Hangman Game<<<<========       ")

def clear(): return os.system('cls')

def play_again():

    while True:
        again = input("Do You Want To Play Again? (y/n) ").lower()
        
        if again == "y" or again == "yes":
            clear()
            return True
        
        elif again == "n" or again == "no":
            return False
        else:
            print("Please Choose Yes or NO")


def game(chance, word, correct_guess_list, total_guess_list):

    i = 0

    while i < chance:
        print_hangman(i)
        print_word(word, correct_guess_list)

        usr_guess = input("\nEnter a char = ").lower()
        if usr_guess.isalpha() == False or len(usr_guess) != 1:
            clear()
            print("Please Enter a Valid char")
            continue

        if usr_guess in total_guess_list:
            clear()
            print("\nYou Enter That Before")
            continue

        else:
            if usr_guess in word:
                correct_guess_list.append(usr_guess)

            else:
                i += 1


        total_guess_list.append(usr_guess)

        if game_over(correct_guess_list, word):
            return True

        clear()

    print_hangman(i)
    return False


def game_over(correct_guesses, word):

    for l in word:
        if l not in correct_guesses:
            return False

    return True

def print_word(word, guess):
    print("\n")
    for l in word:
        if l in guess:
            print(l, end=" ")

        else:

            print("_", end=" ")

def print_hangman(stage):

    hangman = [
        '''







_|_
''',
        '''

 |
 |
 |
 |
 |
_|_
''',
        '''
  ____
 |
 |
 |
 |
 |
_|_
''',
        '''
  ____
 |    |
 |
 |
 |
 |
_|_
''',
        '''

  _____
 |     |
 |     O
 |
 |
 |
_|_
''',
        '''
  _____
 |     |
 |     O
 |     |
 |
 |
_|_
''',
        '''
  _____
 |     | 
 |     O
 |    /|
 |
 |
_|_
''',
        '''
  _____
 |     |
 |     O
 |    /|\
 |
 |
_|_
''',
        '''
  _____
 |     | 
 |     O
 |    /|\
 |    /
 |
_|_
''',
        '''
  _____
 |     |
 |     O
 |    /|\
 |    / \
 |
_|_
'''
        ]

    print("\n" , hangman[stage])


word_list = ["red" , "blue" , "yellow" , "white" , "black" , "grey" , "pink"]
chance = 9

while True:

    correct_guess_list = []
    total_guess_list = []

    word = random.choice(word_list)

    win = game(chance, word, correct_guess_list, total_guess_list)

    if win == True:
        print("\n\n Good Job You Win\n")

    else:
        print("\n\n You Lose :( \n")

    if play_again() == False:
        break
