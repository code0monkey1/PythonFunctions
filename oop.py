'''__init__

The __init__ method is the most important method in a class. 
This is called when an instance (object) of the class is created, using the class name as a function.

All methods must have self as their first parameter, although it isn't explicitly passed,
 Python adds the self argument to the list for you; you do not need to include it when you call the methods.
  Within a method definition, self refers to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.
In this example, Cat instances have attributes color and legs. These can be accessed by putting a dot,
 and the attribute name after an instance. 
In an __init__ method, self.attribute can therefore be used to set the initial value of an instance's attributes.
Example:
'''
class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)
'''

Result:
>>>
ginger
>>>

In the example above, the __init__ method takes two arguments and assigns them to the object's attributes.
 The __init__ method is called the class constructor.
'''

'''Classes can also have class attributes, created by assigning variables within the body of the class. These can be accessed either from instances of the class, or the class itself.
Example:'''
class Dog:
  legs = 4
  def __init__(self, name, color):
    self.name = name
    self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)
#Class attributes are shared by all instances of the class.

'''Trying to access an attribute of an instance that isn't defined causes an AttributeError. This also applies when you call an undefined method.

Example:'''
class Rectangle: 
  def __init__(self, width, height):
    self.width = width
    self.height = height

rect = Rectangle(7, 8)
#print(rect.color)

'''
Result:
>>>
AttributeError: 'Rectangle' object has no attribute 'color'
>>>
'''

'''Inheritance

Inheritance provides a way to share functionality between classes. 
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ in some ways (only Dog might have the method bark), they are likely to be similar in others (all having the attributes color and name). 
This similarity can be expressed by making them all inherit from a superclass Animal, which contains the shared functionality. 
To inherit a class from another class, put the superclass name in parentheses after the class name.
Example:'''
class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
'''

Result:
>>>
brown
Woof!
>>>
'''


''' Overriding : 

A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods, it overrides them.'''

class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog(Wolf):
  def bark(self):
    print("Woof")
        
husky = Dog("Max", "grey")
husky.bark()
'''

Result:
>>>
Woof
>>>

'''

'''Inheritance can also be indirect. One class can inherit from another, and that class can inherit from a third class. 
Example:'''

class A:
  def method(self):
    print("A method")
    
class B(A):
  def another_method(self):
    print("B method")
    
class C(B):
  def third_method(self):
    print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()
'''

Result:
>>>
A method
B method
C method
>>>
'''
#However, circular inheritance is not possible.


'''The function super is a useful inheritance-related function that refers to the parent class. It can be used to find the method with a certain name in an object's superclass.
Example:'''
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam()
'''

Result:
>>>
2
1    
>>> 
'''
#super().spam() calls the spam method of the superclass.


''' Encapsulation : 

Data Hiding

Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, it is mostly only a convention, and does not stop external code from accessing them. 
Its only actual effect is that from module_name import * won't import variables that start with a single underscore.
Example:'''
class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)
   
  def pop(self):
    return self._hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
'''

Result:
>>>
Queue([1, 2, 3])
Queue([0, 1, 2, 3])
Queue([0, 1, 2])
[0, 1, 2]
>>> 

In the code above, the attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.
The __repr__ magic method is used for string representation of the instance.
'''
'''

Strongly private methods and attributes have a double underscore at the beginning of their names. This causes their names to be mangled, which means that they can't be accessed from outside the class. 
The purpose of this isn't to ensure that they are kept private, but to avoid bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name. The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
Example:
'''
class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
#print(s.__egg)
'''

Result:
>>>
7
7
AttributeError: 'Spam' object has no attribute '__egg'
>>>

Basically, Python protects those members by internally changing the name to include the class name.

'''

'''Class Methods

Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the self parameter of the method.
Class methods are different - they are called by a class, which is passed to the cls parameter of the method. 
A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor. 
Class methods are marked with a classmethod decorator.
Example:'''

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

'''
Result:
>>>
25
>>>

new_square is a class method and is called on the class, rather than on an instance of the class.
 It returns a new object of the class cls.

Technically, the parameters self and cls are just conventions; they could be changed to anything else.
 However, they are universally followed, so it is wise to stick to using them.'''

#Static Methods

#Static methods are similar to class methods, except they don't receive any additional arguments; 
#they are identical to normal functions that belong to a class. 
#They are marked with the staticmethod decorator.
#Example:

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients) 

#Static methods behave like plain functions, except for the fact that you can call them from an instance of the class.

'''Properties

Properties provide a way of customizing access to instance attributes. 
They are created by putting the property decorator above a method, which means when the instance attribute with the same name as the method is accessed, the method will be called instead. 
One common use of a property is to make an attribute read-only.
Example:
'''
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True
'''

Result:
>>>
False

AttributeError: can't set attribute
>>>
'''

'''Properties

Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter keyword.
The same applies to defining getter functions.
'''
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      password = input("Enter the password: ")
      if password == "Sw0rdf1sh!":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
'''

Result:
>>>
False
Enter the password: Sw0rdf1sh!
True
'''