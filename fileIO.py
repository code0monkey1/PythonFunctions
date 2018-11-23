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
'''
For example:
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

You can use the + sign with each of the modes above to give them extra access to files. For example, r+ opens the file for both reading and writing.