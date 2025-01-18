import time

def check_odd_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    try:
        user_input = int(input("Enter a number: "))
        result = check_odd_even(user_input)
        print(f"The number {user_input} is {result}.")
        break  # Exit the loop if the input is valid
    except ValueError:
        attempts += 1
        print("Invalid input! Please enter a valid integer.")
        if attempts == max_attempts:
            print("3 failed attempts. You have to wait for 5 minutes.")
            for i in range(5 * 60, 0, -1):
                print(f"Waiting for {i} seconds...", end="\r")
                time.sleep(1)

print("End of the program.")