# Problem: Capitalize First Letter of Each Word
# Build a custom title formatter that capitalizes the first letter of each word without using .title().

# Input: "python for web developers"
# Output: "Python For Web Developers"


def title_formatter(sentence):

    if not isinstance(sentence, str):
        return "Input must be a string"

    words = sentence.split()

    # convert each word's first character into capitalize form
    # Note: In Python, parentheses () around a loop like this create a Generator. A generator is like a "lazy" list. It doesn't actually create the list of words in memory immediately; it just prepares the logic to create them when needed.
    output_sentence = (word[0].upper() + word[1:] for word in words)
    return " ".join(output_sentence)

    # line 17 & line 18 can be written in 1 one like below
    # return " ".join(word[0].upper() + word[1:] for word in words)

input_sentence = "python for web developers"
# input_sentence = "this is sakib bin ehsan!"
# input_sentence = ""
# input_sentence = 1

print("Input -> ", input_sentence)
print("Output -> ", title_formatter(input_sentence))