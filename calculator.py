

def accept_numbers():
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    l = []
    l.append(a)
    l.append(b)
    return l


def add():
    l = accept_numbers()
    result = f"the result of the addition of {l[0]} and {l[1]} is {l[0]+l[1]}"
    print(result)


def sub():
    l=accept_numbers()
    result = f"the result of the subtraction of {l[0]} and {l[1]} is {l[0]-l[1]}"
    print(result)


def mult():
    l=accept_numbers()
    result = f"the result of the multiplication of {l[0]}and {l[1]} is {l[0]*l[1]}"
    print(result)


def div():
    l=accept_numbers()
    result = f"the result of the division of {l[0]} and {l[1]} is {l[0]//l[1]}"
    print(result)


while True:
    option = input(
        "Enter e to END \n Enter a for ADD \n Enter s for SUBTRACT  \n Enter d for DIVIDE  \n Enter m for MULTILPY")

    if option == "a":
        add()
    elif option == 's':
        sub()
    elif option == 'm':
        mult()
    elif option == 'd':
        div()
    elif option == 'e':
        break
    else:
        print("invalid option")
