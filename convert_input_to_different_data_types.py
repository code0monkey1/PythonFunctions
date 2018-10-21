#!/bin/python3
# changetype.py: Enter numbers as strings and convert to other types
#
myintstring = input("Enter a whole number: ") # Ask for input to save to myintstring variable
myint = int(myintstring) # Converts from string to integer data type
myfloatstring = input("Enter a floating point number: ") # Ask for input to save to myfloatstring variable
myfloat = float(myfloatstring) # Converts from string to float data type
print("\n")
print("myint type is : ", type(myint)) # Show the data type of myint
print("myfloat type is : ", type(myfloat)) # Show the data type of myfloat
print("myint is : ", myint) # Display the value of myint
print("myfloat is : ", myfloat) # Display the value of myfloat
print("myint + myfloat is : ", myint+myfloat) # Add myint and myfloat and display
print("myint + myfloat as an integer is : ", int(myint+myfloat)) # Add myint and myfloat, convert to an integer and display

