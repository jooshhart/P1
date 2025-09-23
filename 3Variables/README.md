# Variables

Variables are like containers that store information. You can use them to keep track of values, get input from the user, print results, and change their contents.

---
## Creating and Using Variables
You create a variable by giving it a name and assigning it a value using `=`.

```python
name = "Alice"
age = 12
print(name)
print(age)
```
**Output:**
```
Alice
12
```

---
## Getting Input from the User
You can use the `input()` function to ask the user for information. The value is always a string.

```python
user_name = input("What is your name? ")
print("Hello, " + user_name + "!")
```
**Example Output:**
```
What is your name? Bob
Hello, Bob!
```

---
## Changing Variable Values
You can change a variable's value at any time by assigning it a new value.

```python
score = 10
print(score)
score = 20  # Change the value
print(score)
```
**Output:**
```
10
20
```

---

## Printing Variables
You can print variables by passing them to the `print()` function. You can also combine text and variables using commas or the `+` operator.

```python
name = "Sam"
print("Hello,", name)
print("Hello, " + name)
```
**Output:**
```
Hello, Sam
Hello, Sam
```

---

## Printing Multiple Variables in a Sentence
You can print a sentence using variables by combining text and variables. There are several ways to do this:

### Using Commas
Commas let you print text and variables together. Python adds spaces automatically.

```python
first_name = "Jane"
last_name = "Doe"
age = 15
print("My name is", first_name, last_name, "and I am", age, "years old.")
```
**Output:**
```
My name is Jane Doe and I am 15 years old.
```

### Using f-strings (formatted strings)
An f-string lets you put variables directly inside curly braces `{}` in your string. Just put an `f` before the quotes.

```python
first_name = "Jane"
last_name = "Doe"
age = 15
print(f"My name is {first_name} {last_name} and I am {age} years old.")
```
**Output:**
```
My name is Jane Doe and I am 15 years old.
```

F-strings are the easiest and most powerful way to build sentences with variables in Python!

---
## Summary
- Variables store information.
- You can get input from the user and store it in a variable.
- Variables can change value.
- Use `print()` to show variable values.

## Homework
Make sure to create a program similar to the last. However, this time it needs to use inputs to gain the information. It needs to end with a print that gives a sentence greeting the user and explaining who they are. This time it should only require name, age, and height. Comments will still be required. When checking the terminal, you will be writing into the terminal when it asks for inputs. Make sure to send me the link to your homework in order to submit it.