"""
Most of this homework is done for you. Your task is to connect the functions.
You will be adding the four functions: add, subtract, multiply, divide.
You will also be printing the answer to the user.
This homework is mostly an example of how to use functions in a program.
Use comments to explain your code.
Test your code in the terminal.
Turn in your code by sending me the link.
"""

print("Type your calculation (e.g. 1+2). Type 0 to exit.")

signs = ["+", "-", "*", "/"]

while True:
    user_input = input("Enter calculation: ")
    if user_input.strip() == "0":
        print("Calculator exited.")
        break

    # Try to find a valid sign and split input
    sign_found = False
    for s in signs:
        if s in user_input:
            sign = s
            parts = user_input.split(sign)
            if len(parts) == 2:
                try:
                    left_number = float(parts[0])
                    right_number = float(parts[1])
                    sign_found = True
                except ValueError:
                    print("Error: Please enter valid numbers.")
                break
            else:
                print("Error: Please enter in the format number sign number (e.g. 1+2).")
                break

    if not sign_found:
        print("Error: Please use one of these signs: +, -, *, /")
        continue

    # Connect functions with their appropriate sign
    if sign == "+":
        answer = add(left_number, right_number)
    elif sign == "-":
        answer = subtract(left_number, right_number)
    elif sign == "*":
        answer = multiply(left_number, right_number)
    elif sign == "/":
        if right_number == 0:
            print("Error: Division by zero is not allowed.")
            continue
        answer = divide(left_number, right_number)