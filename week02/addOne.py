'''
addOne.py
Author  Niall Naughton
Date    09/02/2025
Description     Experimenting with input() and Numerical data
'''
import math


#Simple Int Input
number = int(input("Please Enter an Integer Number: "))
newNumber = number + 1
print (f"{number} plus one is {newNumber}\n")


#Simple Float Input
fnumber = float(input("Please Enter a Floating Point Number: "))
newFNumber = fnumber + 1
print (f"{fnumber} plus one is {newFNumber}\n")


#Formatted Float Input
ffNumber = float(input("Please Enter a Floating Point Number: "))
print (f"Number in 2 decimal places is {ffNumber:.2f}\n")

#Formatted Float Formatting 2
piNumber = math.pi * 33
print (f"Raw Number is {piNumber}")
print (f"Number in 2 decimal places is {piNumber:.2f}")
print (f"Number in 8 digits is {piNumber:.8g}")