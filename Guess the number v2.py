import random

# Initialize variables
random_number = random.randint(1, 100)
guess = None

print("Guess the number between 1 and 100")

# Loop until the user guesses the correct number
while guess != random_number:
    # Get the user's guess
    guess = int(input("Enter your guess: "))

    # Check if the guess is correct
    if guess == random_number:
        print("Congratulations! You guessed the correct number.")
    else:
        print("No.")
        # Provide feedback if the guess is higher or lower
        if guess < random_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
