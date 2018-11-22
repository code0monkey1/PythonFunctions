print("Enter ten numbers")
total = 0
product=1
for i in range(10):
    print("Enter the number(",i,")...")
    number=int(input())
    product*=number
    total=total+number
print("Total is",total)
print("Product is ",product)

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
