#Multiple exceptions can also be put into a single except block using parentheses, 
#to have the except block handle all of them.
try:
	variable = 10
	print(variable + "hello")
	print(variable / 2)
except ZeroDivisionError:
	print("Divided by zero")
except (ValueError, TypeError):
	print("Error occurred")

#  An except statement without any exception specified will catch all errors. These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
# For example:
try:
	word = "spam"
	print(word / 0)
except:
	print("An error occurred")

#To ensure some code runs no matter what errors occur, you can use a finally statement. 
#The finally statement is placed at the bottom of a try/except statement. 
#Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks.
try:
	print("Hello")
	print(1 / 0)
except ZeroDivisionError:
	print("Divided by zero")
finally:
	print("This code will run no matter what")

#Code in a finally statement even runs if an uncaught exception occurs in one of the preceding blocks.
try:
	print(1)
	print(10 / 0)
except ZeroDivisionError:
	print("Zero ZeroDivisionError")
finally:
	print("This is executed last")

'''  
Raising Exceptions :

You can raise exceptions by using the raise statement.

You need to specify the type of the exception raised.
'''
print(1)
#raise ValueError
print(2)
'''
Exceptions can be raised with arguments that give detail about them.
For example:

'''
name = "123"
#raise NameError("Invalid name!")

'''In except blocks, the raise statement can be used without arguments to re-raise whatever exception occurred.
For example:
'''
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise