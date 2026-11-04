# Number Guessing Game

import random

# variables
lowest_number = 1
highest_number = 50
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

# cli styling
width = 35
line = "=" * width

# title menu
print(f"{"Guessing Game":'^{width}}")

game_mode = input('select a game mode: "easy" or "hard: ')

if game_mode == "easy":
    guesses = 10
elif game_mode == "hard":
    guesses = 5
else:
    print("invalid input!")

while is_running:

    print("=" * 35)        
    choice = input("Guess a number from 1-100!: ")
    print(line)

    if choice.isdigit() and lowest_number <= int(choice) <= highest_number:
        choice = int(choice)

        if choice != answer:
            print(f"{choice} is incorrect, Try Again!")
            guesses -= 1
            print(f"{guesses} remaining!")

            if guesses == 0:
                is_running = False
                print("=" * 35) 
                print(f"GAME OVER! The answer was: {answer}")
                print("=" * 35) 


        elif choice == answer:
            print(f"{"CONGRATULATIONS!":-^{width}}")
            print(f"You guessed {choice} with {guesses} remaining, and it is correct!")
            break

    else:
        print("invalid input!")
        print(f"please select a number between {lowest_number} and {highest_number}")
