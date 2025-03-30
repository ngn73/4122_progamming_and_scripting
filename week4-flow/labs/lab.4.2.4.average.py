
'''
lab.4.2.4.average.py
Author  Niall Naughton
Date    23/02/2025
Description
Write a program (average.py) that keeps reading numbers until the user
enters a 0. (the program should append each of them into a list)
The program should then print out each of the numbers entered and the
average of them. (Use a list)
'''

numbers = []
# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))
while number != 0:
    numbers.append(number)    
    # read the next number and check if 0
    number = int(input("enter another (0 to quit): "))
   
for value in numbers:
    print (value)

# I want average to be a float
average = float(sum(numbers)) / len(numbers)
print (f"The average is {average:.2f}") #Round to 2 places of decimal
