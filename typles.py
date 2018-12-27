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

Converting Types with the list() and tuple() Functions
Just like how str(42) will return '42', the string representation of the integer 42, 
the functions list() and tuple() will return list and tuple versions of the values passed to them.
 Enter the following into the interactive shell, and notice that the return value is of a 
 different data type than the value passed:


>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
Converting a tuple to a list is handy if you need a mutable version of a tuple value.