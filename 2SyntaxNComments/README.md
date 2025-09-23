# Syntax and Comments

```python

```
## Strings
Strings Are a set of text that are held in between '' or "".
```python
my_string = "Hello, World!"
```
my_string is the variable that contains the value. The value is "Hello, World!"

## Integers
Integers are simple numbers that have no decimals, but can be negative.
```python
my_integer = 42
```
Just like before, we have the variable at the left and the value of that variable is to the right.

## Floats
Floats are like integers, but they are allowed to have decimals.
```python
my_float = 3.14159
```
There will be times when a program requires no decimals, and there are times when a program requires decimals, so float won't always be used, sometimes, int is more necessary.

## Booleans
Booleans are values that merely ask if something is true or not true.
```python
my_bool = True
```
```python
my_bool = False
```
These will mostly be used to indicate the direction of a program

## Lists
Lists are capable of holding a set of information. The whole value of a list variable is on the right.
```python
my_list = [1, 2, 3, "four", 5.0]
```
In a list, it will be indexed of what values are where in the total value. The beginning of a list is indexed at 0, while the rest follows by +1. So, the value of 1 is indexed at place 0, while value "four" is indexed at place 3. In python a list is capable of holding any type of value, but in order code, this doesn't work.

## Print
Print is how values can be posted into the terminal. Basically, when in VS Code, after creating a code and using print, print will sent the information given to it into the terminal below. If you do now have your terminal open, you can find the terminal tab at the top of VS Code. Then you can click on New Terminal. Or you can press these three keys: ctrl or Cmd + Shift + `.
```python
print("This is how you print in Python!")
```

## Comments
Comments are used in order to specify in code what the code does and why. This is critical in order to help you remember what is happening and to help others to understand as well. Comments can also be used to cut out some of your code during testing without actually deleting the code itself.
### Short Comment
```python
# This is a short comment
```
### Long Comment (multi-line)
```python
"""
This is a long comment.
It can span multiple lines.
Useful for documentation or explanations.
"""
```
### Comment Highlighted
```python
# TODO: This is a highlighted comment for tasks
```
### How to comment and uncomment multiple lines
To comment and uncomment multiple lines, simply highlight them and press ctrl + / or Cmd + /

## Syntax
Syntax mean the appropriate way to input code. Here are some tips to know you're doing things correctly. A variable should describe the value that it holds. For example, if the value has to do with a person's age, then the variable should be called, "age."
```python
age = 21
```
As you can see, this variable did not start in a capital letter. No variables should start with a capital letter. This is because of something you will learn about later called classes. These will be set starting with a capital letter to designate the difference between it and a variable.
Now, what happens if there is a variable that asks about your age and a variable that asks about another person's age. Both variables cannot have the same name, which means the variable would require a more specific name.
```python
your_age = 21
other_age = 20
```
As you can see, variables should not have spaces. Instead of spaces, use "_" in order to separate words. Also, make sure to never name a variable with just one letter. You need to be as specific as possible when naming variables.
And remember to leave space in between the variables, values, and distribution. By distribution, I mean =, +, -, etc. Notice in the examples how there is always space for =.

## Homework
You must create your first program. This will require that you know how to create variables, comments, and print. It will also depend on how you know your syntax. I want you to give me your name, age and height. Create a boolean for if your gender is Male. Make a list of favorite foods. Make sure to have comments for each variable describing what the variable is and add a print at the end that says one last thing about yourself. Make sure to comment above this as well to describe print.