# Dice game for rolling dice inside the terminal

import random

# ascii art of the dice
dice_art = {
    1: (" _____ ",
        "|     |",
        "|  o  |",
        "|     |",
        "|_____|",
    ),
    2: (" _____ ",
        "| o   |",
        "|     |",
        "|   o |",
        "|_____|",
    ),
    3: (" _____ ",
        "| o   |",
        "|  o  |",
        "|   o |",
        "|_____|",
    ),
    4: (" _____ ",
        "| o o |",
        "|     |",
        "| o o |",
        "|_____|",
    ),
    5: (" _____ ",
        "| o o |",
        "|  o  |",
        "| o o |",
        "|_____|",
    ),
    6: (" _____ ",
        "| o o |",
        "| o o |",
        "| o o |",
        "|_____|",
    ),
}

# variables
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

# loops
for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# - one dice per line, at a time
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)

# builds all the dice on one line
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

# totality
for die in dice:
    total += die

print(f"* Total: {total}")