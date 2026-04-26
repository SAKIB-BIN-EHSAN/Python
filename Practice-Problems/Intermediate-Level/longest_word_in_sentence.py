# Problem: Longest Word in a Sentence
# Build a function that extracts the longest word from user-generated content.

# Input: "Machine learning is fascinating"
# Output: "fascinating"

import string

def longest_word_in_sentence(sentence):

    if not isinstance(sentence, str) or sentence == "":
        raise ValueError("Input must be a valid sentence")

    words = sentence.split()

    # Solution 1
    # return max(words, key = len)

    # Solution 2
    longest_word_length = 0
    longest_word = ""

    for word in words:
        cleaned_word = word.strip(string.punctuation) # avoids punctuations as part of string
        if len(cleaned_word) > longest_word_length:
            longest_word_length = len(cleaned_word)
            longest_word = cleaned_word

    return longest_word

input_sentence = "Machine learning is fascinating" # output - fascinating
print("Input -> ", input_sentence)
print("Output -> ", longest_word_in_sentence(input_sentence))

input_sentence = "sakib!" # output - sakib
print("Input -> ", input_sentence)
print("Output -> ", longest_word_in_sentence(input_sentence))

input_sentence = "" # output - Throw an error because of empty string
print("Input -> ", input_sentence)
print("Output -> ", longest_word_in_sentence(input_sentence))

input_sentence = 1 # output - Throw an error because of non string values
print("Input -> ", input_sentence)
print("Output -> ", longest_word_in_sentence(input_sentence))