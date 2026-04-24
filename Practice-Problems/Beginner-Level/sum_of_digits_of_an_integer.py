# Problem: Sum of Digits of an Integer
# For a gamification feature, sum the digits of a user’s ID to generate a unique color code.

# Input: 9875
# Output: 29

def sum_of_digits(number: int) -> int:

    if number < 0 or not isinstance(number, int):
        return 0

    # Solution 1
    # return sum(int(num) for num in str(number))

    # Solution 2
    digit_sum = 0
    while number != 0:
        digit_sum += int(number % 10)
        number = int(number / 10)
    
    return digit_sum

input = 243 # output 9
print("Input -> ", input)
print("Output -> ", sum_of_digits(input))

input = 9875 # output 29
print("Input -> ", input)
print("Output -> ", sum_of_digits(input))

input = 0 # output 0
print("Input -> ", input)
print("Output -> ", sum_of_digits(input))

input = 1 # output 1
print("Input -> ", input)
print("Output -> ", sum_of_digits(input))

input = -5 # output 0
print("Input -> ", input)
print("Output -> ", sum_of_digits(input))

input = 22 # output 4
print("Input -> ", input)
print("Output -> ", sum_of_digits(input))