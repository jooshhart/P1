import random

DICE_TYPES = {
    "d4": 4,
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100
}

def roll_dice(dice_type, num):
    sides = DICE_TYPES[dice_type]
    rolls = [random.randint(1, sides) for _ in range(num)]
    total = sum(rolls)
    return rolls, total