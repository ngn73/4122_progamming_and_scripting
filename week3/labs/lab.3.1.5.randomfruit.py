'''
Description : Week 03 Tasks. Variables#4. List  Tests
Author : Niall Naughton
Date : 15.02.2025
'''

#TImport Module
import random

#2 Types of 
#fruits = ['Apple', 'Orange', 'Banana', 'Pear'] #List
fruits = ('Apple', 'Orange', 'Banana', 'Pear') #Tuple

#Generate Fruit Value
len_list = len(fruits)
rnd_index = random.randint(0, (len_list - 1))
fruit = fruits[rnd_index]

#Print out Results
print(f"A Random Fruit: {fruit}")
