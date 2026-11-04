# Concession Stand Program (no AI to write)

# Menu items and their prices
menu = {"popcorn": 1.00,
        "hotdog": 2.00,
        "pretzel": 2.00,
        "candy": 0.75,
        "soda": 1.00,
        "water": 1.25}

# Menu / Total variables
cart = []
total = 0

# Menu items
print( 6 * "*" + " Menu " + 6 * "*")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print( 18 * "*" )

# Running program
while True:
    food = input("Select an item (q to quit): ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

# Cart / Order / Total
print( 6 * "*" + " Your Order " + 6 * "*")

for food in cart:
    total += menu.get(food)
    print(food.capitalize(), end=" ")

print()
print(f"Your total is: ${total:.2f}")
print( 24 * "*" )