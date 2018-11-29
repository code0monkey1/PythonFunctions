'''Generators

Generators are a type of iterable, like lists or tuples. 
Unlike lists, they don't allow indexing with arbitrary indices,
 but they can still be iterated through with for loops. 
They can be created using functions and the yield statement.
Example:'''
def countdown():
	i=5
	while i > 0:
		yield i
		i -= 1

		for i in countdown():
			print(i)

'''The yield statement is used to define a generator, 
replacing the return of a function to provide a result to its caller without destroying local variables'''

'''Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists. 
In fact, they can be infinite!
'''
def infinite_sevens():
	while True:
		yield 7 

		for i in infinite_sevens():
			print(i)


#In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

#Fill in the blanks to create a prime number generator, that yields all prime numbers in a loop. (Consider having an is_prime function already defined):


def get_primes():
	num = 2
	while True:
		if is_prime(num):
			yield num
			num += 1