'''
lab.4.2.3.guess2.py
Author  Niall Naughton
Date    23/02/2025
Description
How would you modify the program in 3 (guess2.py) above, so that the
program tells the user if there guess is too high or too low, each time they
guess. HINT: put an if statement inside the while loop
Extra: get the program to generate a random number between 0 and 100 to
guess (I am not giving the answer to this)
'''
import random

numberToGuess = int(random.random()*100)
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Guess Too Low")
    else: # guess > numberToGuess
        print("Guess Too High")
    guess = int(input("Please guess again:"))
    
print ("Well done! Yes the number was ", numberToGuess)