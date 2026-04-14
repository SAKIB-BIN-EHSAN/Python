# Problem: Reverse a String Without Slicing
# You are building a simple text utility tool for your web app. One of the requirements is to reverse a string input by a user.

# Input: "sakibbinehsan"
# Output: "nashenibbikas"

# Note: Don't use any slicing method

def reverse_a_string(input_str):

    if not input_str:
        return "Input string is empty"

    output_list = []
    input_length = len(input_str)

    for i in range(input_length-1, -1, -1):
        output_list.append(input_str[i])

    output_list = "".join(output_list)

    return output_list


input_str = "sakibbinehsan"
# input_str = ""
output_str = reverse_a_string(input_str)

print("Input String -> ", input_str)
print("Output String -> ", output_str)