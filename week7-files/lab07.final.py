'''
Author: Niall Naughton
Date: 15/03/2025
Description:
Final Code for Lab #07 File handling exercise (including save and load json functions)
'''
import json

def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(l) Load students")
 print("\t(s) Save students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice

def readModules():
 modules = []
 moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
 
 while moduleName != "":
  module = {}
  module["name"]= moduleName
  module["grade"]=int(input("\tEnter grade:"))
  modules.append(module)
  # now read the next module name
  moduleName = input("\tEnter next module name (blank to quit):").strip()
 return modules

def doAdd():
 student_name = input("enter name : ")
 student_modules = readModules()
 
 #add to a Directory my_student
 my_student = {}
 my_student["name"] = student_name
 my_student["modules"] = student_modules
 
 return my_student

def doView(students):
 for student in students:  # Each Student is a Directory (keys: name/modules)
  displayStudent(student)
  displayModules(student)

def displayStudent(student):
 print(f"Student Name : {student['name']}")

def displayModules(student):
 for module in student["modules"]: # Modules is a List, each module is a directory (keys: name/grade)
  print(f"\tModule : {module['name']} : Grade {module['grade']}")

def doSave(students):
 saveDict(students)
 print(f"Saved data to json file {FILENAME}")

def doLoad():
 studentdata =  loadDict()
 print("Loaded student data")
 return studentdata

def saveDict(obj):
 with open(FILENAME, 'wt') as f:
  json.dump(obj,f)

def loadDict():
 obj = {}
 with open(FILENAME) as f:
  obj = json.load(f)
  print(obj)
  return obj

FILENAME ="studentdata.json"
student_details = []
user_choice = displayMenu()

while user_choice != "q":
 if (user_choice.lower() == 'a'):
  student_details.append(doAdd()) #Add collected Student details (name/modules/grades) to List
 elif(user_choice.lower() == 'v'):
  doView(student_details) #display current collection of Students (name/modules/grades)
 elif(user_choice.lower() == 'l'):
  student_details = doLoad() #load current collection of Students from file
 elif(user_choice.lower() == 's'):
  doSave(student_details) #save current collection of Students to json file
 elif(user_choice.lower() == 'q'):
  break
 else: #invalid input
  print("\n\nplease select either a,v or q")
 #get another input choice
 user_choice = displayMenu()

print("Good bye!")