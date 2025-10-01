# Saving and Loading Data

In many programs, you may want to save information so you can use it again later. Python lets you save data to a file (like a `.txt` file) and load it back when you need it.

---

## How to Save Data to a Text File

You can use the `open()` function with `"w"` mode to write (save) data to a file.

```python
# Save data to a file
with open("mydata.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a new line.\n")
```

- The `with` statement makes sure the file closes automatically.
- `"w"` means "write" mode (it will overwrite the file if it exists).

---

## How to Load Data from a Text File

You can use `open()` with `"r"` mode to read data from a file.

```python
# Load data from a file
with open("mydata.txt", "r") as file:
    for line in file:
        print(line.strip())
```

- `"r"` means "read" mode.
- `line.strip()` removes extra spaces and newlines.

---

## File Locations and Paths

When saving or loading files, Python looks for the file in the "current working directory" (where your terminal or script is running).  
If your `.txt` file is in a different folder (like a `Homework` folder), you need to use a relative or absolute path.

**Example:**

If your folder structure is:
```
P1/
  8SaveLoad/
    Homework/
      scoreboard.txt
      game.py
```

And you run your code from the `P1` folder, you should use:
```python
with open("8SaveLoad/Homework/scoreboard.txt", "r") as file:
    # your code here
```

If you run your code from inside the `Homework` folder, you can just use:
```python
with open("scoreboard.txt", "r") as file:
    # your code here
```

**Tip:**  
You can check your current working directory in Python:
```python
import os
print(os.getcwd())
```
This helps you know where Python is looking for files.

---

## Why Save and Load Data?

- **Remember user progress or scores**
- **Store lists, settings, or logs**
- **Share data between runs of your program**

---

# Homework: Save and Load a Scoreboard

Write a program that lets the user play a simple guessing game (like guessing a random number between 1 and 10).  
Each time the user wins, save their name and score to a file called `scoreboard.txt`.  
When the program starts, load and display the current scoreboard.

**Requirements:**
- Use the `random` library for the guessing game.
- Use functions for the main parts of your code.
- Use file saving and loading as shown above.
- Print the scoreboard in a nice format at the start and after each win.
- Make sure your file path works with your folder structure!

**Example:**

```
Current Scoreboard:
Alice: 2
Bob: 1

Guess the number (1-10): 7
Correct! You win!
Enter your name: Alice

Current Scoreboard:
Alice: 3
Bob: 1
```

*Hint: You can store each score as a line like `Alice: 3` and update the file after each win!*