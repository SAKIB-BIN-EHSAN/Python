# Problem: Check if a Word is a Palindrome
# Write a function that checks if a word or phrase is the same when reversed, ignoring spaces and punctuation.
# Note: Don't use any slicing method

# Input: "Madam"
# Output: True

def check_a_word_is_palindrome(input_word):

    cleaned_word = []
    for ch in input_word:
        if ch.isalpha():
            cleaned_word.append(ch)
    
    cleaned_word = ''.join(cleaned_word).lower()
    word_length = len(cleaned_word)

    for i in range(0, word_length-1):
        if cleaned_word[i] != cleaned_word[word_length-1-i]:
            return False
    
    return True

input_word = "Madam"
print("Input -> ", input_word)
print("Output -> ", check_a_word_is_palindrome(input_word))

input_word = "sakib bin ehsan"
print("Input -> ", input_word)
print("Output -> ", check_a_word_is_palindrome(input_word))

input_word = "*&*[]sakib!@#$bin&ehsan?"
print("Input -> ", input_word)
print("Output -> ", check_a_word_is_palindrome(input_word))

input_word = "mm"
print("Input -> ", input_word)
print("Output -> ", check_a_word_is_palindrome(input_word))

input_word = "S"
print("Input -> ", input_word)
print("Output -> ", check_a_word_is_palindrome(input_word))