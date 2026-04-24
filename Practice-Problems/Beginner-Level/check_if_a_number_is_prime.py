# Problem: Check if a number is prime
# Write a function to check if a number is prime, useful in some encryption schemes.

# Input: 29
# Output: True

from typing import Union
import math

def is_prime(number: int) -> Union[bool, str]:

    if not isinstance(number, int) or number < 0:
        return "Input must be a non-negative integer"

    if number == 0 or number == 1:
        return False

    if number == 2:
        return True

    upper_limit = int(math.sqrt(number))+1
    for divisor in range(2, upper_limit):
        if (number % divisor == 0):
            return False
    
    return True

input = 2 # Prime
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = 7 # Prime
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = 13 # Prime
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = 14 # Not a prime
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = 0 # Not a prime
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = 1 # Not a prime
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = 8 # Not a prime
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = -7
print("Input -> ", input)
print("Output -> ", is_prime(input))

input = "Sakib"
print("Input -> ", input)
print("Output -> ", is_prime(input))