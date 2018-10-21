#!/bin/python3
# bucket.py - bucket list builder
#
print('\nBUCKET LIST BUILDER\n') # The \n creates a new line
bucket = [] # Create an empty list called 'bucket'
choice = input('Enter selection: e(X)it, (A)dd, (L)ist (R)emove...') # Ask for input before loop
while choice != 'X': # This loop will continue until 'X' is entered
    if choice== 'A':
        print('Enter list item... ')
        newitem = input()
        bucket.append(newitem) # Add 'newItem' to the list called 'bucket'
    elif choice == 'L':
        for item in bucket: # This loop continues for however many items are in the list
            print(item)
    elif choice=='R':
      element=input("Enter the element to be removed")
      bucket.remove(element)
    else: # This is a 'default' option in case of no match
            print('Invalid selection.')
    choice = input('Enter selection: e(X)it, (A)dd, (L)ist...') # Ask for input at end of loop
print('\nGOODBYE!\n') # Only displayed if the loop has ended
