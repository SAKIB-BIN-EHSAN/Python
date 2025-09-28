# Problem: Write a function that takes 2 numbers as arguments (age of two brothers) and find who is elder

def find_elder_brother(age1, age2):
    if age1 > age2:
        return "Brother 1 is elder"
    elif age2 > age1:
        return "Brother 2 is elder"
    else:
        return "Both brothers are of the same age"


# Example usage 1
age_brother1 = 25
age_brother2 = 30

print(find_elder_brother(age_brother1, age_brother2))

# Example usage 2
age_brother1 = 10
age_brother2 = 5

print(find_elder_brother(age_brother1, age_brother2))

# Example usage 3
age_brother1 = 20
age_brother2 = 20

print(find_elder_brother(age_brother1, age_brother2))
