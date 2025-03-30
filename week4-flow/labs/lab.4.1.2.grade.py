'''
Description : Week 04 Tasks. Program Flow #2
Author : Niall Naughton
Date : 20.02.2025

Write a program (grade.py) that reads in a student’s percentage mark and
prints out corresponding the grade (the program should check that the
percentage is valid:
• Under 40% => Fail
• Between 40% and 49% => Pass
• Between 50% and 59% => Merit 2
• Between 60% and 69% => Merit 1
• Over 70% => Distinction
'''

grade = float(input("Enter a Student's Grade between 0 and 100 :"))
result = ""

if grade < 0 or grade > 100:
    print("Please enter a number between 0 and 100")
elif grade < 40 :
    result = "Fail"
elif grade < 50:
    result = "Pass"
elif grade < 60 :
    result = "Merit 1"
elif grade < 70 :
    result = "Merit 2"
else :
    result = "Distinction"

#Output Result
print(f"The Result is a {result}")

