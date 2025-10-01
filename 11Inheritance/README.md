# Inheritance

## What Is Inheritance?

Inheritance lets you create a new class based on an existing class.  
The new class (called a **child** or **subclass**) automatically gets all the attributes and methods of the existing class (called the **parent** or **superclass**).  
You can also add new features or change how things work in the child class.

---

## Why Use Inheritance?

- **Reuse code:** Don’t repeat yourself! Put shared code in a parent class.
- **Organize:** Group related classes together.
- **Extend:** Add or change features in child classes without changing the parent.

---

## How to Use Inheritance

Here’s a simple example:

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

dog = Dog("Buddy")
dog.speak()  # Output: Buddy says woof!
```

---

## What is `super()`?

The `super()` function lets you call methods from the parent class.  
This is especially useful in the `__init__` method, so you don't have to rewrite code that already exists in the parent.

**Example:**

```python
class Parent:
    def __init__(self, value):
        self.value = value

class Child(Parent):
    def __init__(self, value, extra):
        super().__init__(value)  # Calls Parent's __init__
        self.extra = extra
```

---

## What Are Grandchildren in Inheritance?

A **grandchild** class is a class that inherits from a child class, which itself inherits from a parent class.  
This creates a chain: **Parent → Child → Grandchild**.  
The grandchild gets all the features of both the parent and child classes, and can add its own.

---

## A More Complicated Example of Inheritance

This example shows a parent class, two child classes, and a grandchild class.  
It also demonstrates how to use `super()` to reuse code from parent classes.

```python
# Parent class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"{self.name} earns ${self.salary} per year.")

# Child class
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call the parent __init__
        self.department = department

    def show_info(self):
        print(f"{self.name} manages {self.department} and earns ${self.salary} per year.")

# Another child class
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def code(self):
        print(f"{self.name} writes code in {self.language}.")

# Grandchild class (inherits from Developer)
class SeniorDeveloper(Developer):
    def __init__(self, name, salary, language, years_experience):
        super().__init__(name, salary, language)
        self.years_experience = years_experience

    def mentor(self):
        print(f"{self.name} mentors others with {self.years_experience} years of experience.")

# Create objects
alice = Manager("Alice", 90000, "Sales")
bob = Developer("Bob", 80000, "Python")
carol = SeniorDeveloper("Carol", 120000, "Java", 10)

alice.show_info()      # Output: Alice manages Sales and earns $90000 per year.
bob.show_info()        # Output: Bob earns $80000 per year.
bob.code()             # Output: Bob writes code in Python.
carol.show_info()      # Output: Carol earns $120000 per year.
carol.code()           # Output: Carol writes code in Java.
carol.mentor()         # Output: Carol mentors others with 10 years of experience.
```

---

## Summary

- **Inheritance** lets you build new classes from existing ones.
- **super()** allows you to use methods from the parent class, making your code cleaner and more reusable.
- **Grandchildren** are classes that inherit from child classes, creating a chain of inheritance and allowing for even more code reuse and organization.

---

# Homework: Practice Inheritance

1. **Create a parent class with two attributes.**
2. **Create two child classes that come with their own method.**
3. **Create a grandchild class that inherits from one of the child classes and adds an attribute with its own method.**
4. **Make one object of each class and show how you can use both the parent, child, and grandchild methods.**
5. **You will be creating the file. Make sure to make the folder called Homework to put the file into. Remember to use """ in order to describe what the file is used for.**
6. **Include comments to describe each class.**

*Try adding more features or making more child classes!*