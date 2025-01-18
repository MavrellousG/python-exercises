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
        # Provide feedback if the guess is higher or lower
        if guess < random_number:
            print("Try a Higher Number")
        else:
            print("Try a Lower Number")
