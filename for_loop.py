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