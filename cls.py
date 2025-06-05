# --- Using Functions Only ---

def create_person(name, age):
    return {"name": name, "age": age}

def birthday(person):
    person["age"] += 1
    print(f"Happy birthday, {person['name']}! You are now {person['age']}.")

def introduce(person):
    print(f"Hi, my name is {person['name']} and I am {person['age']} years old.")

# Using functions with dictionaries
alice = create_person("Alice", 30)
introduce(alice)
birthday(alice)
introduce(alice)

# --- Using a Class ---

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age}.")

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Using a class
bob = Person("Bob", 25)
bob.introduce()
bob.birthday()
bob.introduce()

# --- Summary ---
# With functions, you manage data using dictionaries and pass them around.
# With classes, you bundle data and behavior together, making code more organized and easier to extend.