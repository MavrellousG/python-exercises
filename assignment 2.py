# Step 1: Set Up Variables
score = 0  # This will keep track of the user's score

# Step 2: Ask Questions
# Question 1
answer1 = input("What is the capital of France? ").strip().lower()
if answer1 == "paris":
    score += 1  # If the answer is correct, add 1 to the score

# Question 2
answer2 = input("What color is the sky? ").strip().lower()
if answer2 == "blue":
    score += 1  # If the answer is correct, add 1 to the score

# Question 3
answer3 = input("Which animal is the largest land animal? ").strip().lower()
if answer3 == "elephant":
    score += 1  # If the answer is correct, add 1 to the score

# Step 3: Display the Score
print("Your final score is", score, "out of 3")