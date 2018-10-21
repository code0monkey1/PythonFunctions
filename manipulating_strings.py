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
