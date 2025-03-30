'''
Description : Week 04 Tasks. Program Flow #1 
Author : Niall Naughton
Date : 20.02.2025

Write a program (isEven.py) that asks the user to enter in a number, and the
program will tell the user if the number is even or odd.
'''

#Get Input
int_num = int(input("Enter an integer Number :"))

if (int_num % 2) == 0:
    print (f"The number {int_num} is an even number")
else:
    print(f"The number {int_num} is an odd number")