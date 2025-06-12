import random
import time
d=0
d20 = list(range(1, 21))
done = "false"
while done == "false":
    try:
        a = int(input("how many times did you rob the bank?\n"))
        a+1
        done = "true"
        if a<0:
            print ("how do you rob the bank less than 1 time?")
            print ("oh, maybe you are giving money to the bank")
    except ValueError:
        print ("you are supposed to enter a integer")
        done = "false"
if a>0:
    b = list(range(1, a+1))
    for x in b:
        c=random.choice(d20)*random.choice(d20)*random.choice(d20)
        print (f"durring robbery {x} you got {c} dollars.")
        d += c
    print (f"you made a total of {d} dollars by robbing the bank")
else:
    b = list(range(1, 1-a))
    for x in b:
        c=random.choice(d20)*random.choice(d20)*random.choice(d20)
        print (f"durring gift {x} you gave the bank {c} dollars.")
        d += c
    print (f"you gave a total of {d} dollars to the bank")