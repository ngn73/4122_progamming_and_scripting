'''
Description : Week 04 Tasks. Program Flow Extra Tasks 
Author : Niall Naughton
Date : 23.02.2025
Tasks:
1. In practice the percentages are rounded ie 69.5 gets rounded to 70 so is
equal to a Distinction.
How would you modify the program in 1 to deal with this?
I see two ways.
2. How would you use a while loop to modify 1 so that it keeps prompting the
user for a number until the user enters -1
3. I believe that data camp has some exercises in python you may want to look 
'''
input_grade = input("Enter a Student's Grade between 0 and 100 (or ""q"" to quit):")    #First input
while input_grade != "q":
    grade = float(input_grade)
    print(f"{round(grade)}")
    input_grade = input("Enter a Student's Grade between 0 and 100 (or ""q"" to quit):")    #Looped Input


