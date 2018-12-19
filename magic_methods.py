'''Magic methods are special methods which have double underscores at the beginning and end of their names. 
They are also known as dunders. 
So far, the only one we have encountered is __init__, but there are several others. 
They are used to create functionality that can't be represented as a normal method. 

One common use of them is operator overloading. 
This means defining operators for custom classes that allow operators such as + and * to be used on them.
An example magic method is __add__ for +.'''

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
'''

Result:
>>>
8
16    
>>>
'''

'''
The __add__ method allows for the definition of a custom behavior for the + operator in our class. 
As you can see, it adds the corresponding attributes of the objects and returns a new object, containing the result.
Once it's defined, we can add two objects of the class together.
'''

'''More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y). 
However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called. 
There are equivalent r methods for all magic methods just mentioned.
Example:'''
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
'''

Result:
>>>
spam
============
Hello world!
>>>
'''

'''
Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__. 
There are no other relationships between the other operators.
Example:
'''
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs
'''

Result:
>>>
>spam>eggs
e>spam>ggs
eg>spam>gs
egg>spam>s
eggs>spam>
>>>
'''
#As you can see, you can define any custom behavior for the overloaded operators

'''There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types. 
Example:'''
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

'''
Result:
>>>
6
7
D
C
>>>

We have overridden the len() function for the class VagueList to return a random number.
The indexing function also returns a random item in a range from the list, based on the expression.'''


''' Q >> Which magic method call is made by x[y] = z?
   Ans>> x.__setitem__(y, z)
'''

'''The del statement reduces the reference count of an object by one, and this often leads to its deletion.
The magic method for the del statement is __del__. 
The process of deleting objects when they are no longer needed is called garbage collection.
In summary, an object's reference count increases when it is assigned a new name or placed in a container (list, tuple, or dictionary).
The object's reference count decreases when it's deleted with del, its reference is reassigned,
or its reference goes out of scope. When an object's reference count reaches zero,
Python automatically deletes it.'''

'''
Example:
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>
'''