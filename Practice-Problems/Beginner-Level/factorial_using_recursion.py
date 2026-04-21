# Problem: Factorial Using Recursion
# Write a function to return the factorial of a number, used in data science combinations calculation.

# Input: 5
# Output: 120

def calculate_factorial(number: int):

    if not isinstance(number, int) or number < 0:
        return "Input must be a non-negative integer"

    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)
    
input = 0
print("Input -> ", input)
print("Output -> ", calculate_factorial(input))

input = 1
print("Input -> ", input)
print("Output -> ", calculate_factorial(input))

input = 5
print("Input -> ", input)
print("Output -> ", calculate_factorial(input))

input = 6
print("Input -> ", input)
print("Output -> ", calculate_factorial(input))

input = -6
print("Input -> ", input)
print("Output -> ", calculate_factorial(input))

input = "sakib"
print("Input -> ", input)
print("Output -> ", calculate_factorial(input))