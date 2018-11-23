'''
The argument of the open function is the path to the file. 
If the file is in the current working directory of the program, you can specify only its name.
'''
myfile = open("in.txt")

'''You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default. 
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
For example:
'''

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

#binary read mode 
open("filename.txt","rb")

#You can use the + sign with each of the modes above to give them extra access to files. 
#For example, r+ opens the file for both reading and writing.


'''Once a file has been opened and used, you should close it.
This is done with the close method of the file object.
'''

file = open("filename.txt", "w")
# do stuff to the file
file.close()

'''The contents of a file that has been opened in text mode can be read using the read method.'''
file = open("filename.txt", "r")
contents = file.read();
print(contents) #This will print all of the contents of the file "filename.txt".

'''To read only a certain amount of a file, you can provide a number as an argument to the read function.
 This determines the number of bytes that should be read. 
You can make more calls to read on the same file object to read more of the file byte by byte. 
With no argument, read returns the rest of the file. '''

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

# Just like passing no arguments, negative values will return the entire contents.
'''After all contents in a file have been read, any attempts to read further from 
that file will return an empty string, because you are trying to read from the end of the file.'''

file = open("filename.txt", "r")
file.read()
print("Re-reading")
print(file.read())
print("Finished")
file.close()


'''To retrieve each line in a file, 
you can use the readlines method to return a list
in which each element is a line in the file.'''

file = open("in.txt", "r")
contents=file.readlines();
print(contents)
file.close()

'''
You can also use a for loop to iterate through the lines in the file:
'''
f = open("in.txt", "r")
for line in f:
	print(line)

	f.close() 

'''To write to files you use the write method, which writes a string to the file.
The "w" mode will create a file, if it does not already exist.
When a file is opened in write mode, the file's existing content is deleted.
Opening a file mode in write mode itself , deletes all the contents of the file before overwriting it
For example:
'''
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

'''
The write method returns the number of bytes written to a file, if successful.
To write something other than a string, it needs to be converted to a string first.
'''
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

#It is good practice to avoid wasting resources by making sure that 
#files are always closed after they have been used. One way of doing this is to use try and finally.

try:
	f = open("filename.txt")
	print(f.read())
finally:
	f.close()

#This ensures that the file is always closed, even if an error occurs.

'''An alternative way of doing this is using with statements.
 This creates a temporary variable (often called f), 
 which is only accessible in the indented block of the with statement.'''

with open("out.txt") as fe:
 	print(fe.read())

#The file is automatically closed at the end of the with statement, even if exceptions occur within it.