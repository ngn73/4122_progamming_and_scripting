'''
lab.4.2.2.guess1.py
Author  Niall Naughton
Date    23/02/2025
Description
Write a program (guess1.py) that prompts the user to guess a number, the
program should keep prompting the user to guess the number until the user
gets the right on
'''

numberToGuess = 74
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print ("Wrong")
    guess = int(input("Please guess again:"))
    
print ("Well done! Yes the number was ", numberToGuess)