'''
----------------------------------------------------------------------------------
Author : Niall Naughton
Date : 20.02.2025
----------------------------------------------------------------------------------
Description : Week 06 Task
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
You should create a function called <tt>sqrt</tt> that does this.
I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). I suggest that you look at the newton method at estimating square roots. 
This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.
----------------------------------------------------------------------------------
Approach:
I will use the Babylonian method for computing the root of a number rather than built in python functions

For a given number : N
1. Make an initial guess : g = N/2
2. Improve the guess : g2 = (g + N/g)/2
3. Iteratively apply above formula where guess will successively get closer and closer to exact root value.
4. Continue iterating until the difference between successive guess values match to a fixed number of decimal places
-----------------------------------------------------------------------------------
'''

#Square Root method by iteratively calling babylonian approximate guess
def mysqrt(number):
 epsilon = 0.001 # Desired level of accuracy
 current_guess = number   #First guess
 previous_guess = 0.0
 while (abs(current_guess - previous_guess) > epsilon):
  print(f"Current guess : {current_guess}")
  previous_guess = current_guess
  current_guess = myguess(current_guess, number)
 return current_guess

# Apply babylonian guess formula
def myguess(latest_guess, number):
 return ((latest_guess + number)/latest_guess)/2.0  # Babylonian method

inNumber = float(input("Enter a Positive Number : "))
print(f"The square root of {inNumber} is {mysqrt(inNumber)} ")

