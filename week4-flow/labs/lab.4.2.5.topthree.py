'''
lab.4.2.5.topthree.py
Author  Niall Naughton
Date    23/02/2025
Description
Write a program (topthree.py) generates 10 random numbers (0-100) ,
prints them out then prints out the top three. (there are concepts I have not
covered yet in this question)
'''
import random

rnd_count = 1
rnd_list = []

#loop 10 times and generate a random number (1 - 100)
while rnd_count <= 10:
    rnd_list.append(int(random.randint(1, 100)))
    rnd_count += 1

#output generated list
print(f"Numbers generated are {rnd_list}")

#Sort and output top 3 values from list
rnd_list.sort(reverse = True)
print(f"The  top 3 Numbers are {rnd_list[0:3]}")