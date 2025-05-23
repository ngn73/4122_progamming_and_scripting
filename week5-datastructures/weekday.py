'''
Description : Week 05 Task.  
Author : Niall Naughton
Date : 02.03.2025

----------------------------------------------------------------------------------
Description : Week 05 Task
Write a program that outputs whether or not today is a weekday. 
(The program should be called weekday.py)
----------------------------------------------------------------------------------
Approach:
Use strftime() to extract day name and then compare to dictionary of key/value pairs
https://www.geeksforgeeks.org/how-to-format-date-using-strftime-in-python/
https://www.w3schools.com/python/gloss_python_date_format_codes.asp

'''
import datetime

#Use a Dictionary to define Weekdays/Weekends
days_of_week = {
    "monday": "weekday",
    "tuesday": "weekday",
    "wednesday": "weekday",
    "thursday": "weekday",
    "friday": "weekday",
    "saturday": "weekend",
    "sunday": "weekend"
}

#Get today's date
now = datetime.date.today()
#Convert to a Day Name (and lowercase to match above keys)
today = (now.strftime("%A")).lower()

if days_of_week[today] == "weekday":
    print(f"Yes, unfortunately today, {today}, is a weekday.")
else:
    print(f"It is {today} ... the weekend, yay!")