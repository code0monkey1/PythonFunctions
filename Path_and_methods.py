from pathlib import Path

obj = Path()

items = obj.glob("*.txt") # A GENERATOR  object is returned by the glob method 
# this will return all files that end with .txt extention



for item in items:
	print(item)

# to get all the files / directores in the present working directory use "*"

print("\n next line \n")

everything = obj.glob('*')

for item in everything:
	print(item)