'''
Description : Week 03 Tasks. String Input.
Author : Niall Naughton
Date : 16.02.2025
'''

#Get Input
str_input = input('Enter a String : ')
len_input = len(str_input)

#Output result
print(f'The lenght of {str_input} is {len_input }')

#Alternative solution to Q#2 : How would you output a string like this?
#Use of escape chars for Quotes, Carraige Return, and a Tab thrown in
print(f'The lenght of  string \"{str_input}\" is {len_input } Characters.\n\tTime to say \"Good Bye\"')