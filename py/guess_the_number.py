import random

def guessNum():
    print("x----------------------x")
    print("| Number Guessing Game |")
    print("x----------------------x")
    print()
    print("think of a number between 1 and 100?")
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess or 'q' for quit : ").strip().lower()

        if guess == "q":
            print(f"You quit. The number was {secret}.")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret:
            print("<<< Too low")
        elif guess > 100:
            print("---try below 100---")
        elif guess > secret:
            print("Too high >>>")
        else:
            print(f"Correct! -> {guess} <- You guessed it in [{attempts}] attempts.")
            break

guessNum()
