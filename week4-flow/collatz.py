'''
collatz.py
Author  Niall Naughton
Date    23/02/2025
Description     Weekly Task #4
Write a program, called collatz.py, that asks the user to input any positive integer 
and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, 
divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.
Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).
'''

#get input
number = int(input("Enter a Positive Integer"))
count = 1
collatz = [] #apply Collatz series to a List

#Loop Calculation while number > 1
while number > 1:
    if number%2 == 0: #Even Number
        number = number/2
    else:   #Odd
        number = (number * 3) + 1
    collatz.append(int(number))
    count = count + 1
print(f"The Number {number} generated the following Collatz Series : {collatz}")
print(f"Completed Task with {count - 1} calculations ")