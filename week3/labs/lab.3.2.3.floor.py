
'''
Description : Week 03 Tasks. Absolute Numbers.
Author : Niall Naughton
Date : 15.02.2025
'''
#import addtional module
import math as m

#Get Input
numberTofloor = float(input("Enter a float number:"))

#Use floor() and ceiling())
flooredNumber = m.floor(numberTofloor)
ceilingNumber =m.ceil(numberTofloor)

#Output results
print(f'{numberTofloor} floored is {flooredNumber}, Ceiling is {ceilingNumber}')