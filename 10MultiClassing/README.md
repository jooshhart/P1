# Using Classes from Separate Files

As your projects get bigger, it's helpful to organize your code by putting classes in their own files. This makes your code easier to read, reuse, and manage.

---

## How to Put a Class in a Separate File

Suppose you have a class called `Character`. You can put it in a file called `character.py`:

```python
# character.py
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def show_info(self):
        print(f"{self.name} has {self.health} health points.")
```

---

## How to Use That Class in Another File

In your main program file (for example, `game.py`), you can import the class:

```python
# game.py
from character import Character

hero = Character("Aria", 100)
hero.show_info()
```

**Output:**
```
Aria has 100 health points.
```

---

## Why Organize Code This Way?

- **Cleaner code:** Each file has a clear purpose.
- **Easier to find things:** You know where each class is defined.
- **Reusability:** You can use the same class in different projects by copying just one file.

---

# Homework: Practice with Multi-File Classes

1. **Create a file called `pet.py` and write a class called `Pet` with a name, species, gender, and it's sound.**
2. **Create a separate file called `main.py`.**
3. **In `main.py`, import the `Pet` class and create two different pets. Display their info.**

**Expected Output:**
```
Buddy is a dog. He says, "Woof!"
Whiskers is a cat. She says "Meow!"
```

*Try adding more methods or attributes to your Pet class!*