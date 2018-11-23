'''Tuples

Tuples are very similar to lists, except that they are immutable (they cannot be changed). 
Also, they are created using parentheses, rather than square brackets. 
Example:'''
words = ("spam", "eggs", "sausages",)

'''You can access the values in the tuple with their index, just as you did with lists:'''
print(words[0])

'''Trying to reassign a value in a tuple causes a TypeError.
words[1] = "cheese"

Result:
>>>
TypeError: 'tuple' object does not support item assignment
>>>
'''

#Like lists and dictionaries, tuples can be nested within each other.

'''Tuples can be created without the parentheses, by just separating the values with commas.
Example:
'''
my_tuple = "one", "two", "three"
print(my_tuple[0])

#Tuples are faster than lists, but they cannot be changed.