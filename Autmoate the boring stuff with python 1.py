#import pyperclip


#hello world , here I come 

#pyperclip.paste() # this will pase anything that is in the clipboard 

#pyperclip.copy("this will be copied") # this will copy the statement to the clipboard 


# the end and the sep arguments of print 

#print("hello","world",sep="balma") # this will put the separating character
 #as balma between the words
#print("hello to all", end="yooo")  # the end argument will have the ending 
#'\n' thing repaaced with what you wish
eggs ='hello'

def myfunc() :
	global eggs # to force the assignment of the value to a global variable , 
	#instead of the local variable beign created 
	eggs='hello there'

	myfunc()
	print(eggs)


# Exception handling in python
def dividebyz( number ):

	try:
		print(	22/number )
	except ZeroDivisionError:  # keeping this as ' except : 'without any arguments catches all exceptions
		print("this is an invalid division")


	class guessingGame:
		def __init__(self, numero, number):
			self.numero=0
			self.number=0

		def inputNumber():
			global numero , number
			number=input(" Enter a number ")
			

		def startgame():
			numero=sys.rand(1,10)
			while True:
				inputNumber()
				if(isCorrectGuess(number)):
					print("Your guess is correct \n You win!!")
					break
				elif number>numero:
					print("Guess lower")
				else :
					print("Guess higher")



		def isCorrectGuess(number):
			return numero==number


	guessingGame.startgame()