'''Lambda function example'''

def function(args,a):
	return args(a)

print(function(lambda x: x+2,2))

'''Lambda functions aren't as powerful as named functions. 
They can only do things that require a single expression - usually equivalent to a single line of code.
Example:'''

#named function
def polynomial(x):
	return x**2 + 5*x + 4
print(polynomial(-4))

#equavalent lambda
print((lambda x: x**2 + 5*x + 4) (-4))

