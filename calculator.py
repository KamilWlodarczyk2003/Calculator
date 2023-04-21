﻿
#Add

from pyclbr import Function
from unittest import result


def Add(n1,n2):
    return n1+n2

#Subtract

def Subtract(n1,n2):
    return n1-n2

#Multiply

def Multiply(n1,n2):
    return n1*n2

#Divide

def Divide(n1,n2):
    return n1/n2

Functions={"+": Add, "-": Subtract, "*":Multiply, "/":Divide}

num1=int(input("What's your first number?: "))

for x in Functions:
    print(x)
operation_symbol=input("Pick an operator from the list above: ")

num2=int(input("What's your first number?: "))

result=Functions[operation_symbol](num1,num2)

print(f"{num1} {operation_symbol} {num2} = {result}")