# print("Enter ten numbers")
# total = 0
# product=1
# for i in range(10):
#     print("Enter the number(",i,")...")
#     number=int(input())
#     product*=number
#     total=total+number
# print("Total is",total)
# print("Product is ",product)

# ---------- if and  else if chaining
num = 7
if num == 5:
   print("Number is 5")
elif num == 11:
   print("Number is 11")
elif num == 7:
   print("Number is 7")
else:
   print("Number isn't 5, 11 or 7")
# ---- you could even give it a range 

for i in range (1,3): # i prints from 1 to 2  ( not including 3 )
	print(i)
# --- you could evend add a step argument 

for i in range ( 1, 10 ,2 ): # the third is the incremented_by value
	print(i)  # prints 1 , 3 , 5 , 7 , 9    // increasing 2 every time 

# --- you could even have a negative step argument 

for i in range ( 5 , -1 , -1 ):
	print(i , end=" ") # to print on the same line put end=" "
 # prints 5 , 4 , 3 , 2 , 1, 0  
	# decreasing one every time till it reaches -1 (and does not include -1 )