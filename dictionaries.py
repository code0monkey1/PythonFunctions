'''Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
Example:'''

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
'''Trying to index a key that isn't part of the dictionary returns a KeyError.
Example:'''
primary = {
"red": [255, 0, 0], 
"green": [0, 255, 0], 
"blue": [0, 0, 255], 
}

print(primary["red"])
#print(primary["yellow"])

'''Only immutable objects can be used as keys to dictionaries.
Immutable objects are those that can't be changed. So far, 
the only mutable objects you've come across are lists and dictionaries. 
Trying to use a mutable object as a dictionary key causes a TypeError.'''

bad_dict = {
  #[1, 2, 3]: "one two three", 
  }

'''Just like lists, dictionary keys can be assigned to different values.
However, unlike lists, a new dictionary key can also be assigned a value, not just ones that already exist.'''

squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.

nums = {
1: "one",
2: "two",
3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

'''A useful dictionary method is get. It does the same thing as indexing,
but if the key is not found in the dictionary it returns another specified value instead ('None', by default).'''

pairs = {1: "apple",
"orange": [2, 3, 4], 
True: False, 
None: "True",
}

# using the get method is the preferable approach
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary")) # functions like default value returned
# in java map when value not present

