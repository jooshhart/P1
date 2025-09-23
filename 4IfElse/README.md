# If, Elif, and Else

Conditional statements let your program make decisions. In Python, you use `if`, `elif`, and `else` to control what code runs based on conditions.

---
## The if Statement
Use `if` to run code only if a condition is true.

```python
age = 18
if age >= 18:
	print("You are an adult.")
```
**Output:**
```
You are an adult.
```

---
## The else Statement
`else` runs if the `if` condition is not true.

```python
age = 15
if age >= 18:
	print("You are an adult.")
else:
	print("You are a minor.")
```
**Output:**
```
You are a minor.
```

---
## The elif Statement
`elif` (else if) lets you check more conditions if the first `if` is false.

```python
score = 85
if score >= 90:
	print("Grade: A")
elif score >= 80:
	print("Grade: B")
else:
	print("Grade: C or below")
```
**Output:**
```
Grade: B
```

---
## Multiple elifs
You can use as many `elif` statements as you need.

```python
number = 0
if number > 0:
	print("Positive")
elif number < 0:
	print("Negative")
else:
	print("Zero")
```
**Output:**
```
Zero
```

---
## Indentation Matters
Python uses indentation (spaces) to show what code belongs to each part of the if/else structure.

```python
x = 5
if x > 0:
	print("x is positive")
	print("This line is also inside the if block")
print("This line is outside the if block")
```
**Output:**
```
x is positive
This line is also inside the if block
This line is outside the if block
```

---
## Summary
- Use `if` to check a condition.
- Use `elif` to check more conditions.
- Use `else` for everything else.
- Indentation is important in Python!

## Homework
This time you will be creating a program that creates a game. It will be a choose adventure game. You will be using print to give a situation. You will use input to ask the user what they will do, and you will use if, elif, and else in order to continue the story. Here is an example of what needs to be done:
```python
print("Welcome to the adventure game!")
print("Choose your path wisely between the numbers 1, 2, and 3.")
print("You find yourself stuck in the woods. You see a bird flying above you and you hear a creaking from behind.")
choice1 = input("Do you want to follow the bird (1), investigate the creaking (2), or move forward (3)? ")
if choice1 == "1":
    print("You follow the bird and it leads you to a beautiful clearing with a pond.")
    choice2 = input("Do you want to swim in the pond (1) or rest by the shore (2)? ")
    if choice2 == "1":
        print("You swim in the pond and find a hidden treasure chest!")
        choice3 = input("Do you want to open the chest (1) or leave it closed (2)? ")
        if choice3 == "1":
            print("You open the chest and find gold coins inside!")
        elif choice3 == "2":
            print("You leave the chest closed and enjoy the pond.")
        else:
            print("Invalid choice. You decide to head back home.")
    elif choice2 == "2":
        print("You rest by the shore and enjoy the peaceful surroundings.")
        choice3 = input("Do you want to collect some flowers (1) or take a nap (2)? ")
        if choice3 == "1":
            print("You collect beautiful flowers and make a bouquet.")
        elif choice3 == "2":
            print("You take a nap and wake up feeling refreshed.")
        else:
            print("Invalid choice. You decide to head back home.")
    else:
        print("Invalid choice. You decide to head back home.")
elif choice1 == "2":
    print("You investigate the creaking and find a friendly deer.")
    choice2 = input("Do you want to follow the deer (1) or pet it (2)? ")
    if choice2 == "1":
        print("You follow the deer and it leads you to a safe path out of the woods.")
        choice3 = input("Do you want to thank the deer (1) or continue on your own (2)? ")
        if choice3 == "1":
            print("You thank the deer for its help.")
        elif choice3 == "2":
            print("You continue on your own and find your way home.")
        else:
            print("Invalid choice. You decide to head back home.")
    elif choice2 == "2":
        print("You pet the deer and it becomes your companion for the journey.")
        choice3 = input("Do you want to name the deer (1) or let it be wild (2)? ")
        if choice3 == "1":
            print("You name the deer 'Buddy' and it follows you everywhere.")
        elif choice3 == "2":
            print("You let the deer be wild and it runs off into the woods.")
        else:
            print("Invalid choice. You decide to head back home.")
    else:
        print("Invalid choice. You decide to head back home.")
elif choice1 == "3":
    print("You move forward and find a mysterious cave.")
    choice2 = input("Do you want to enter the cave (1) or walk around it (2)? ")
    if choice2 == "1":
        print("You enter the cave and discover ancient drawings on the walls.")
        choice3 = input("Do you want to study the drawings (1) or take a picture (2)? ")
        if choice3 == "1":
            print("You study the drawings and learn about the history of the area.")
        elif choice3 == "2":
            print("You take a picture of the drawings to show your friends.")
        else:
            print("Invalid choice. You decide to head back home.")
    elif choice2 == "2":
        print("You walk around the cave and find a beautiful waterfall.")
        choice3 = input("Do you want to swim in the waterfall (1) or just admire it (2)? ")
        if choice3 == "1":
            print("You swim in the waterfall and feel rejuvenated.")
        elif choice3 == "2":
            print("You admire the waterfall and take in its beauty.")
        else:
            print("Invalid choice. You decide to head back home.")
    else:
        print("Invalid choice. You decide to head back home.")
else:
    print("Invalid choice. You decide to head back home.")
```
As you can see, in this instance else is used to demonstrate a wrong answer. In other instances, it can be used to find an outlier or the opposite. It simply gives the rest of what is possible to select. Else has many more uses. Make sure to test youtr code before turning in. This program needs to be three choices long. Remember to turn in your code by sending me the link. 