'''
Author: Niall Naughton
Date: 15/03/2025

----------------------------------------------------------------------------------
Task Description:
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.
----------------------------------------------------------------------------------
Approach:
I will use the The str.count(sub) method that returns the number of non-overlapping occurrences 
of a substring sub in the target string
https://docs.python.org/3/library/stdtypes.html#str.count
This can be applied to the string returned from a file read() operation.
'''
import os

#Tests for a valid file and returns a string with full contents of file
def readFile(file_name):
 str_content = ""
 try:
  with open(file_name, 'r', encoding='utf-8') as f:
   str_content = f.read()
   if os.path.getsize(file_name) == 0: #if file is empty
    str_content = ""
    print(f"Error: The file {file_name} is empty")
 except FileNotFoundError: #this happens when a file is not found
  str_content = ""
  print(f"Error: The file {file_name} was not found.")
 except UnicodeDecodeError:  # this happens when trying to read binary data as text
  str_content = ""
  print(f"Error: The file {file_name} was not a Text file.")
 #finally return file content string
 return str_content


#get the count of occurrences of a char (my_char) with a string(my_str)
def getCharCount(my_str, my_char):
  try:
   if isinstance(my_str, str):
    return my_str.count(my_char)
   else:
    raise ValueError(f"The file's content is not in a string format.")
  except ValueError as e:
   print(e)
   return 0

#Get input
char = 'e'
filename = input("Enter a file to test: ")

#Call functions
str_file = readFile(filename)
if len(str_file) > 0: #valid file
 num_chars = getCharCount(str_file, char)
 #Print output
 print(f"The number of occurrences of character {char} in Text File {filename} is : {num_chars}")
else:
 print(f"file {filename} is not valid.");

