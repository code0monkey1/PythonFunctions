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
 
 # a lists can have multiple type of values 
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])

#Lists can be added and multiplied in the same way as strings.
For example:
nums = [1, 2, 3]
print(nums + [4, 5, 6]) #[1, 2, 3, 4, 5, 6]
print(nums * 3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#To check if an item is in a list, the in operator can be used. It returns True if the item occurs one or more times in the list, and False if it doesn't.
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words) #true
print("egg" in words) #true
print("tomato" in words) #false

#The insert method is similar to append, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words) #['Python', 'is', 'fun']

#The index method finds the first occurrence of a list item and returns its index.
#If the item isn't in the list, it raises a ValueError.
letters = ['p', 'q', 'r', 's', 'p', 'u']

print(letters.index('r'))#2
print(letters.index('p'))#0
print(letters.index('z'))#ValueError: 'z' is not in list
# There are a few more useful functions and methods for lists. 
max(list): Returns the list item with the maximum value
min(list): Returns the list item with minimum value
list.count(obj): Returns a count of how many times an item occurs in a list
list.remove(obj): Removes an object from a list
list.reverse(): Reverses objects in a list

#Range

#The range function creates a sequential list of numbers.
#The code below generates a list containing all of the integers, up to 10.
numbers = list(range(10)) #The call to list is necessary because range by itself creates
# a range object, and this must be converted to a list if you want to use it as one.
print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#If it is called with two arguments, it produces values from the first to the second.
#For example:
numbers = list(range(3, 8)) 
print(numbers) #[3, 4, 5, 6, 7]
print(range(20) == range(0, 20)) #True

#range can have a third argument, which determines the interval of the sequence produced. 
#This third argument must be an integer.
numbers = list(range(5, 20, 2))
print(numbers) #[5, 7, 9, 11, 13, 15, 17, 19]

#iterating through a list
words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
 # hello!
 # world!
 # spam!
 # eggs