
'''
Description : Week 03 Tasks. Absolute Numbers.
Author : Niall Naughton
Date : 15.02.2025
'''

#Enter an ambiguous number (positive or negative)
number = float(input("Enter a number:"))
absoluteVal = abs(number)

#print normally and formatted to 5 places of decimal
print(f'The absolute value of {number} is {absoluteVal}')
print(f'The absolute value of {number} is {absoluteVal:.5f}')