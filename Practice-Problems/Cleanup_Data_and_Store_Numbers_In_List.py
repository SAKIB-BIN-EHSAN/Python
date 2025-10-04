# Problem: The list below is the collection of the ages of people from a village.
# Clean up the data and store only numbers in another list.
# data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]
new_list = []

for item in data_list:
    if (isinstance(item, int)):
        new_list.append(item)

print("--- New List ---")
print(new_list)
