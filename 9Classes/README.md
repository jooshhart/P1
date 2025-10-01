# Classes and Objects

## What Are Classes and Objects?

- **Class:** A blueprint for creating objects. It defines what data (attributes) and actions (methods) the objects will have.
- **Object:** An individual thing created from a class. Each object can have its own data.

Think of a class as a recipe, and objects as the cakes you bake from that recipe.

---

## Why Use Classes?

- **Organization:** Group related data and functions together.
- **Reusability:** Make many objects from one class, each with their own data.
- **Easier to manage:** Code is cleaner and easier to understand, especially for bigger projects.

---

## How to Make a Class

Here’s a simple example:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute

    def bark(self):       # method
        print(f"{self.name} says woof!")
```

- `__init__` is a special method that runs when you make a new object.
- `self` refers to the object itself.

---

## How to Make and Use Objects

```python
my_dog = Dog("Buddy", 3)   # Create an object
print(my_dog.age)         # Access attribute
my_dog.bark()              # Call method
```

**Output:**
```
3
Buddy says woof!
```

---

## What Difference Do Classes Make?

Without classes, you might have to manage lots of separate variables and functions for each thing.  
With classes, you can create as many objects as you want, each with their own data and actions, using the same code.

**Without classes:**
```python
dog1_name = "Buddy"
dog1_age = 3
def bark1():
    print("Buddy says woof!")
```

**With classes:**
```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog1.bark()
dog2.bark()
```

---

# Homework: Make a Class for a Game Character

Create a class called `Character` that has:
- A name
- Health points
- A method to print out the character’s info

Then, make two different characters and print their info.

**Output:**
```
Aria has 100 health points.
Drake has 80 health points.
```

*Try adding more attributes or methods, like an attack method or a way to change health!*