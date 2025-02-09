'''
helloworld.py
Author  Niall naughton
Date    09/02/2025
Description    Experimenting with Print() and String formatting in Python
'''

#Simple Print Atatement
print("Hello World")

#Use of a Variable
txt = "Helo world"
print(txt)

#Use of Specific Data Type for Variable
str_txt1 = str("hello World")
print(str_txt1)

#Concatonating String Variables
str_1 = str("hello")
str_2 = str("world")
print(str_1 + " " + str_2)

#Formatting String with print() format
str_firstname = "Niall"
str_surname = "Naughton"
print("Hello {0} {1} to the World".format(str_firstname, str_surname))
#Alt Formatting Version
print(f"Hello {str_firstname} {str_surname} to the new World")

#Use of String Replace Fn
str_txt2 = str("Hello World")
print(str_txt2.replace("World", ""))

#Use of String Capitalise Fn
str_txt3 = str("HELLO WORLD")
print(str_txt3.capitalize())

#Use of String lower Fn
str_txt3 = str("HELLO WORLD")
print(str_txt3.lower())