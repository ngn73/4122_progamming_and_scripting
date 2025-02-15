
'''
Description : Week 03 Tasks. Variables#2. Minus Tests
Author : Niall Naughton
Date : 15.02.2025
'''
#Take 2 Ints as Inputs
num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))

#Minus Inputs
num3 = num1 - num2

#Print result
print(f"{num1} minus {num2} is {num3}")

#When entering 1.25624 ... I was surpised that it threw an error instead of casting 1.25624 as 1 (int) without issue
#When entering blah ... Understandably threw an error :  invalid literal for int() with base 10: 'blah'

