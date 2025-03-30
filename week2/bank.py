'''
bank.py
Author  Niall Naughton
Date    23/02/2025
Description     Weekly Task #2
The program should:
    1. Prompt the user and read in two money amounts (in cent)
    2. Add the two amounts
    3. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
'''

#Int Input
number1 = int(input("Please Enter an Money Amount #1 (in cents): "))
number2 = int(input("Please Enter an Money Amount #2 (in cents): "))

number3 = (number1 + number2)
print (f"The Sum of €{number1/100:,.2f} plus €{number2/100:,.2f} is €{number3/100:,.2f}\n")

