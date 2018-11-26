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

'''String Formatting

So far, to combine strings and non-strings, you've converted the non-strings to strings and added them. 
String formatting provides a more powerful way to embed non-strings within strings. String formatting uses a string's format method to substitute a number of arguments in the string.
Example:
'''
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
'''

Result:
>>>
Numbers: 4 5 6
>>>
'''

#Each argument of the format function is placed in the string at the corresponding position, 
#which is determined using the curly braces { }.
'''
String formatting can also be done with named arguments.
Example:
'''
a = "{x}, {y}".format(x=5, y=12)
print(a)

# Result : 5,12

#What is the result of this code?
str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)

# Ans : 7, 9, 5

'''String Functions

Python contains many useful built-in functions and methods to accomplish common tasks. 
join - joins a list of strings with another string as a separator. 
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively. 
To change the case of a string, you can use lower and upper.
The method split is the opposite of join, turning a string with a certain separator into a list.
Some examples:'''
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"


