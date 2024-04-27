import math
def add(a,b):
    c=a+b
    return c
def subtraction(a,b):
    c=a-b
    return c
def multiplication(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c
def floor_division(a,b):
    c=math.floor(a/b)
    return c
def remainder(a,b):
    c=a%b
    return c
def exponent(a,b):
    c=a**b
    return c
#MAIN
print("\t\t\t\tARITHMATIC CALCULATOR\n")
a=float(input("Enter the first number to calculate : "))
b=float(input("Enter the second number to calculate : "))
loop=True
while(loop):
    print("\n1.Addition of numbers\n2.Subtraction of numbers.\n3.Multiplication of numbers.\n4.Division of numbers.\n5.Floor division of numbers\n6.Remainder of numbers.\n7.Exponent of numbers a**b.\n8.exit\n")
    ch=int(input("Enter your choice"))
    if ch==1:
        print("Addition of number:",add(a,b))
    elif ch==2:
        print("Subtraction of numbers:",subtraction(a,b))
    elif ch==3:
        print("Multiplication of number:",multiplication(a,b))  
    elif ch==4:
        print("Division of numbers:",division(a,b))
    elif ch==5:
        print("Floor division of numbers:",floor_division(a,b))
    elif ch==6:
        print("Remainder when a/b:",remainder(a,b))
    elif ch==7:
        print("Exponent when a**b:",exponent(a,b))
    elif ch==8:
        print("Exited! THANK YOU FOR USING THE CALCULATOR")
        loop=False  
    else:
        print("invalid choice")       

