'''
hello2.py
Author  Niall Naughton
Date    09/02/2025
Description     Experimenting with input() and bit of Date formatting and arrays
'''
import datetime

#Simple Input/ouput
fname = input("Enter your First Name:")
print(f"Your Name is :{fname}\nNice to meet you!")

#Input/ouput with formatted Date 
lname = input("Enter your Last Name:")
DayL = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
date = DayL[datetime.datetime.today().weekday()]
print (f"Nice to meet you Mr. {lname} this {date}")


#Input with Formatted  String
age = input(f"Hello {fname}, today is {date}. What is your age:")
print (f"So {fname} you are {age} years old")