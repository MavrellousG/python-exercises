favouriteCountries = ["India", "UK", "Spain", "Greece"]

# for i in favouriteCountries:
#     print(i)
#     if favouriteCountries[2]== "Spain":
#         print("Yaaay Spain is 3rd in your list of favourite countries")
#         break
#     else:
#         print("Boooo Spain is not 3rd in your list of favourite countries")
#         break

# for i in favouriteCountries:
#     print(i)
#     if i== "Spain":
#         print("Yaaay Spain is 3rd in your list of favourite countries")
#     else:
#         print("Boooo Spain is not 3rd in your list of favourite countries")


'''
userInput = input("Enter Name: ")
# for i in range(len(userInput)-1,-1,-1):
#     print(userInput[i])'''


# To print the characters of user input in reverse order without using the `reverse` method, you can iterate through the string from the end to the beginning. Here’s how you can do it:

# ### Step-by-Step Explanation

# 1. **Get User Input**:
#    - Use the `input()` function to get the user input.
#    ```python
#    userInput = input("Enter Name: ")
#    ```

# 2. **Initialize a `for` Loop**:
#    - Use a `for` loop with the `range()` function to iterate from the last index of the string to the first index.
#    ```python
#    for i in range(len(userInput) - 1, -1, -1):
#        print(userInput[i])
#    ```

# ### Complete Code
# Here's the complete code with comments explaining each step:

# ```python
# # Get user input
# userInput = input("Enter Name: ")

# # Loop through the input string in reverse order
# for i in range(len(userInput) - 1, -1, -1):
#     print(userInput[i])



# ### Explanation
# - `range(len(userInput) - 1, -1, -1)` generates a sequence of indices from the last index to the first index. Here’s what each parameter means:
#   - `len(userInput) - 1`: The starting index (last index of the string).
#   - `-1`: The stopping index (the loop stops just before this index, so it includes the first index).
#   - `-1`: The step, which indicates that the loop should decrement by 1 in each iteration.

# - Inside the loop, `userInput[i]` accesses the character at the current index `i` and prints it.

# This code will print the characters of the user input in reverse order, one character per line.

# I hope this helps! Let me know if you have any more questions or need further clarification.

   
    #USING Slicing

    #Take the string
    #Reverse the string
    #[::-1]# reverse the string
    #apply loop and print character by character

'''userInput = input("Enter Name: ")
for i in userInput[::-1]:
    print(i)
print(userInput[::-1])'''

 #USING Slicing

    #Take the string
    #Reverse the string
    #[::-1]# reverse the string
    #apply loop and print character by character
'''userInput = input("Enter Name: ")
reversed = userInput[::-1]
for character in reversed:
    print(character)'''


#pseudo code

#save a target number
# guess the number
# if number is correct forward
# if number isn't correct keep trying
# unless correct number is found
# user random library to generate random number

import random

targerNumber = 6
guess = random.randint(1, 6) #made by system
counter = 1

while guess != targerNumber:
    
    print("Your guess is incorrect")
    guess = random.randint(1, 6)
    print("Guess again: ", guess)
    counter += 1
# if guess == targerNumber:
# print(guess)
print("You guessed the correct number", guess, " after ", counter, "attempts")


# Create  repository named Python Exercises