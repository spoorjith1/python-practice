import random

def roll_dice():
    return random.randint(1, 6)

def diceFn():
    print("Dice Roll Simulator")
    print("--------------------")

    while True:
        choice = input("Roll the dice? [y] for yes/ [n] for no: ").strip().lower()
        if choice == "y":
            res = roll_dice()
            print(f"🎲 You rolled: {res}")
        elif choice == "n":
            print("Thanks for playing")
            print("x--- GAME OVER ---x")
            break
        else:
            print("Please enter 'y' or 'n'.")
            
diceFn()
