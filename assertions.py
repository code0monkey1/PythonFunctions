'''Programmers often place assertions at the start of a function to check for valid input, 
and after a function call to check for valid output.'''

print(1)
assert 2 + 2 == 4
print(2)
#assert 1 + 1 == 3
print(3)

#The assert can take a second argument that is passed to the AssertionError raised if the assertion fails.

temp = -10
#assert (temp >= 0), "Colder than absolute zero!"

'''AssertionError exceptions can be caught and handled like any other exception using the try-except statement,
 but if not handled, this type of exception will terminate the program.'''

 