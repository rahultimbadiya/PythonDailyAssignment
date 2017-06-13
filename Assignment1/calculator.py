def Add(a,b):
    print("Addition of two numbers: ",(a + b))

def Sub(a,b):
    print("Subtraction of two numbers: ", (a - b))

def Mul(a,b):
    print("Addition of two numbers: ", (a * b))

def Div(a,b):
    try:
        print("Division of two numbers: ", (a / b))
    except ZeroDivisionError:
        print("Not a valid number please try something else")

Add(2,3)
Sub(4,5)
Mul(6,7)
Div(8,4)