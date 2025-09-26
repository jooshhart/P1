# Functions in Python

Functions are reusable blocks of code that help organize your programs, avoid repetition, and make your code easier to read and maintain. You can use functions to group related actions, perform calculations, or handle specific tasks.

---

## Why Use Functions?

- **Organization:** Functions break your code into smaller, manageable pieces.
- **Reusability:** Write code once, use it many times.
- **Readability:** Functions make your code easier to understand.
- **Testing:** Functions can be tested separately from the rest of your code.

---

## How to Write a Function

Here's a simple function that greets the user:

```python
def greet(name):
    print("Hello,", name + "!")
```

To use (call) the function:

```python
greet("Alice")
```
**Output:**
```
Hello, Alice!
```

---

## Functions Can Return Values

Functions can also return values for use elsewhere in your code:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print("The sum is:", result)
```
**Output:**
```
The sum is: 8
```

---

## Functions Can Do Many Things

You can use functions for calculations, handling user input, working with lists, and much more.

```python
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(find_max([2, 8, 5, 1]))
```
**Output:**
```
8
```

---

# Homework

## Make a Calculator
Make a function for addition, subtraction, multiplication, and division. Most of the code is provided below. However, you still need to be able to print a statement that explains that left number, sign, right number, "=", answer at the end.

```python
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
```