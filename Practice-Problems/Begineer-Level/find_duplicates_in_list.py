# Problem: Find Duplicates in a List
# You’re given a user-uploaded list of tags. Identify duplicates for suggestion cleanup.

# Input: ["ai", "ml", "python", "ml", "dl", "ai"]
# Output: ["ml", "ai"]

def find_duplicates_in_list(input_list):

    if len(input_list) == 0:
        print("Input is empty array")
        return []

    duplicates = set()
    unique_items = set()

    for item in input_list:
        if item in unique_items:
            duplicates.add(item)
        else: 
            unique_items.add(item)
    
    if len(duplicates) == 0:
        return []
    else:
        return duplicates


# input_list = ["ai", "ml", "python", "ml", "dl", "ai"]
# input_list = ["sas", "sas", "sas", "app"]
input_list = ["s", "a", "k", "i", "b"]
# input_list = []

print("Input -> ", input_list)
print("Output -> ", find_duplicates_in_list(input_list))


