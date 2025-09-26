# Imports

## What Are Imports?

Imports let you use code from other files or libraries in your program. This helps you avoid rewriting code and lets you use powerful tools made by others.

## Why Are Imports Important?

- **Reuse:** Use code that’s already written and tested.
- **Organization:** Split your code into multiple files for easier management.
- **Access to Libraries:** Use Python’s built-in features and third-party packages.

---

## How to Use Imports

To use an import, write:

```python
import math
```

Now you can use functions from the `math` library, like:

```python
print(math.sqrt(16))  # Output: 4.0
```

You can also import specific functions:

```python
from math import sqrt
print(sqrt(25))  # Output: 5.0
```

Or rename imports:

```python
import math as m
print(m.pi)  # Output: 3.141592653589793
```

---

## Safe vs. Unsafe Imports

- **Safe Imports:**  
  - Standard Python libraries (`math`, `random`, `datetime`, etc.)
  - Your own files/modules
  - Well-known third-party libraries (like `numpy`, `pandas`) from trusted sources

- **Unsafe Imports:**  
  - Unknown or untrusted third-party libraries (may contain malware or bugs)
  - Files from the internet you haven’t checked
  - Avoid using `import *` (can overwrite variables and cause confusion)

---

## Most Used Imports

- `math` — Math functions
- `random` — Random numbers
- `datetime` — Dates and times
- `os` — Operating system tasks
- `sys` — System-specific parameters
- `time` — Time-related functions

---

# Homework

## Dice Roller

Make a program that lets the user roll different sided dice: d4, d6, d8, d10, and d20. First you will need to import random. Next you will need to find a way to make sure the user can only choose a dice of one of those sizes. `random.randint` can be used to find a random number. Here is an example:

```python
random.randint(1, 9) #This will give a random number between 1 and 9
```

Make sure to make nice code that repeats and prints the answer in the end as a statement.