#!/bin/python3
# strings.py
#
import time # This imports a library which contains functions relating to time

mystring = input("Enter a word or sentence: ")
for ii in range(len(mystring)): # Sets a range from 0 to number of characters in mystring
  print(mystring[ii]) # Print the character at index ii of mystring
  time.sleep(0.1) # Pause for 0.1s using the 'sleep' function from the 'time' library

input("Press ENTER to view the string's characters in reverse order")
for ii in range(len(mystring)):
  print(mystring[-1-ii]) # Print the character at index (-1 minus ii) of mystring
  time.sleep(0.1)

print("Chiru " * 3)
# output : Chiru Chiru Chiru

float(input("Enter a number: ")) + float(input("Enter another number: "))
#Enter a number: 40
#Enter another number: 2
#42.0

 x = 123.456
 print(x)
# 123.456
 x = "This is a string"
# print(x + "!")
#This is a string!

del variable_name # deletes the variable reference 

#substring
name = "chira"
print(name[0:3])
#chi

print(len(name))
#5

#formatted string 
statememt="hello my name is chiranjeev"
l = f"{statememt} {statememt}" # this experession is evaluated at runtime
print(l)

#hello my name is chiranjeev hello my name is chiranjeev

print(statememt.lower()) #these do exactly what you expect them to do 
print(statememt.upper())
print(statememt.title())
print(statememt.strip())



yess = "hello" not in statememt
print(yess)

# False 