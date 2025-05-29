cat=""

while (cat != "1" and cat != "2"):
    cat = input("The cat is about to push the vase off the table. \n(1)Will you stop the cat? \n(2) Or will you catch the vase?")
    if (cat != "1" and cat != "2"):
        print("Please choose 1 or 2.\n")

if cat == "1":
    broken = ""
    while (broken != "1" and broken != "2"):
        broken = input("Oh no! The cat scratched you and the vase fell anyway! \n(1)Will you hide the vase? \n(2) Or will you try to fix it?")
        if (broken != "1" and broken != "2"):
            print("Please choose 1 or 2.\n")

