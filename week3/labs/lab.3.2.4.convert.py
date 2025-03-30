'''
Description : Week 03 Task 2 Question #4.
Author : Niall Naughton
Date : 15.02.2025
'''

#Get Floating Number
f_input = float(input("Enter floating point amount (positive or negative) : "))

#round to 2 places of decimal (as it is money) and multiply by 100
f_2_input = (round(f_input, 2)) *100
#This will round up the 3 place of decimal entered

#cast to int and Get absolute amount
abs_input = abs(int(f_2_input))


#Output result
print(f'The absolute amount in cents is {abs_input}')