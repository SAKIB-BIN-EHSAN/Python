# Problem: Count Vowels in a Sentence
# As part of a data-cleaning pipeline, count how many vowels are in a string to later analyze readability.

# Input: "Data Science is awesome"
# Output: 10

vowels = {'a', 'e', 'i', 'o', 'u'}

def count_vowels_in_sentence(sentence):

    if not sentence:
        print("Input string is empty")
        return 0

    vowels_count = 0
    
    for ch in sentence.lower():
        if ch in vowels:
            vowels_count += 1

    return vowels_count
    
# input_str = "Hello Brother"
# input_str = ""
input_str = "Data Science is Awesome"
number_of_vowels = count_vowels_in_sentence(input_str)

print("Input -> ", input_str)
print("Output -> ", number_of_vowels)