'''Угадай число менее, чем за 20 попыток'''
import random

guess = int(input("Choose a number you want the computer to guess from  1-100: "))

turns = 0
a = None

compguess = random.randint(1,100)

while turns < 10 and 100 > guess >= 1 and compguess != guess: #computer has 10 turns to guess number, you can change it to what you want
    print("The computer's guess is:  ", compguess)
    if compguess>guess:
        a = compguess
        compguess = random.randint(1, compguess)

    elif compguess < guess:
        compguess = random.randint(compguess, a)
        turns += 1


    if compguess == guess and turns < 10:
        print("The computer guessed your number of: ", guess)
        turns += 1

    elif turns >= 10 and compguess != guess:
        print("The computer couldn't guess your number, well done.")


input("")
