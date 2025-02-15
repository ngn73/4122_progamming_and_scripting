
'''
Description : Week 03 Tasks. Variables#2. Division Tests
Author : Niall Naughton
Date : 15.02.2025
'''

#Take 2 Ints as Inputs
num1 = int(input("Enter first Number : "))
num2 = int(input("Enter second Number : "))

#Use 2 types of Division
answer1 = num1 // num2 #returns 3
answer2 = num1 / num2 #returns 3.3333333333...

#Modulus
remainder = num1 % num2

#Print out Results
print(f"{num1} divided by {num2} is {answer1} with  remainder {remainder} with int division")
print(f"{num1} divided by {num2} is {answer2:.3f} with  remainder {remainder} with normal division") #formatted for 3 decimal places


