
'''
Description : Week 03 Tasks. Rounding Numbers.
Author : Niall Naughton
Date : 15.02.2025
'''

#Enter Number
numberInput = float(input("Enter a floating number : "))

#Use 2 types of round()
roundedNumber = round(numberInput)
roundedfloatNumber = round(numberInput, 3) #formatted for 3 Decimal Places

#print differnt formats of round()
print ( f'{numberInput} rounded to int is {roundedNumber}')
print ( f'{numberInput} rounded to 3 Decimal places is {roundedfloatNumber}')


