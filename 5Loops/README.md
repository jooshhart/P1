# Loops

Loops let you repeat actions in your code. Python has two main types: `while` loops and `for` loops.

---
## While Loops
A `while` loop repeats as long as a condition is true.

```python
count = 0
while count < 3:
	print("Counting:", count)
	count += 1
```
**Output:**
```
Counting: 0
Counting: 1
Counting: 2
```

---
## For Loops
A `for` loop repeats for each item in a list or range.

```python
for color in ["red", "green", "blue"]:
	print("Color:", color)
```
**Output:**
```
Color: red
Color: green
Color: blue
```

You can also use `range()` to loop a certain number of times:

```python
for i in range(5):
	print(i)
```
**Output:**
```
0
1
2
3
4
```

`For` loops are used mostly to search for things. If you use a for loop on a string, it will search each character in the string, even the spaces. If you use it on a list, each time it loops, it will grab each value in that list. So, if you have this list:
```python
numbers = [1, 2, 3, 4]
```
And if you have inputed a variable called search with a value of `3`. Then you can you for loop like this:
```python
for number in numbers:
	if number = search:
		print(search, "is in the list.")
		break
	else:
		print(search, "is not in the list.")
```
Now you have a way to search for a number inputted by the user.

---
# Homework Assignments

## 1. Choose Your Own Adventure (with While Loop)
Update your previous choose your own adventure program. Add a `while` loop so that if the user enters something invalid, the program asks again instead of stopping. The program should keep going until the user gives a valid answer.

*Hint: Use a `while` loop to check if the input is valid!*

---
## 2. While Loop Menu
Use while loops to make a program menu. This menu should give the user 2 different options, plus the 3rd which is to end the program. This means that nothing else can end the program, except when the user prompts the program to end. 

---
## 3. For Loop Practice
Write a program that uses a `for` loop to search for something in a list. For example, ask the user for a name and check if that name is in a list of names. Print a message if the name is found or not found.

*Hint: Try making a list of names first. Have a variable input so the user can search for the any name they'd like. Include a boolean that identifies if the name is found or not found. Start that boolean at False.

---
