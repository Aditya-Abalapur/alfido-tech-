import random

# The computer chooses a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of guesses
guesses_left = 7

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {guesses_left} guesses to find it.")

# Loop to allow the player to guess
while guesses_left > 0:
    try:
        # Get the player's guess
        guess = int(input("Enter your guess: "))

        # Check if the guess is within the valid range
        if not 1 <= guess <= 100:
            print("Please guess a number between 1 and 100.")
            continue

        # Check the guess against the secret number
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            break  # End the game if the guess is correct

        # Decrement the number of guesses left
        guesses_left -= 1
        print(f"You have {guesses_left} guesses left.")

    except ValueError:
        print("Invalid input. Please enter a whole number.")

# This code runs if the loop finishes without a correct guess
if guesses_left == 0 and guess != secret_number:
    print("\nGame Over!")
    print(f"The number I was thinking of was {secret_number}.")
