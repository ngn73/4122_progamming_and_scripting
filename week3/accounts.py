'''
accounts.py
Author  Niall Naughton
Date    23/02/2025
Description     Weekly Task #3
Bank account numbers can stored as 10 character strings
For security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
Write a python program called accounts.py that reads in a 10 character account number
and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
'''

#Get 10 Character Account Number
account_number = input("Please enter an 10 digit account number: ")

#Output Masked Account Number
mask_prefix = "X" * 6 #Interesting Syntax
print(f"Masked Account Number is {mask_prefix}{account_number[-4:]}") #Use String Slicing
