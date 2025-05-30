import os
import time 

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the quotient of a and b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

x = None  # Initialize x to enter the loop

while x != "0":
    x = input("Welcome to the math functions program! Please choose a function!\n(1)Addition\n(2)Subtraction\n(3)Multiplication\n(4)Division\n(5)AddnMultiply\n(0)Exit: ")
    if x == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        os.system('cls')
        print(f"{a} + {b} = {add(a, b)}")
    elif x == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        os.system('cls')
        print(f"{a} - {b} = {subtract(a, b)}")
    elif x == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        os.system('cls')
        print(f"{a} * {b} = {multiply(a, b)}")
    elif x == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        os.system('cls')
        try:
            print(f"{a} / {b} = {divide(a, b)}")
        except ValueError as e:
            print(e)
    elif x == "5":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        os.system('cls')
        print(f"{a} + {b} = {add(a, b)}, while {a} * {b} = {multiply(a, b)}")
    elif x == "0":
        print("Exiting the program. Goodbye!")
        time.sleep(2)
        os.system('cls')
    else:
        print("Invalid option. Please try again.")
        os.system('cls')
    time.sleep(2)