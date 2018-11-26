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
#For example:
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
max(list) # Returns the list item with the maximum value
min(list) #Returns the list item with minimum value
list.count(obj) # Returns a count of how many times an item occurs in a list
list.remove(obj) #Removes an object from a list
list.reverse() # Reverses objects in a list

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

 '''List Slices :

 List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a list with two colon-separated integers. This returns a new list containing all the values in the old list between the indices.
 Example:
 '''
 squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 print(squares[2:6])
 print(squares[3:8])
 print(squares[0:1])

''' Result:
>>>
[4, 9, 16, 25]
[9, 16, 25, 36, 49]
[0]
>>>

Like the arguments to range, the first index provided in a slice is included in the result, but the second isn't.'''

#If the first number in a slice is omitted, it is taken to be the start of the list.
#If the second number is omitted, it is taken to be the end.
#Example:
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

'''
Result:
>>>
[0, 1, 4, 9, 16, 25, 36]
[49, 64, 81]
>>>

***Slicing can also be done on tuples.
'''

'''List Slices

List slices can also have a third number, representing the step, to include only alternate values in the slice.'''
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

'''
Result:
>>>
[0, 4, 16, 36, 64]
[4, 25]
>>>

[2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3.

'''

'''Negative values can be used in list slicing (and normal list indexing). 
When negative values are used for the first and second values in a slice (or a normal index), 
they count from the end of the list.
'''
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

'''
Result:
>>>
[1, 4, 9, 16, 25, 36, 49, 64]
>>>

If a negative value is used for the step, the slice is done backwards.

***Using [::-1] as a slice is a common and idiomatic way to reverse a list.
'''
#What is the output of this code?
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

#Ans : [49,36]

'''List Comprehensions:
List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
For example, we can do the following:
# a list comprehension:
'''
cubes = [i**3 for i in range(5)]

print(cubes)

#Ans :>>>
#[0, 1, 8, 27, 64]
#>>>

'''A list comprehension can also contain an if statement to enforce a condition on values in the list.
Example:
'''
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)
'''

Result:
>>>
[0, 4, 16, 36, 64]
>>> 
'''

#Create a list of multiples of 3 from 0 to 20.

#Ans : a = [i for i in range(20) ifi%3==0]


'''Trying to create a list in a very extensive range will result in a MemoryError.
This code shows an example where the list comprehension runs out of memory.'''
even = [2*i for i in range(10**100)]

'''Result:
>>>
MemoryError
>>>
'''

#Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.

a = [x*10 for x in range(5, 9)]

'''
Numeric Functions : 

To find the maximum or minimum of some numbers or a list, you can use max or min.
To find the distance of a number from zero (its absolute value), use abs.
To round a number to a certain number of decimal places, use round.
To find the total of a list, use sum.
Some examples:
'''
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))
'''

Result:
>>>
0
9
99
42
15
>>>

'''
'''List Functions

Often used in conditional statements, all and any take a list as an argument, and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise). 
The function enumerate can be used to iterate through the values and indices of a list simultaneously.
Example:
'''
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)
   Try It Yourself
'''
Result:
>>>
All larger than 5
At least one is even
(0, 55)
(1, 44)
(2, 33)
(3, 22)
(4, 11)
>>>
'''