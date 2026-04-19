# Problem: Flatten a Nested List
# You are given a nested list of elements (e.g., UI config data). Flatten it into a single-level list.

# Input: [1, [2, 3], [4, [5]]]
# Output: [1, 2, 3, 4, 5]


# nested_list = [1, [2, 3], [4, [5]]]
nested_list = [1, [2, 3], [4, 4, [5, [6, [6]]]]]
# nested_list = []

# Recursively flattens a nested list
def convert_into_flatten_recursive(item, flatten_list):
    if type(item) is not list:
        flatten_list.append(item)
    else:
        for sub_item in item:
            convert_into_flatten_recursive(sub_item, flatten_list)

# Flattens a nested list into a single-level list
def flatten_a_nested_list(input_list):
    flatten_list = []
    for item in input_list:
        convert_into_flatten_recursive(item, flatten_list)
    
    return flatten_list


print("Input -> ", nested_list)
print("Output -> ", flatten_a_nested_list(nested_list))
