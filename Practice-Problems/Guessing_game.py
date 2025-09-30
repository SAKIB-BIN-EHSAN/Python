# Problem: Guessing Game
# Write a function that takes a number 1 to 9 from the user input (use input function inside a function).
# Store a number in a variable (let’s assume 6).
# If the input value is less than the variable, print (your guess is almost there),
# if the input value is greater than the variable, print - your guess is higher,
# if the input value and variable are equals, print - Your Guess Is Correct!

import random

# Generate a random number between 1 and 9(inclusive)
guessed_number = random.randint(1, 9)

while (1):
    user_input = int(input("Enter a number between 1 and 9: "))

    if user_input < 1 or user_input > 9:
        print("The number must be in between 1 and 9")
        continue
    else:
        if user_input < guessed_number:
            print("Your guess is almost there")
        elif user_input > guessed_number:
            print("Your guess is higher")
        else:
            print("Your Guess Is Correct!")
            break
