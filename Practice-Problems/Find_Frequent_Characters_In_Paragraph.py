# Problem: Find the most frequent character in the paragraph
# rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!

from collections import Counter

rhyme = "Twinkle, twinkle, little star. How I wonder what you are!"
rhyme_without_spaces = ""

# Removing the spaces from the rhyme
for char in rhyme:
    if char != ' ':
        rhyme_without_spaces += char

# Finding the most repeated character using built-in function
frequency_of_characters = Counter(rhyme_without_spaces)

most_repeated_character = max(
    frequency_of_characters, key=frequency_of_characters.get)

print(most_repeated_character)

# Finding the most repeated character using loop
dict_of_characters_count = {}
for char in rhyme_without_spaces:
    dict_of_characters_count[char] = dict_of_characters_count.get(char, 0) + 1

most_frequent_character = max(
    dict_of_characters_count, key=dict_of_characters_count.get)

print(most_frequent_character)
