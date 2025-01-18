import time

def calculate_bonus(salary, years_of_service):
    return salary * 0.07 if years_of_service > 3 else 0

def main():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        try:
            salary = float(input("Enter your salary: "))
            years_of_service = int(input("Enter your years of service: "))
            print(f"Your bonus amount is: {calculate_bonus(salary, years_of_service)}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            attempts += 1
            if attempts == max_attempts:
                print("3 failed attempts. You have to wait for 5 minutes.")
                for i in range(5 * 60, 0, -1):
                    print(f"Waiting for {i} seconds...", end="\r")
                    time.sleep(1)
                print("\nEnd of the program.")
                break
    print("End of the program.")

if __name__ == "__main__":
    main()
