'''
Although they are created differently from normal variables, functions are just like any other kind of value. 
They can be assigned and reassigned to variables, and later referenced by those names.
'''
def multiply(x, y):
   return x * y


a = 2
b = 4
operation = multiply
print(operation(a, b))

'''Functions can also be used as arguments of other functions.'''

def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))

'''There is another kind of import that can be used if you only need certain functions from a module.
These take the form from module_name import var, and then var can be used as if it were defined normally in your code. 
For example, to import only the pi constant from the math module:
from math import pi
'''
from math import pi
print(pi)

'''Use a comma separated list to import multiple objects. For example:
from math import pi, sqrt

To imports all objects from a module. 
For example: from math import *

This is generally discouraged, as it confuses variables in your code with variables in the external module.
You can import a module or object under a different name using the as keyword. This is mainly used when a module or object has a long or confusing name.
For example:

'''
from math import sqrt as square_root
print(square_root(100))

'''Many third-party Python modules are stored on the Python Package Index (PyPI). 
The best way to install these is using a program called pip. 
This comes installed by default with modern distributions of Python. 
If you don't have it, it is easy to install online. Once you have it,
 installing libraries from PyPI is easy. Look up the name of the library you want to install, 
 go to the command line (for Windows it will be the Command Prompt), and enter pip install library_name. 
 Once you've done this, import the library and use it in your code.

Using pip is the standard way of installing libraries on most operating systems,
 but some libraries have prebuilt binaries for Windows.
  These are normal executable files that let you install libraries with a GUI the same way you would install
  other programs.
'''

