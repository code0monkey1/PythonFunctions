'''
Sets

Sets are data structures, similar to lists or dictionaries. They are created using curly braces, or the set function.
 They share some functionality with lists, such as the use of in to check whether they contain a particular item.
'''
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

'''
Result:
>>>
True
False
>>>
'''

#To create an empty set, you must use set(), as {} creates an empty dictionary.

'''Sets differ from lists in several ways, but share several list operations such as len. 
They are unordered, which means that they can't be indexed. 
They cannot contain duplicate elements. 
Due to the way they're stored, it's faster to check whether an item is part of a set, rather than part of a list.
Instead of using append to add to a set, use add. 
The method remove removes a specific element from a set; pop removes an arbitrary element.
'''
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

'''
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either. 
The intersection operator & gets items only in both. 
The difference operator - gets items in the first set but not in the second. 
The symmetric difference operator ^ gets items in either set, but not both.

'''
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

'''
Data Structures

As we have seen in the previous lessons, Python supports the following data structures: lists, dictionaries, tuples, sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements. 
- Use tuples when your data cannot change. 
Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, because it's immutable.
'''