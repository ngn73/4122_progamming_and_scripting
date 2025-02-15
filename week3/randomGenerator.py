'''
Description : Week 03 Tasks. Variables#3. Ransom Number  Tests
Author : Niall Naughton
Date : 15.02.2025
'''

#TImport Module
import random

#Input Limits
#Note : Inputs must be cast to Int .... otherwise treated as String and then Error
seed1 = int(input("Enter starting RND Seed : "))
seed2 = int(input("Enter ending RND Seed : "))

#Generate RND Number
rnd_number = random.randint(seed1,seed2)

#Print out Results
print(f"here is a random number {rnd_number}")

